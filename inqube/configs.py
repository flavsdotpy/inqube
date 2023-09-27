from inqube.exceptions import ConfigMissingRequiredException


class Config:

    _NAME = "Config"
    _REQUIRED = set()
    _BASE_REQUIRED = set()
    _OPTIONAL = dict()
    _BASE_OPTIONAL = dict()

    def __init__(self, cfg: dict):
        if type(self) == Config:
            raise Exception(f"{self._NAME} must be subclassed.")
        self._cfg = cfg
        self._req = self._REQUIRED | self._BASE_REQUIRED
        self._opt = self._OPTIONAL | self._BASE_OPTIONAL
        self.__validate()

    def __getattr__(self, __name: str):
        if __name in self._cfg:
            return self._cfg[__name]
        elif __name in self._opt:
            return self._opt[__name]
        else:
            raise Exception(f"{self._NAME} does not have attribute {__name}")

    def __validate(self):
        missing_fields = self._req - set(self._cfg.keys())
        if missing_fields:
            raise ConfigMissingRequiredException(f"{self._NAME} missing required fields: {missing_fields}")
