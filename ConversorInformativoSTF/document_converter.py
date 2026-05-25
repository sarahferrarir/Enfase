import mammoth


def docx_to_markdown(docx_path: str) -> str:
    with open(docx_path, "rb") as file:
        result = mammoth.convert_to_markdown(file)
        return result.value