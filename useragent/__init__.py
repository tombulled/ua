from .models import UserAgent, Product, ProductIdentifier
from .enums  import ProductName
from .parser import Parser

parse = Parser.parse

import sys
import types

class UserAgentModule(types.ModuleType):
    @staticmethod
    def __call__(useragent: str) -> UserAgent:
        return Parser.parse(useragent)

sys.modules[__name__].__class__ = UserAgentModule
