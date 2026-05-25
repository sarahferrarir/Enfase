# Conversor de Informativos STF com LLM/Ollama

Converte Informativos do Superior Tribunal Federal (STF) de DOCX para JSON estruturado usando **LLM via Ollama**.

## 🎯 Objetivo

Extrair julgados de informativos STF com **robustez semântica** em vez de regex rígida. A LLM identifica e extrai campos corretamente mesmo com variações na estrutura do documento.

## 🏗️ Arquitetura

```
src/
├── document_reader.py      # Lê DOCX com mammoth
├── text_preprocessor.py    # Limpeza básica de markdown
├── chunker.py              # Divide em chunks sem assumir limites
├── ollama_client.py        # Cliente centralizado do Ollama
├── llm_processor.py        # Envia chunks para LLM com prompts
├── validator.py            # Valida julgados extraídos
├── schemas.py              # Modelos Pydantic
├── utils.py                # Funções utilitárias
└── converter.py            # Orquestrador principal
```

## 📋 Pipeline

```
DOCX
  ↓
📖 DocumentReader (mammoth)
  ↓
Markdown
  ↓
🧹 TextPreprocessor (limpeza básica)
  ↓
Texto limpo
  ↓
✂️  Chunker (divisão inteligente)
  ↓
Chunks (3000 chars com overlap)
  ↓
🤖 LLMProcessor → Ollama
  ↓
JSON estruturado (classe, número, título, resumo, etc)
  ↓
✔️ Validator (validação + deduplicação)
  ↓
JSON final
```

## 🚀 Uso Rápido

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar Ollama

```bash
# Terminal 1: iniciar servidor Ollama
ollama serve

# Terminal 2: baixar modelo (primeira vez)
ollama pull qwen2.5:14b
# ou
ollama pull llama3.1:8b
```

### 3. Converter DOCX

```bash
python -m src.converter exemplos/Informativo1214.docx
```

**Opções:**

```bash
# Customizar modelo
python -m src.converter exemplos/Informativo1214.docx --model llama3.1:8b

# Especificar saída
python -m src.converter exemplos/Informativo1214.docx -o saida.json

# Customizar tamanho de chunks
python -m src.converter exemplos/Informativo1214.docx --chunk-size 5000

# Usar Ollama em outra máquina
python -m src.converter exemplos/Informativo1214.docx --url http://192.168.1.100:11434
```

## 📊 Resultado

O JSON gerado tem estrutura:

```json
{
  "julgado_stf": [
    {
      "id": "uuid",
      "created_at": "2026-05-25T13:15:30.123Z",
      "informativo": "1214",
      "classe_processo": "ADI",
      "numero_processo": "1234/SP",
      "titulo": "...",
      "resumo": "...",
      "relator": "...",
      "legislacao": "...",
      "ods_onu2030": "1, 2, 5",
      ...
    }
  ]
}
```

## 🔧 Configuração Detalhada

### Modelos Recomendados

| Modelo | Tamanho | RAM | Velocidade | Qualidade |
|--------|---------|-----|-----------|-----------|
| `qwen2.5:14b` | 8.9GB | 16GB | Média | ⭐⭐⭐⭐⭐ |
| `llama3.1:8b` | 4.7GB | 8GB | Rápido | ⭐⭐⭐⭐ |
| `llama2:7b` | 3.8GB | 8GB | Rápido | ⭐⭐⭐ |

**Recomendação:** `qwen2.5:14b` para melhor extração de campos judiciais.

### Parâmetros do Cliente Ollama

**Arquivo:** `src/ollama_client.py`

```python
OllamaClient(
    base_url="http://localhost:11434",
    model="qwen2.5:14b",
    temperature=0.1,          # 0=determinístico, 1=criativo
    timeout=300,              # segundos
    max_retries=3,
)
```

- `temperature=0.1`: Mantém respostas determinísticas e consistentes
- `timeout=300`: Aguarda até 5 minutos por chunk
- `max_retries=3`: Tenta 3 vezes se falhar

### Parâmetros do Chunker

**Arquivo:** `src/chunker.py`

```python
chunks = chunk_text(
    text,
    chunk_size=3000,    # caracteres
    overlap=300,        # sobreposição entre chunks
)
```

- **chunk_size**: Quanto maior, menos chunks (mais contexto para LLM)
- **overlap**: Évita perder julgados que ficam na fronteira entre chunks

## 🧪 Testando

### Teste com Exemplo

```bash
# Converter exemplo
python -m src.converter exemplos/Informativo1214.docx

# Verificar saída
cat exemplos/Informativo1214.json | jq '.julgado_stf | length'

# Ver primeiro julgado
cat exemplos/Informativo1214.json | jq '.julgado_stf[0]'
```

### Debug

```bash
# Ativar logs mais verbose
# (Adicione print statements onde necessário)

# Verificar resposta do Ollama manualmente
python -c "
from src.ollama_client import OllamaClient
client = OllamaClient()
response = client.generate('Olá, você está funcionando?')
print(response['text'])
"
```

## ⚠️ Troubleshooting

### Erro: "Ollama não está disponível"

```
RuntimeError: Ollama não está disponível em http://localhost:11434
Inicie com: ollama serve
```

**Solução:**
```bash
# Terminal separado
ollama serve

# Verificar se modelo está baixado
ollama list
```

### Erro: "Ollama não retornou JSON válido"

```
ValueError: Ollama não retornou JSON válido
```

**Causas:**
- Modelo não é adequado para estruturação JSON
- Temperature muito alta (use 0.1)
- Chunk muito grande (reduza para 2000)

**Solução:**
```bash
# Tente modelo diferente
python -m src.converter exemplos/Informativo1214.docx --model llama3.1:8b

# Ou reduza tamanho de chunk
python -m src.converter exemplos/Informativo1214.docx --chunk-size 2000
```

### Erro: "Timeout"

**Solução:**
```bash
# Aumente timeout (padrão 300s)
# Edite src/ollama_client.py, aumentar timeout do __init__

# Ou reduz chunk_size
python -m src.converter exemplos/Informativo1214.docx --chunk-size 1500
```

### Poucos julgados extraídos

**Causas:**
- Chunks muito pequenos (perdendo contexto)
- Temperature muito baixa (respostas muito genéricas)
- Prompt não está claro

**Soluções:**
1. Aumentar `chunk_size` de 3000 para 5000
2. Aumentar `temperature` de 0.1 para 0.3
3. Revisar prompt em `src/llm_processor.py` → `JULGADO_EXTRACTION_PROMPT`

## 📝 Estrutura Esperada do DOCX

O conversor funciona com informativos padrão STF:

```
Informativo nº 1214/2024

PLENÁRIO

DIREITO CONSTITUCIONAL – ADI 1234/SP
Breve descrição da matéria
Resumo: A decisão trata de...

DIREITO CIVIL – RE 5678/MG
...
```

**O que o conversor NÃO precisa:**
- ❌ Seções em negrito específicas
- ❌ Formatação exata
- ❌ Regex hardcoded
- ❌ Estrutura rígida

A LLM se adapta automaticamente! 🎯

## 🔄 Comparação: Antigo vs Novo

### Antigo (versionamento/old_converter/)

```
- Regex rígida para tudo
- Quebra com pequenas variações
- Difícil debugar (qual regex falhou?)
- Muitos false negatives
- Pouca flexibilidade
```

### Novo (src/)

```
✅ LLM entende semântica
✅ Robusto a variações
✅ Debug claro: "qual chunk falhou?"
✅ Menos false negatives
✅ Customizável por prompt
```

## 📦 Estrutura do Projeto

```
ConversorInformativoSTF/
├── exemplos/                    # ✅ Intocado
│   ├── Informativo1214.docx
│   ├── Informativo1215.docx
│   ├── Informativo1216.docx
│   ├── julgado-stf.json        # Referência de campo
│   ├── Informativo1214.json    # Saída esperada
│   └── ...
├── versionamento/
│   └── old_converter/           # Código antigo (referência)
│       ├── converter.py
│       ├── models.py
│       ├── llm_processor.py
│       └── ...
├── src/                         # ✨ Nova arquitetura
│   ├── __init__.py
│   ├── converter.py             # Orquestrador
│   ├── document_reader.py
│   ├── text_preprocessor.py
│   ├── chunker.py
│   ├── ollama_client.py
│   ├── llm_processor.py
│   ├── validator.py
│   ├── schemas.py
│   └── utils.py
├── requirements.txt
├── README.md
└── ANALISE_*.md                 # Documentação antiga
```

## 🎓 Próximos Passos

1. **Testar com diferentes modelos** — compare qwen vs llama
2. **Fine-tune do prompt** — customize `JULGADO_EXTRACTION_PROMPT` para seus dados
3. **Adicionar novos campos** — estenda `schemas.py` conforme necessário
4. **Validações customizadas** — adicione regras em `validator.py`
5. **Caching** — cache chunks já processados para otimizar

## 📧 Suporte

Se encontrar problemas:
1. Verifique logs (adicione `--verbose` se implementado)
2. Teste Ollama diretamente: `ollama run qwen2.5:14b "Olá"`
3. Revise o chunk problemático (veja output do conversor)
4. Consulte troubleshooting acima

---

**Desenvolvido com ❤️ para extração robusta de julgados STF**
