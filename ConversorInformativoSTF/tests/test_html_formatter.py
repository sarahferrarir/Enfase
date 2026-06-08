from __future__ import annotations

import unittest

from src.html_formatter import paragraphs_to_html, paragraphs_to_list_html
from src.schemas import Paragraph, TextRun


class HtmlFormatterTest(unittest.TestCase):
    def test_formats_paragraph_runs_and_links(self) -> None:
        paragraph = Paragraph(
            index=1,
            text="Texto com link",
            runs=[
                TextRun(text="Texto ", bold=True),
                TextRun(text="com "),
                TextRun(text="link", href="https://example.com?a=1&b=2"),
            ],
        )

        self.assertEqual(
            paragraphs_to_html([paragraph]),
            '<p><strong>Texto </strong>com <a target="_blank" rel="noopener noreferrer nofollow" href="https://example.com?a=1&amp;b=2"><u>link</u></a></p>',
        )

    def test_formats_footer_as_list(self) -> None:
        paragraphs = [
            Paragraph(index=1, text="RE 1/RJ, relator Ministro A"),
            Paragraph(index=2, text="RE 2/SP, relator Ministro B"),
        ]

        self.assertEqual(
            paragraphs_to_list_html(paragraphs),
            "<ul>\n<li><p>RE 1/RJ, relator Ministro A</p></li>\n<li><p>RE 2/SP, relator Ministro B</p></li>\n</ul>",
        )


if __name__ == "__main__":
    unittest.main()
