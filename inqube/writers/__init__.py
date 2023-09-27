from importlib import import_module
from uuid import uuid4

from inqube.configs import Config
from inqube.exceptions import BaseMethodNotImplementedException


class BaseWriterConfig(Config):

    _NAME = "BaseWriterConfig"
    _BASE_REQUIRED = {
        "filepath",
        "format"
    }
    _BASE_OPTIONAL = {
        "filename": None
    }

    def __init__(self, *args, **kwargs):
        if type(self) == BaseWriterConfig:
            raise Exception(f"{self._NAME} must be subclassed.")
        super().__init__(*args, **kwargs)


class BaseWriter:

    _NAME = "BaseWriter"
    _CFG_CLASS = BaseWriterConfig

    def __init__(self, cfg: dict):
        if type(self) == BaseWriter:
            raise Exception(f"{self._NAME} must be subclassed.")
        self.cfg = self._CFG_CLASS(cfg)

    def _get_filename(self):
        return self.cfg.filename or str(uuid4())

    def write(self, data: list[dict]):
        raise BaseMethodNotImplementedException(f"Write method not implemented for {self._NAME} !")
