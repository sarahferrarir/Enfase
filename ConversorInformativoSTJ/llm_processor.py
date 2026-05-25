import json
import ollama
from models import JulgadoItem

def check_ollama_connection() -> bool:
    """Verifica se serviço Ollama está disponível."""
    try:
        ollama.list()
        return True
    except Exception as e:
        raise ConnectionError(
            "Erro: Ollama não está rodando. "
            "Execute 'ollama serve' em outro terminal."
        )

def process_julgado_with_ollama(cleaned_text: str) -> str:
    """Envia texto limpo para Ollama e retorna resposta JSON."""

    prompt = f"""
Você é um extrator de dados jurídicos estruturados.

Extraia os dados do julgado abaixo em formato JSON.

REGRAS OBRIGATÓRIAS:
- Não resuma.
- Não explique.
- Não interprete.
- Não reescreva.
- Não corrija ortografia.
- Copie os campos textuais exatamente como aparecem no texto original.
- Se um campo não existir, retorne null.
- Retorne APENAS um JSON válido, sem explicações adicionais.

FORMATO ESPERADO:
{{
    "processo": string ou null,
    "ramo_direito": string ou null,
    "tema": string ou null,
    "destaque": string ou null,
    "informacoes_inteiro_teor": string ou null,
    "relator": string ou null,
    "orgao_julgador": string ou null,
    "data_julgamento": string ou null,
    "legislacao_aplicada": [lista de strings]
}}

TEXTO ORIGINAL:
{cleaned_text}
"""

    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "system",
                "content": "Você retorna apenas JSON válido seguindo exatamente o formato fornecido.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        options={"temperature": 0},
    )

    return response["message"]["content"]

def validate_julgado(llm_output: str) -> JulgadoItem | None:
    """Valida resposta do LLM com Pydantic. Retorna JulgadoItem ou None se inválido."""
    try:
        data = json.loads(llm_output)
        julgado = JulgadoItem(**data)
        return julgado
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Resposta recebida: {llm_output[:200]}")
        return None
    except ValueError as e:
        print(f"Erro ao validar dados com Pydantic: {e}")
        return None

def warn_if_field_not_in_source(julgado: JulgadoItem, cleaned_text: str) -> None:
    """Avisa se campos textuais gerados pelo LLM não aparecem no texto original."""
    campos_textuais = [
        "processo",
        "ramo_direito",
        "tema",
        "destaque",
        "informacoes_inteiro_teor",
        "relator",
        "orgao_julgador",
        "data_julgamento",
    ]

    for campo in campos_textuais:
        valor = getattr(julgado, campo)

        if valor and valor not in cleaned_text:
            print(f"Aviso: o campo '{campo}' não foi encontrado exatamente no texto original.")

def process_single_julgado(cleaned_text: str) -> JulgadoItem | None:
    """Processa um julgado individual: chama Ollama, valida resultado e verifica fidelidade textual."""
    try:
        check_ollama_connection()
        llm_output = process_julgado_with_ollama(cleaned_text)
        julgado = validate_julgado(llm_output)

        if julgado:
            warn_if_field_not_in_source(julgado, cleaned_text)

        return julgado

    except ConnectionError as e:
        print(f"Erro de conexão: {e}")
        return None
    except Exception as e:
        print(f"Erro ao processar julgado: {e}")
        return None