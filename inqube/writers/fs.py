from inqube.utils.fileutils import write_jsonlines_file, write_csv_file
from inqube.writers import BaseWriter, BaseWriterConfig


class FileSystemWriterConfig(BaseWriterConfig):
    _NAME = "FileSystemWriterConfig"


class FileSystemWriter(BaseWriter):

    _NAME = "FileSystemWriter"
    _CFG_CLASS = FileSystemWriterConfig

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def write(self, data: list[dict]):
        output_path = f"{self.cfg.filepath}/{self._get_filename()}.{self.cfg.format}"
        if self.cfg.format == "json":
            write_jsonlines_file(output_path, data)
        elif self.cfg.format == "csv":
            write_csv_file(output_path, data)

