import re
import unicodedata


def format_error(message, status=400):
    return {"error": message}, status


def slugify(text: str) -> str:
    """Convert text into a lowercase, hyphen-separated ASCII slug.

    Args:
        text: The text to convert.

    Returns:
        The normalized slug, with runs of non-alphanumeric characters replaced
        by a single hyphen.

    Raises:
        ValueError: If text is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")

    normalized_text = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("ascii")
        .lower()
    )
    return re.sub(r"[^a-z0-9]+", "-", normalized_text).strip("-")
