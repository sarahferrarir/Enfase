import re
from typing import List, Tuple
from .schemas import Julgado


class JulgadoValidator:
    """Valida e corrige julgados extraídos."""

    @staticmethod
    def cross_check_against_text(julgado: Julgado, original_text: str) -> List[str]:
        """
        Valida se os campos extraídos realmente aparecem no texto original.
        Previne hallucinations.

        Args:
            julgado: julgado a validar
            original_text: texto original do documento

        Returns:
            Lista de avisos (vazio se tudo ok)
        """
        warnings = []

        if not original_text:
            return warnings

        text_lower = original_text.lower()

        # Verificar número do processo
        if julgado.numero_processo:
            numero_clean = str(julgado.numero_processo).strip().lower()
            # Extrair cada número (separa por ";")
            numeros = [n.strip() for n in numero_clean.split(";")]
            for numero in numeros:
                # Remover "agr" (recurso de agravo) para busca
                numero_search = numero.replace("agr", "").strip()
                if numero_search and numero_search not in text_lower:
                    warnings.append(f"⚠️ Número não encontrado no texto: {numero}")

        # Verificar relator
        if julgado.relator:
            relator_lower = str(julgado.relator).lower()
            if relator_lower not in text_lower:
                warnings.append(f"⚠️ Relator não encontrado: {julgado.relator}")

        # Verificar data
        if julgado.data_julgamento:
            data_str = str(julgado.data_julgamento).replace("-", ".")
            if data_str not in text_lower and str(julgado.data_julgamento) not in text_lower:
                warnings.append(f"⚠️ Data não encontrada: {julgado.data_julgamento}")

        return warnings

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

        # Aceita múltiplas classes separadas por ";", mas rejeita outras separações
        if "/" in classe_str or ("," in classe_str and ";" not in classe_str):
            issues.append(f"❌ Classe inválida: {julgado.classe_processo}")
            return False, issues

        # Verifica se cada classe (separada por ";") é válida
        classes_parts = [c.strip() for c in classe_str.split(";")]
        for classe_part in classes_parts:
            if not any(cv in classe_part for cv in classes_validas):
                issues.append(f"❌ Classe desconhecida: {classe_part}")
                return False, issues

        # Validação 6: Número pode ser múltiplo (separado por ";"), mas não "e"
        numero_str = str(julgado.numero_processo).strip()
        # Rejeita "e" ou múltiplas vírgulas sem ";", mas aceita ";"
        if " e " in numero_str.lower() or (numero_str.count(",") > 1 and ";" not in numero_str):
            issues.append(f"❌ Número inválido (formato errado): {numero_str}")
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
            warnings = JulgadoValidator.cross_check_against_text(julgado, original_text)
            # Avisos não invalidam, apenas alertam
            if warnings:
                issues.extend(warnings)

        is_valid = len([i for i in issues if i.startswith("❌")]) == 0
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
        Detecta decisões conjuntas (mesmo resumo/título) e as combina com ";".

        Args:
            julgados: lista de julgados

        Returns:
            Lista sem duplicatas, com decisões conjuntas unidas
        """
        if not julgados:
            return []

        # Primeira passagem: agrupar por resumo+título (decisões conjuntas)
        resumo_map = {}  # (titulo_norm, resumo_norm) -> [julgados]

        for j in julgados:
            if not j.resumo or not j.titulo:
                continue

            titulo_norm = str(j.titulo).strip().lower()[:50]
            resumo_norm = str(j.resumo).strip().lower()[:100]
            key = (titulo_norm, resumo_norm)

            if key not in resumo_map:
                resumo_map[key] = []

            resumo_map[key].append(j)

        # Mergear decisões conjuntas
        merged_from_resumo = []
        for (titulo, resumo), grupo in resumo_map.items():
            if len(grupo) == 1:
                merged_from_resumo.append(grupo[0])
            else:
                # Decisão conjunta: combinar múltiplos processos em um
                merged = JulgadoValidator._merge_conjoint(grupo)
                merged_from_resumo.append(merged)

        # Segunda passagem: remover duplicatas por número
        numero_map = {}  # numero_normalizado -> [julgados]

        for j in merged_from_resumo:
            if not j.numero_processo:
                continue

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
    def _merge_conjoint(julgados: List[Julgado]) -> Julgado:
        """
        Combina múltiplos julgados da mesma decisão conjunta em um.
        Concatena números, classes, incidentes com ";".

        Args:
            julgados: grupo de julgados da mesma decisão

        Returns:
            Julgado unido com múltiplos números/classes
        """
        if not julgados:
            return None

        base = julgados[0]

        # Coletar todos os números e classes
        numeros = []
        classes = []
        incidentes = []
        ufs = []

        for j in julgados:
            if j.numero_processo and j.numero_processo not in numeros:
                numeros.append(j.numero_processo)
            if j.classe_processo and j.classe_processo not in classes:
                classes.append(j.classe_processo)
            if j.incidente_julgamento and j.incidente_julgamento not in incidentes:
                incidentes.append(j.incidente_julgamento)
            if j.uf and j.uf not in ufs:
                ufs.append(j.uf)

        # Criar julgado unido
        merged = base
        merged.numero_processo = ";".join(numeros) if numeros else base.numero_processo
        merged.classe_processo = ";".join(classes) if classes else base.classe_processo
        merged.incidente_julgamento = "; ".join(incidentes) if incidentes else base.incidente_julgamento
        merged.uf = ";".join(ufs) if ufs else base.uf

        return merged

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
