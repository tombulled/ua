# useragent
User Agent parsing and creation

## Usage
```python
>>> import useragent
>>>
>>> user_agent = useragent.parse('Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0')
>>>
>>> user_agent
UserAgent(
    products=[
        Product(identifier=ProductIdentifier(name='Mozilla', version='5.0'), comments=['X11', 'Linux x86_64', 'rv:88.0']),
        Product(identifier=ProductIdentifier(name='Gecko', version='20100101'), comments=[]),
        Product(identifier=ProductIdentifier(name='Firefox', version='88.0'), comments=[])
    ]
)
>>>
```
