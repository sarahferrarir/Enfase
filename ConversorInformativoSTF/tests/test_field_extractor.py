from __future__ import annotations

import unittest

from src.field_extractor import extract_fields
from src.schemas import EditorialItem, InformativoMetadata, Paragraph


def _item(title: str, noticia_extra: str = "") -> EditorialItem:
    paragraphs = [
        Paragraph(index=1, text="DIREITO TRIBUTARIO - CONTRIBUICAO SOCIAL"),
        Paragraph(index=2, text=title),
        Paragraph(index=3, text="Resumo:"),
        Paragraph(
            index=4,
            text=(
                "E constitucional a sujeicao passiva das cooperativas "
                "a contribuicao destinada ao custeio da seguridade social."
            ),
        ),
    ]
    if noticia_extra:
        paragraphs.append(Paragraph(index=5, text=noticia_extra))
    paragraphs.append(
        Paragraph(
            index=6,
            text=(
                "[RE 597.315/RJ, relator Ministro Dias Toffoli, "
                "julgamento finalizado em 30.05.2026]"
            ),
        )
    )
    return EditorialItem(paragraphs=paragraphs)


class FieldExtractorThemeRGTest(unittest.TestCase):
    def test_extracts_theme_rg_from_main_title_process(self) -> None:
        julgado = extract_fields(
            _item(
                "Sujeicao passiva das cooperativas a contribuicao destinada "
                "ao custeio da seguridade social - RE 597.315/RJ (Tema 516 RG)"
            ),
            InformativoMetadata(numero_informativo="1218"),
        )

        self.assertEqual(julgado.classe_processo, "RE")
        self.assertEqual(julgado.numero_processo, "597315")
        self.assertEqual(julgado.uf, "RJ")
        self.assertEqual(julgado.tema_rg, "516 RG")
        self.assertEqual(julgado.repercussao_geral, "sim")
        self.assertEqual(
            julgado.titulo,
            "Sujeicao passiva das cooperativas a contribuicao destinada ao custeio da seguridade social",
        )
        self.assertNotIn("Tema 516 RG", julgado.titulo or "")

    def test_does_not_extract_theme_rg_from_precedents(self) -> None:
        julgado = extract_fields(
            _item(
                "Sujeicao passiva das cooperativas a contribuicao destinada "
                "ao custeio da seguridade social - RE 597.315/RJ",
                "Precedentes citados: RE 599.362 (Tema 323 RG) e RE 598.085 (Tema 177 RG).",
            ),
            InformativoMetadata(numero_informativo="1218"),
        )

        self.assertIsNone(julgado.tema_rg)
        self.assertIsNone(julgado.repercussao_geral)


if __name__ == "__main__":
    unittest.main()
