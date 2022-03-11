import ua


def test_parser() -> None:
    user_agent: ua.UserAgent = ua.parse(
        "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0"
    )

    assert user_agent == ua.UserAgent(
        products=[
            ua.Product(
                name="Mozilla",
                version="5.0",
                comments=["X11", "Linux x86_64", "rv:88.0"],
            ),
            ua.Product(name="Gecko", version="20100101", comments=[]),
            ua.Product(name="Firefox", version="88.0", comments=[]),
        ]
    )
