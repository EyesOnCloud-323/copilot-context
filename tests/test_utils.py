import pytest

from app.utils import format_error
from app.utils import slugify


def test_format_error_uses_default_status():
    response, status = format_error("Invalid request")

    assert response == {"error": "Invalid request"}
    assert status == 400


def test_format_error_uses_provided_status():
    response, status = format_error("Not found", 404)

    assert response == {"error": "Not found"}
    assert status == 404


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello, World!", "hello-world"),
        ("  multiple   spaces  ", "multiple-spaces"),
        ("Café déjà vu", "cafe-deja-vu"),
        ("", ""),
    ],
)
def test_slugify_normalizes_text(text, expected):
    assert slugify(text) == expected


def test_slugify_rejects_non_string_input():
    with pytest.raises(ValueError, match="text must be a string"):
        slugify(None)
