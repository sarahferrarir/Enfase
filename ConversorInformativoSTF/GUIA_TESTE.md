# 🚀 PRÓXIMOS PASSOS - Teste e Validação

## ✅ O que foi implementado

### 1. **Reorganização do Projeto**
- ✅ Código antigo movido para `versionamento/old_converter/`
- ✅ Pasta `exemplos/` intocada e protegida
- ✅ Nova estrutura em `src/` criada

### 2. **Novos Módulos Implementados**

| Arquivo | Função | Status |
|---------|--------|--------|
| `src/schemas.py` | Modelos Pydantic para Julgado e Informativo | ✅ Completo |
| `src/document_reader.py` | Lê DOCX com mammoth | ✅ Completo |
| `src/text_preprocessor.py` | Limpeza básica de markdown | ✅ Completo |
| `src/chunker.py` | Divisão inteligente em chunks | ✅ Completo |
| `src/ollama_client.py` | Cliente centralizado do Ollama | ✅ Completo |
| `src/llm_processor.py` | Processamento via LLM com prompts | ✅ Completo |
| `src/validator.py` | Validação e deduplicação de julgados | ✅ Completo |
| `src/utils.py` | Funções utilitárias (ID, timestamp, etc) | ✅ Completo |
| `src/converter.py` | Orquestrador principal do pipeline | ✅ Completo |

### 3. **Dependências Atualizadas**
```
pydantic==2.6.4
mammoth==0.4.17
requests==2.31.0
ollama==0.1.31
```

---

## 📋 Como Testar

### **PREREQUISITO: Ollama Instalado**

```bash
# Instalar Ollama (se não tiver)
# https://ollama.ai

# Verificar instalação
ollama --version

# Iniciar servidor (TERMINAL DEDICADO)
ollama serve
```

### **PASSO 1: Instalar Dependências**

```bash
cd /Users/sarahferrarir/Enfase/ConversorInformativoSTF

# Criar virtual env (recomendado)
python3 -m venv venv
source venv/bin/activate

# Instalar requirements
pip install -r requirements.txt
```

### **PASSO 2: Baixar Modelo Ollama**

```bash
# Em OUTRO terminal (com Ollama rodando)
ollama pull qwen2.5:14b

# Ou modelo alternativo mais leve
ollama pull llama3.1:8b

# Verificar modelos instalados
ollama list
```

### **PASSO 3: Testar o Pipeline**

```bash
# Teste com Informativo1214.docx
python -m src.converter exemplos/Informativo1214.docx

# Ou com modelo alternativo
python -m src.converter exemplos/Informativo1214.docx --model llama3.1:8b

# Com mais debug
python -m src.converter exemplos/Informativo1214.docx -o resultado_teste.json
```

### **PASSO 4: Verificar Resultado**

```bash
# Ver arquivo gerado
ls -lh exemplos/Informativo1214.json

# Contar julgados
cat exemplos/Informativo1214.json | python -m json.tool | grep -c "numero_processo"

# Ver estrutura
cat exemplos/Informativo1214.json | python -m json.tool | head -50

# Ver um julgado completo
cat exemplos/Informativo1214.json | python -m json.tool | head -100
```

---

## 🔍 Entendendo o Pipeline

### **Fluxo de Execução**

```
1. converter.py main()
   ↓
2. read_docx() → markdown bruto
   ↓
3. clean_text() → remove lixo
   ↓
4. extract_metadata() → pega número/data informativo
   ↓
5. chunk_text() → divide em 3000 chars
   ↓
6. Para cada chunk:
   - llm_processor.process_chunk()
   - Envia para Ollama via ollama_client.py
   - Recebe JSON estruturado
   ↓
7. Para cada julgado extraído:
   - validator.is_valid() → verifica campos
   - convert_to_julgado() → Pydantic model
   ↓
8. validator.merge_julgados() → remove duplicatas
   ↓
9. Salva resultado.json
```

### **Principais Classes**

**OllamaClient** (src/ollama_client.py)
```python
client = OllamaClient(
    model="qwen2.5:14b",
    temperature=0.1,
    timeout=300,
)

response = client.generate(
    prompt="Seu prompt aqui",
    json_mode=True,
)
```

**LLMProcessor** (src/llm_processor.py)
```python
processor = LLMProcessor(client)

julgados = processor.process_chunk(text)
# Retorna lista de dicts com dados extraídos
```

**JulgadoValidator** (src/validator.py)
```python
is_valid, issues = validator.is_valid(julgado)
if not is_valid:
    print(f"Problemas: {issues}")
```

---

## ⚡ Customizações Possíveis

### **1. Alterar Modelo Ollama**

```bash
# Usar llama3.1 (mais rápido, menos memória)
python -m src.converter exemplos/Informativo1214.docx --model llama3.1:8b

# Ou outro modelo disponível
ollama pull mistral
python -m src.converter exemplos/Informativo1214.docx --model mistral
```

### **2. Aumentar Chunk Size (mais contexto)**

```bash
# Padrão: 3000 chars
# Aumentar para 5000 pode melhorar extração
python -m src.converter exemplos/Informativo1214.docx --chunk-size 5000
```

### **3. Aumentar Temperature (mais criativo)**

```bash
# Padrão: 0.1 (determinístico)
# Aumentar para 0.3 pode ajudar se tem poucos julgados
python -m src.converter exemplos/Informativo1214.docx --temperature 0.3

# Editar também em src/converter.py, linha que cria InformativoConverter
```

### **4. Customizar Prompt**

Editar `src/llm_processor.py`:
```python
JULGADO_EXTRACTION_PROMPT = """Seu novo prompt aqui...
```

---

## 🧪 Casos de Teste Esperados

### **Teste 1: Informativo1214.docx**
```bash
python -m src.converter exemplos/Informativo1214.docx

# Esperado:
# - ~24 julgados (comparar com versionamento/old_converter/)
# - JSON com campos: classe_processo, numero_processo, titulo, resumo
# - Nenhum erro de JSON inválido
```

### **Teste 2: Informativo1215.docx**
```bash
python -m src.converter exemplos/Informativo1215.docx

# Esperado:
# - Melhoria vs versão antiga (~4 → mais julgados)
# - Sem quebras por regex rígida
```

### **Teste 3: Informativo1216.docx**
```bash
python -m src.converter exemplos/Informativo1216.docx

# Esperado:
# - Melhoria vs versão antiga
# - Robustez a variações de estrutura
```

---

## 🐛 Debug se Algo Falhar

### **Problema: "Ollama não está disponível"**
```bash
# Terminal 1: iniciar servidor
ollama serve

# Terminal 2: verificar conexão
python -c "
from src.ollama_client import OllamaClient
c = OllamaClient()
print(c._health_check())  # Deve retornar True
"
```

### **Problema: "JSON inválido"**
```bash
# Teste o modelo diretamente
ollama run qwen2.5:14b '{"teste": "json"}'

# Se não retornar JSON puro, pode ser problema do modelo
# Tente llama3.1:8b que é mais confiável com JSON
```

### **Problema: Poucos julgados extraídos**
```bash
# 1. Aumentar chunk_size
python -m src.converter exemplos/Informativo1214.docx --chunk-size 5000

# 2. Aumentar temperature
# Editar src/converter.py, função main(), linha que cria InformativoConverter

# 3. Revisar prompt (editar JULGADO_EXTRACTION_PROMPT em src/llm_processor.py)
```

### **Problema: Processamento muito lento**
```bash
# Usar modelo mais leve
python -m src.converter exemplos/Informativo1214.docx --model llama3.1:8b

# Ou reduzir chunk_size
python -m src.converter exemplos/Informativo1214.docx --chunk-size 2000
```

---

## 📊 Métricas de Sucesso

✅ **Pipeline está funcionando quando:**

1. ✅ Ollama responde a prompts
2. ✅ Chunks são processados sem erro
3. ✅ JSON é gerado sem erro de validação
4. ✅ Pelo menos alguns julgados são extraídos
5. ✅ Campos obrigatórios (classe, número, título) não são nulos
6. ✅ Sem julgados duplicados
7. ✅ Output JSON é válido e parseable

---

## 🎯 Próximas Iterações (Opcionais)

1. **Fine-tuning do Prompt**
   - Adicionar exemplos ao prompt (few-shot learning)
   - Especificar melhor quais campos são críticos
   - Adicionar instruções contra alucinações

2. **Adicionar Logging**
   - Salvar chunks processados
   - Registrar quais campos falharam
   - Debug de LLM com prompts/respostas

3. **Caching**
   - Cache de chunks já processados
   - Evitar reprocessar mesmo arquivo

4. **Validações Avançadas**
   - Cross-check com numero_processo encontrado no texto
   - Validar formato de data
   - Validar UF contra lista de estados

5. **Integração com Banco de Dados**
   - Salvar diretamente em MongoDB/PostgreSQL
   - Evitar duplicatas globais

---

## 📞 Referências

- **Ollama**: https://ollama.ai
- **Pydantic**: https://docs.pydantic.dev/
- **Mammoth**: https://github.com/mwilliamson/python-mammoth
- **Documentação STF**: http://www.stf.jus.br

---

**Status:** ✅ Implementação completa. Pronto para testar!
