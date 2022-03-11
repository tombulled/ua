import pytest
import ua


@pytest.fixture
def user_agent() -> ua.UserAgent:
    return ua.UserAgent(
        products=[
            ua.Product(
                name="Mozilla",
                version="5.0",
                comments=["X11", "Linux x86_64", "rv:88.0"],
            ),
            ua.Product(name="Firefox", version="88.0", comments=[]),
        ]
    )


def test_str(user_agent: ua.UserAgent) -> None:
    assert str(user_agent) == "Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Firefox/88.0"


def test_iter(user_agent: ua.UserAgent) -> None:
    assert list(user_agent) == user_agent.products
