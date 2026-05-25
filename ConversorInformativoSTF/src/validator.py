import re
from typing import List, Tuple
from .schemas import Julgado


class JulgadoValidator:
    """Valida e corrige julgados extraídos."""

    @staticmethod
    def is_valid(julgado: Julgado, original_text: Optional[str] = None) -> Tuple[bool, List[str]]:
        """
        Valida um julgado extraído.

        Args:
            julgado: instância de Julgado
            original_text: texto original (opcional, para validação cross-check)

        Returns:
            Tuple (is_valid: bool, issues: List[str])
        """
        issues = []

        # Validação 1: Precisa ter pelo menos classe ou número
        has_classe = julgado.classe_processo and str(julgado.classe_processo).strip()
        has_numero = julgado.numero_processo and str(julgado.numero_processo).strip()

        if not (has_classe or has_numero):
            issues.append("Falta classe_processo e numero_processo")

        # Validação 2: Se tem classe, deve ser válida
        if has_classe:
            classes_validas = [
                "ADI", "ADPF", "ADO", "ADC", "RE", "ARE",
                "HC", "MS", "Rcl", "RCL", "ACO"
            ]
            classe_str = str(julgado.classe_processo).strip().upper()
            if not any(c in classe_str for c in classes_validas):
                issues.append(f"Classe inválida: {julgado.classe_processo}")

        # Validação 3: Se tem resumo, não deve ser muito curto
        if julgado.resumo:
            if len(str(julgado.resumo).strip()) < 20:
                issues.append("Resumo muito curto")

        # Validação 4: Se tem título, não deve ser muito curto
        if julgado.titulo:
            if len(str(julgado.titulo).strip()) < 5:
                issues.append("Título muito curto")

        # Validação 5: Cross-check com texto original
        if original_text:
            if has_numero:
                numero_str = str(julgado.numero_processo).strip()
                if numero_str not in original_text:
                    issues.append(
                        f"Número não encontrado no texto original: {numero_str}"
                    )

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
        Remove duplicatas de julgados baseado em numero_processo.

        Args:
            julgados: lista de julgados

        Returns:
            Lista sem duplicatas
        """
        seen = set()
        result = []

        for j in julgados:
            if not j.numero_processo:
                result.append(j)
                continue

            numero = str(j.numero_processo).strip().upper()
            if numero not in seen:
                seen.add(numero)
                result.append(j)

        return result


from typing import Optional
