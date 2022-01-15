from .models import UserAgent, Product
from .enums import ProductName
from .parser import Parser

import sys
import types

parse = Parser.parse


class UserAgentModule(types.ModuleType):
    @staticmethod
    def __call__(useragent: str) -> UserAgent:
        return Parser.parse(useragent)


sys.modules[__name__].__class__ = UserAgentModule
