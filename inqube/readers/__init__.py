from importlib import import_module

from inqube.configs import Config
from inqube.exceptions import BaseMethodNotImplementedException, ConfigMissingRequiredException


class BaseReaderConfig(Config):

    _NAME = "BaseReaderConfig"
    _BASE_REQUIRED = {
        "entity"
    }
    _ENTITY_REQUIRED = dict()

    def __init__(self, *args, **kwargs):
        if type(self) == BaseReaderConfig:
            raise Exception(f"{self._NAME} must be subclassed.")
        super().__init__(*args, **kwargs)
        self.__validate_entity_required()

    def __validate_entity_required(self):
        entity = self._cfg["entity"]
        missing_fields = set(self._ENTITY_REQUIRED[entity]) - set(self._cfg.keys())
        if missing_fields:
            raise ConfigMissingRequiredException(
                f"{self._NAME} missing required fields: {missing_fields} for entity {entity}")


class BaseReader:

    _NAME = "BaseReader"
    _CFG_CLASS = BaseReaderConfig

    def __init__(self, cfg: dict):
        if type(self) == BaseReader:
            raise Exception(f"{self._NAME} must be subclassed.")
        self.cfg = self._CFG_CLASS(cfg)

    def read(self) -> list[dict]:
        raise BaseMethodNotImplementedException(f"Read method not implemented for {self._NAME}!")
