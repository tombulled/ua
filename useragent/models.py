import pydantic

import typing

class BaseModel(pydantic.BaseModel): pass

class ProductIdentifier(BaseModel):
    name:     str
    version:  str

    def __str__(self) -> str:
        return f'{self.name}/{self.version}'

class Product(BaseModel):
    identifier: ProductIdentifier
    comments:   typing.List[str] = pydantic.Field \
    (
        default_factory = list,
    )

    def __str__(self):
        return str(self.identifier) + \
        (
            ' ({comment})'.format \
            (
                comment = '; '.join(self.comments),
            )
            if self.comments
            else ''
        )

class UserAgent(BaseModel):
    products: typing.List[Product]

    def __str__(self):
        return ' '.join(map(str, self.products))
