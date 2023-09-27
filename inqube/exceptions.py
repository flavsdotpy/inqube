# general
class BaseMethodNotImplementedException(Exception):
    pass

class InvalidFileFormatException(Exception):
    pass

# cfg
class ConfigMissingRequiredException(Exception):
    pass

class ConfigInvalidValueException(Exception):
    pass

# reader
class ReaderAPIRequestFailure(Exception):
    pass
