import pytest
import ua


@pytest.fixture
def product() -> ua.Product:
    return ua.Product(
        name="SomeProduct", version="1.0", comments=["comment-1", "comment-2"]
    )


def test_identifier(product: ua.Product) -> None:
    assert product.identifier == "SomeProduct/1.0"


def test_product(product: ua.Product) -> None:
    assert str(product) == "SomeProduct/1.0 (comment-1; comment-2)"
