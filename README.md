# useragent
User Agent parsing and creation

## Usage
```python
>>> import useragent
>>>
>>> useragent('Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0')
UserAgent(
    products=[
        Product(identifier=ProductIdentifier(name='Mozilla', version='5.0'), comments=['X11', 'Linux x86_64', 'rv:88.0']),
        Product(identifier=ProductIdentifier(name='Gecko', version='20100101'), comments=[]),
        Product(identifier=ProductIdentifier(name='Firefox', version='88.0'), comments=[])
    ]
)
```

## References
* [Wikipedia - User agent](https://en.wikipedia.org/wiki/User_agent)
* [Mozilla - HTTP > User-Agent](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent)
* [RFC-7231 - Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content (Section 5.5.3)](https://datatracker.ietf.org/doc/html/rfc7231#section-5.5.3)
