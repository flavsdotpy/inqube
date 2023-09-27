import yaml
from importlib import import_module

from inqube.exceptions import ConfigInvalidValueException
from inqube.processors import BaseProcessor
from inqube.readers import BaseReader
from inqube.writers import BaseWriter


class InQubeRunner:

    @staticmethod
    def load_class(cls: str, component_type: str):
        groups = cls.split(".")
        module = ".".join(groups[:-1])
        if not module.startswith(f"inqube.{component_type}."):
            raise ConfigInvalidValueException(f"Invalid class `{cls}` for `{component_type}`")
        return getattr(import_module(module), groups[-1])

    @staticmethod
    def run(yaml_content: str):
        cfg = yaml.safe_load(yaml_content)
        reader_cfg = cfg.pop("reader")
        reader: BaseReader = InQubeRunner.load_class(reader_cfg.pop("class"), "readers")(reader_cfg)
        data = reader.read()

        for processor_cfg in cfg.pop("processors"):
            processor: BaseProcessor = InQubeRunner.load_class(processor_cfg.pop("class"), "processors")(processor_cfg)
            data = processor.process(data)

        writer_cfg = cfg.pop("writer")
        writer: BaseWriter = InQubeRunner.load_class(writer_cfg.pop("class"), "writers")(writer_cfg)
        writer.write(data)
