import re
from typing import List, Tuple
from .schemas import Julgado


class JulgadoValidator:
    """Valida e corrige julgados extraídos."""

    @staticmethod
    def is_valid(julgado: Julgado, original_text: Optional[str] = None) -> Tuple[bool, List[str]]:
        """
        Valida rigorosamente um julgado extraído.
        Para ser válido, DEVE ter: classe, número, título e resumo.

        Args:
            julgado: instância de Julgado
            original_text: texto original (opcional, para validação cross-check)

        Returns:
            Tuple (is_valid: bool, issues: List[str])
        """
        issues = []

        # Validação 1: DEVE ter classe_processo
        has_classe = julgado.classe_processo and str(julgado.classe_processo).strip()
        if not has_classe:
            issues.append("❌ OBRIGATÓRIO: classe_processo ausente")
            return False, issues

        # Validação 2: DEVE ter numero_processo
        has_numero = julgado.numero_processo and str(julgado.numero_processo).strip()
        if not has_numero:
            issues.append("❌ OBRIGATÓRIO: numero_processo ausente")
            return False, issues

        # Validação 3: DEVE ter titulo
        has_titulo = julgado.titulo and str(julgado.titulo).strip()
        if not has_titulo:
            issues.append("❌ OBRIGATÓRIO: titulo ausente")
            return False, issues

        # Validação 4: DEVE ter resumo
        has_resumo = julgado.resumo and str(julgado.resumo).strip()
        if not has_resumo:
            issues.append("❌ OBRIGATÓRIO: resumo ausente")
            return False, issues

        # Validação 5: Classe deve ser válida
        classes_validas = [
            "ADI", "ADPF", "ADO", "ADC", "RE", "ARE",
            "HC", "MS", "Rcl", "RCL", "ACO", "SL", "PET"
        ]
        classe_str = str(julgado.classe_processo).strip().upper()
        # Deve conter EXATAMENTE uma classe (não multipla)
        if ";" in classe_str or "/" in classe_str or "," in classe_str:
            issues.append(f"❌ Classe inválida (múltiplas): {julgado.classe_processo}")
            return False, issues

        if not any(c in classe_str for c in classes_validas):
            issues.append(f"❌ Classe desconhecida: {julgado.classe_processo}")
            return False, issues

        # Validação 6: Número deve ser único (não múltiplos)
        numero_str = str(julgado.numero_processo).strip()
        if numero_str.count("e") > 0 or numero_str.count(",") > 1:
            issues.append(f"❌ Número inválido (múltiplos): {numero_str}")
            return False, issues

        # Validação 7: Resumo não deve ser apenas referência processual
        resumo_str = str(julgado.resumo).strip()
        if resumo_str.startswith("[") and resumo_str.endswith("]"):
            issues.append(f"❌ Resumo é apenas referência: {resumo_str[:50]}...")
            return False, issues

        # Validação 8: Resumo deve ter tamanho mínimo (50 chars)
        if len(resumo_str) < 50:
            issues.append(f"❌ Resumo muito curto ({len(resumo_str)} chars): {resumo_str}")
            return False, issues

        # Validação 9: Título deve ter tamanho mínimo
        titulo_str = str(julgado.titulo).strip()
        titulo_clean = titulo_str.replace("*", "").replace("_", "").strip()
        if len(titulo_clean) < 10:
            issues.append(f"❌ Título muito curto: {titulo_str}")
            return False, issues

        # Validação 10: Cross-check com texto original (se disponível)
        if original_text:
            if numero_str not in original_text:
                issues.append(
                    f"⚠️ Número não encontrado no texto: {numero_str}"
                )
                # Não invalida, apenas warning

        is_valid = len(issues) == 0
        return is_valid, issues

    @staticmethod
    def clean_field(text: Optional[str]) -> Optional[str]:
        """
        Limpa campo removendo markdown extras, espaços extras.

        Args:
            text: texto do campo

        Returns:
            Texto limpo ou None
        """
        if not text:
            return None

        text = str(text).strip()

        # Remove markdown
        text = re.sub(r"__\*|\*__|\*\*|__|\*", "", text)

        # Remove espaços extras
        text = re.sub(r"\s+", " ", text).strip()

        # Remove HTML se houver
        text = re.sub(r"<[^>]+>", "", text).strip()

        return text if text else None

    @staticmethod
    def normalize_numero_processo(numero: Optional[str]) -> Optional[str]:
        """
        Normaliza número do processo para formato padrão.
        Esperado: XXX 123456/UF

        Args:
            numero: número em formato solto

        Returns:
            Número normalizado ou None
        """
        if not numero:
            return None

        numero = str(numero).strip().upper()

        # Remove espaços e caracteres inválidos
        numero = re.sub(r"[^\w/\-\.]", " ", numero)
        numero = " ".join(numero.split())

        return numero if numero else None

    @staticmethod
    def merge_julgados(
        julgados: List[Julgado],
    ) -> List[Julgado]:
        """
        Remove duplicatas e une entradas do mesmo processo.
        Prioriza a versão mais completa (com mais campos preenchidos).

        Args:
            julgados: lista de julgados

        Returns:
            Lista sem duplicatas, com entradas unidas quando possível
        """
        if not julgados:
            return []

        # Normaliza números para agrupar duplicatas
        numero_map = {}  # numero_normalizado -> [julgados]

        for j in julgados:
            if not j.numero_processo:
                continue

            # Normaliza número: remove pontos, espaços extras
            numero_norm = JulgadoValidator.normalize_numero_processo(j.numero_processo)

            if numero_norm not in numero_map:
                numero_map[numero_norm] = []

            numero_map[numero_norm].append(j)

        # Para cada grupo, manter apenas o mais completo
        result = []
        for numero_norm, grupo in numero_map.items():
            if len(grupo) == 1:
                result.append(grupo[0])
            else:
                # Merge: pegar julgado mais completo
                merged = JulgadoValidator._merge_group(grupo)
                result.append(merged)

        return result

    @staticmethod
    def _merge_group(julgados: List[Julgado]) -> Julgado:
        """
        Unir grupo de julgados do mesmo processo.
        Manter a versão com mais campos preenchidos.

        Args:
            julgados: grupo de julgados do mesmo número

        Returns:
            Julgado unido com campos mais completos
        """
        # Contar campos preenchidos em cada um
        def count_filled(j: Julgado) -> int:
            filled = 0
            for attr in ["classe_processo", "numero_processo", "titulo", "resumo",
                        "relator", "data_julgamento", "ramo_direito", "legislacao"]:
                val = getattr(j, attr)
                if val and str(val).strip():
                    filled += 1
            return filled

        # Manter o com mais campos
        best = max(julgados, key=count_filled)

        # Completar com campos dos outros
        for j in julgados:
            if j == best:
                continue

            # Se best tem campo vazio, preencher com j se tiver
            for attr in ["relator", "data_julgamento", "legislacao", "ods_onu2030",
                        "ramo_direito", "observacao", "redator_acordao"]:
                best_val = getattr(best, attr)
                if not best_val or str(best_val).strip() == "":
                    j_val = getattr(j, attr)
                    if j_val and str(j_val).strip():
                        setattr(best, attr, j_val)

        return best


from typing import Optional
