from inqube.processors import BaseProcessor, BaseProcessorConfig


class DropColumnsProcessorConfig(BaseProcessorConfig):
    _NAME = "DropColumnsProcessorConfig"
    _REQUIRED = {
        "columns_to_drop"
    }


class DropColumnsProcessor(BaseProcessor):

    _NAME = "DropColumnsProcessor"
    _CFG_CLASS = DropColumnsProcessorConfig

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process(self, data):
        for row in data:
            for column in self.cfg.columns_to_drop:
                del row[column]
        return data
