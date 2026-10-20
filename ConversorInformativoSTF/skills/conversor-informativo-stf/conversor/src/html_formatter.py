from __future__ import annotations

from html import escape

from .schemas import Paragraph, TextRun


LINK_ATTRS = 'target="_blank" rel="noopener noreferrer nofollow"'


def _format_run(run: TextRun) -> str:
    text = escape(run.text)
    if not text:
        return ""

    if run.href:
        content = text
        if run.bold:
            content = f"<strong>{content}</strong>"
        if run.italic:
            content = f"<em>{content}</em>"
        content = f"<u>{content}</u>"
        return f'<a {LINK_ATTRS} href="{escape(run.href, quote=True)}">{content}</a>'

    if run.underline:
        text = f"<u>{text}</u>"
    if run.italic:
        text = f"<em>{text}</em>"
    if run.bold:
        text = f"<strong>{text}</strong>"
    return text


def paragraph_inline_html(paragraph: Paragraph) -> str:
    if paragraph.runs:
        return "".join(_format_run(run) for run in paragraph.runs).strip()
    return escape(paragraph.text).strip()


def paragraph_to_html(paragraph: Paragraph) -> str:
    content = paragraph_inline_html(paragraph)
    return f"<p>{content}</p>" if content else ""


def paragraphs_to_html(paragraphs: list[Paragraph]) -> str | None:
    """Converte paragrafos em HTML, preservando listas simples."""

    parts: list[str] = []
    list_items: list[str] = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            parts.append("<ul>" + "".join(list_items) + "</ul>")
            list_items = []

    for paragraph in paragraphs:
        if not paragraph.text.strip():
            continue

        paragraph_html = paragraph_to_html(paragraph)
        if not paragraph_html:
            continue

        if paragraph.is_list_item:
            list_items.append(f"<li>{paragraph_html}</li>")
            continue

        flush_list()
        parts.append(paragraph_html)

    flush_list()
    return "\n".join(parts) if parts else None


def paragraphs_to_list_html(paragraphs: list[Paragraph]) -> str | None:
    items = [f"<li>{paragraph_to_html(paragraph)}</li>" for paragraph in paragraphs if paragraph.text.strip()]
    if not items:
        return None
    return "<ul>\n" + "\n".join(items) + "\n</ul>"
