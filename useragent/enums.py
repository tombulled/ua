import humps

import enum

class StrEnum(str, enum.Enum): pass

class AutoPascalName(StrEnum):
    _generate_next_value_ = lambda name, *_: humps.pascalize(name.lower())

class ProductName(AutoPascalName):
    MOZILLA: str = enum.auto()
    GECKO:   str = enum.auto()
    FIREFOX: str = enum.auto()
