import re


def clean_markdown(text: str) -> str:
    # Remove anchors HTML
    text = re.sub(r"<a[^>]*></a>", "", text)

    # Remove imagens base64
    text = re.sub(r"!\[\]\(data:image[^)]*\)", "", text)

    # Remove barras de escape
    text = text.replace("\\.", ".")
    text = text.replace("\\-", "-")
    text = text.replace("\\(", "(")
    text = text.replace("\\)", ")")

    # Remove espaços extras
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()