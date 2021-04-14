import parse

class MetaParsableString(type):
    def __new__(cls, name, bases, attrs):
        for key in parse.__all__:
            func = getattr(parse, key)

            def decorator(func):
                def wrapper(self, format: str):
                    return func(format, self)

                return wrapper

            attrs[key] = decorator(func)

        return super().__new__(cls, name, bases, attrs)

class ParsableString(str, metaclass = MetaParsableString): pass
