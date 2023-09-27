from inqube.configs import Config
from inqube.exceptions import BaseMethodNotImplementedException


class BaseProcessorConfig(Config):

    _NAME = "BaseProcessorConfig"

    def __init__(self, *args, **kwargs):
        if type(self) == BaseProcessorConfig:
            raise Exception(f"{self._NAME} must be subclassed.")
        super().__init__(*args, **kwargs)


class BaseProcessor:

    _NAME = "BaseProcessor"
    _CFG_CLASS = BaseProcessorConfig

    def __init__(self, cfg: dict):
        if type(self) == BaseProcessor:
            raise Exception(f"{self._NAME} must be subclassed.")
        self.cfg = self._CFG_CLASS(cfg)

    def process(self, data: list[dict]) -> list[dict]:
        raise BaseMethodNotImplementedException(f"Read method not implemented for {self._NAME}!")
