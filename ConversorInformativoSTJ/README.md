# ConversorInformativoSTJ

Ferramenta para converter documentos HTML de Informativos de Jurisprudência do Superior Tribunal de Justiça (STJ) em JSON estruturado e validado.

## Descrição

Este projeto automatiza a extração de dados jurídicos de informativos STJ usando um modelo de linguagem local (LLM). Cada julgado é processado individualmente, validado com Pydantic e consolidado em um arquivo JSON estruturado.

### Características

- ✅ Processamento local via Ollama (sem APIs externas)
- ✅ Validação rigorosa de dados com Pydantic
- ✅ Suporte a múltiplos informativos
- ✅ Preservação exata de texto jurídico
- ✅ Saída JSON formatada e estruturada
- ✅ Tratamento de erros robusto

## Requisitos

- **Python**: 3.10 ou superior
- **Ollama**: versão recente
- **Memória**: ~8GB RAM (para Llama 3.1:8b)
- **Armazenamento**: ~5GB para modelo

## Instalação

### 1. Clonar ou baixar o projeto

```bash
git clone <seu-repositorio>
cd ConversorInformativoSTJ
```

### 2. Criar ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# ou
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências Python

```bash
pip install -r requirements.txt
```

**Dependências:**
- `ollama` - Cliente para comunicação com Ollama
- `pydantic` - Validação de estrutura de dados
- `beautifulsoup4` - Parsing de HTML

### 4. Instalar Ollama

#### macOS
```bash
brew install ollama
```

#### Linux
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

#### Windows
Baixar em: https://ollama.ai/download

### 5. Download do modelo Llama 3.1:8b

Iniciar o serviço Ollama:

```bash
ollama serve
```

Em outro terminal, baixar o modelo:

```bash
ollama pull llama3.1:8b
```

Isso levará alguns minutos dependendo da velocidade da internet (~5GB).

Verificar que o modelo está disponível:

```bash
ollama list
```

Deverá mostrar `llama3.1:8b` na lista.

## Como usar

### Execução básica

```bash
python converter.py informativo_866.html
```

**Entrada:** Arquivo HTML do informativo (ex: `informativo_866.html`)  
**Saída:** Arquivo JSON (ex: `informativo_866.json`)

### Exemplo completo

```bash
# Processar um informativo
python converter.py exemplos/informativo_866.html

# Resultado esperado:
# Encontrados 17 julgados para processar.
# 
# Processando julgado 1/17...
# ✓ Julgado 1 processado com sucesso
# 
# [... mais julgados ...]
# 
# Total de julgados processados: 17
# ✓ JSON salvo em: exemplos/informativo_866.json
```

### Verificar saída

O arquivo JSON contém:

```json
{
  "numero_informativo": "886",
  "data_publicacao": "28 de abril de 2026",
  "julgados": [
    {
      "processo": "AgInt no REsp 2.221.968-PR",
      "ramo_direito": "DIREITO ADMINISTRATIVO",
      "tema": "...",
      "destaque": "...",
      "informacoes_inteiro_teor": "...",
      "relator": "Ministro Paulo Sérgio Domingues",
      "orgao_julgador": "Primeira Turma",
      "data_julgamento": "16/3/2026",
      "legislacao_aplicada": ["MP n. 513/2010"]
    }
  ]
}
```

## Estrutura de Saída JSON

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `numero_informativo` | string | Número do informativo (ex: "886") |
| `data_publicacao` | string | Data de publicação (ex: "28 de abril de 2026") |
| `julgados` | array | Lista de julgados processados |

### Campos de cada julgado

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `processo` | string | Identificação do processo judicial |
| `ramo_direito` | string | Área de direito aplicável |
| `tema` | string | Tema jurídico central |
| `destaque` | string | Resumo/destaque do julgado |
| `informacoes_inteiro_teor` | string | Informações completas do acórdão |
| `relator` | string | Nome do magistrado relator |
| `orgao_julgador` | string | Órgão que julgou (ex: "Primeira Turma") |
| `data_julgamento` | string | Data em que foi julgado |
| `legislacao_aplicada` | array[string] | Leis e artigos citados |

## Troubleshooting

### Erro: "Ollama service not running"

**Solução:**
```bash
# Terminal 1: Iniciar Ollama
ollama serve

# Terminal 2: Executar script
python converter.py seu_arquivo.html
```

### Erro: "nenhuma div com classe 'clsInformativoBlocoItem' encontrada"

**Possíveis causas:**
- Arquivo HTML não é um Informativo STJ válido
- Arquivo HTML corrompido
- Layout diferente (informativo mais antigo)

**Solução:**
- Verificar que o arquivo é um Informativo STJ oficial
- Tentar com os exemplos em `exemplos/` para validar setup
- Verificar se o HTML não foi alterado

### Erro: "validation error for JulgadoItem"

**Causa:** Ollama retornou JSON malformado

**Solução:**
- Verifique conexão com Ollama (`ollama serve` rodando)
- Reinicie o serviço Ollama
- Tente novamente

### Script rápido demais ou processamento lento

**Configurar temperatura do LLM** em `llm_processor.py`:
```python
# Aumentar temperatura para respostas mais variadas
options={"temperature": 0.3}  # padrão: 0
```

## Arquivos do Projeto

```
ConversorInformativoSTJ/
├── converter.py           # Script principal
├── html_parser.py         # Parsing de HTML
├── llm_processor.py       # Processamento com Ollama
├── models.py              # Validação Pydantic
├── requirements.txt       # Dependências Python
├── README.md              # Este arquivo
└── exemplos/              # Arquivos de exemplo
    ├── informativo_866.html
    ├── informativo_866.json
    ├── informativo_885.html
    └── informativo_885.json
```

## Desenvolvimento

### Estrutura de processamento

```
HTML input
    ↓
Ler com múltiplas codificações
    ↓
Parse com BeautifulSoup
    ↓
Validar estrutura HTML (div.clsInformativoBlocoItem)
    ↓
Extrair metadados (número, data)
    ↓
Para cada div.clsInformativoBlocoItem:
  - Limpar HTML → texto puro
  - Enviar para Ollama/Llama 3.1
  - Validar com Pydantic
  - Adicionar se válido
    ↓
Consolidar em InformativoResponse
    ↓
Salvar JSON formatado
```

### Executar com debug

```bash
# Ver entrada do LLM
# Descomente em html_parser.py, função clean_html_block()
print(cleaned_text[:500])
```

## Licença

MIT

## Suporte

Para problemas, consulte a seção Troubleshooting acima.
