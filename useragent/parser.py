import addict

import typing

from . import types
from . import models

def chunk(user_agent: str) -> typing.List[str]:
    chunks = []

    for segment in user_agent.split():
        if '/' in segment or not chunks:
            chunks.append(segment)
        else:
            chunks[-1] += f' {segment}'

    return chunks

def parse(user_agent: str) -> models.UserAgent:
    products = []

    for segment in chunk(user_agent):
        segment = types.ParsableString(segment.strip())

        comments = []

        if (result := segment.search('({comment})')):
            result = addict.Dict(result.__dict__)

            comments = list(map(str.strip, result.named.comment.split(';')))

            segment = types.ParsableString(segment[:result.spans.comment[0] - 1].strip())

        if (result := segment.parse('{name}/{version}')):
            result = addict.Dict(result.__dict__)

            product = models.Product \
            (
                identifier = models.ProductIdentifier \
                (
                    name    = result.named.name,
                    version = result.named.version,
                ),
                comments = comments,
            )

            products.append(product)

    return models.UserAgent \
    (
        products = products
    )
