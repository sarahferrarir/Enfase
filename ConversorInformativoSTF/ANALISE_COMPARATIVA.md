# Análise Comparativa: JSON Atual vs JSON de Referência

## Resumo Executivo

O JSON gerado pelo projeto (`Informativo1214.json`) possui **4 julgados** com **25 campos**.
O JSON de referência (`julgado-stf.json`) possui **30 julgados** com **41 campos**.

### Diferença de Conteúdo
- Quantidade: 26 julgados a mais no referência
- Campos: 16 campos adicionais no referência

---

## 1. CAMPOS FALTANTES (16 campos)

### Críticos (devem ser preenchidos):
| Campo | Tipo | Descrição | Prioridade |
|-------|------|-----------|-----------|
| `id` | UUID | Identificador único do julgado | 🔴 ALTA |
| `created_at` | ISO DateTime | Timestamp de criação | 🔴 ALTA |
| `status` | String | Status da aprovação (ex: "APROVADO") | 🟠 MÉDIA |
| `type` | String | Tipo de julgado (ex: "STF") | 🟠 MÉDIA |
| `ramo_direito` | String | Deve incluir "DIREITO " prefix | 🟡 BAIXA |
| `ods_onu2030` | String | Formato com espaço: "1, 16" | 🟡 BAIXA |

### Campos Enriquecidos (agregam valor):
| Campo | Tipo | Descrição | Conteúdo |
|-------|------|-----------|----------|
| `classificacao` | JSON String | Tema, subtema, disciplina | Array com estrutura hierárquica |
| `questao` | JSON String | Pergunta de múltipla escolha com gabarito | Opcoes A-E, enunciado, letra_correta |
| `conteudo_fixacao` | HTML String | Pontos-chave da decisão | `<ul><li>...` com destaques |
| `comentario` | HTML String | Comentário extenso sobre a decisão | ~3.8K chars |
| `noticia_completa` | HTML String (atual: plain text) | Notícia completa com links | ~5.5K chars |
| `resumo` | HTML String (atual: plain text) | Resumo com formatação | Conversion necessária |
| `noticia` | HTML String (atual: null) | Notícia sintetizada | HTML com tags |

### Campos Adicionais de Metadados:
| Campo | Tipo | Valor Padrão |
|-------|------|-------------|
| `metadata` | JSON Object | `{}` (vazio) |
| `comments` | JSON Object | `{}` (vazio) |
| `new_classificacao` | JSON Object | `{}` (vazio) |
| `html` | String | `null` |
| `is_extraordinary` | Boolean | `false` |
| `grau_incidencia` | String | "PENDENTE" |
| `modified_by_users` | Array | `[]` (vazio) |
| `tema_julgado` | String | `null` |

---

## 2. CAMPOS QUE MUDAM DE FORMATO

### `ramo_direito`
- **Atual:** "CONSTITUCIONAL"
- **Referência:** "DIREITO CONSTITUCIONAL"
- **Ação:** Adicionar "DIREITO " como prefix se necessário

### `ods_onu2030`
- **Atual:** "5;10;16" (separado por ponto-e-vírgula)
- **Referência:** "1, 16" (separado por vírgula + espaço)
- **Ação:** Formatar com vírgula e espaço

### `resumo`, `noticia`, `noticia_completa`
- **Atual:** Plain text
- **Referência:** HTML com tags (`<p>`, `<strong>`, `<ul>`, `<li>`, etc)
- **Ação:** Wrappear conteúdo com tags HTML quando necessário

---

## 3. DADOS NOVOS A SEREM GERADOS

### ID e Timestamp
```json
{
  "id": "73ba1a09-993f-432f-ab5c-9fd229ed0d13",  // UUID v4
  "created_at": "2026-05-05T20:49:15.092Z"       // ISO 8601
}
```

### Classificação (Estrutura Hierárquica)
```json
{
  "tema": {
    "id": 41,
    "nome": "Direitos Sociais",
    "racional": "Discute-se a proteção do mínimo existencial..."
  },
  "subtema": {
    "id": 4408,
    "nome": "Mínimo Existencial e Reserva do Possível",
    "racional": "..."
  },
  "disciplina": {
    "id": 124,
    "nome": "Direito Constitucional",
    "racional": "..."
  }
}
```

---

## 4. ESTRATÉGIA DE IMPLEMENTAÇÃO

### Fase 1: Atualizar Models.py
- Adicionar novos campos ao Pydantic model `Julgado`
- Definir tipos corretos (str, dict, bool, list)
- Usar valores padrão para campos opcionais

### Fase 2: Estender llm_processor.py
- Manter extração atual de campos
- Adicionar novos extractors para:
  - `ramo_direito` com prefix "DIREITO "
  - `ods_onu2030` com formato correto
  - `noticia` e `comentario` (opcionais - podem permanecer null inicialmente)
  - `conteudo_fixacao` (gerar com destaques do resumo)
  - `classificacao` e `questao` (null inicialmente - AI pode enriquecer depois)

### Fase 3: Atualizar converter.py
- Gerar `id` (UUID v4) e `created_at` (timestamp ISO)
- Adicionar `status` = "APROVADO" por padrão
- Adicionar `type` = "STF"
- Adicionar outros campos com valores padrão

### Fase 4: Enriquecimento Futuro (fora do escopo)
- `classificacao`: Extrair via IA ou tabela de referência
- `questao`: Gerar via IA baseado no julgado
- `comentario`: Gerar ou extrair de fonte externa
- `conteudo_fixacao`: Extrair pontos-chave via IA

---

## 5. IMPACTO E PRIORIZAÇÕES

### Prioridade 1️⃣ (MUST HAVE)
- [x] `id` e `created_at`
- [x] `status` e `type`
- [x] Corrigir `ramo_direito` com prefix
- [x] Corrigir formato `ods_onu2030`

### Prioridade 2️⃣ (SHOULD HAVE)
- [x] Adicionar campos com valores default
- [x] Converter `resumo`, `noticia` para HTML

### Prioridade 3️⃣ (NICE TO HAVE)
- [ ] Gerar `conteudo_fixacao` automaticamente
- [ ] Gerar `classificacao` e `questao` (requer IA)
- [ ] Popular `comentario` (requer IA)

---

## 6. CHECKLIST DE ALTERAÇÕES

**Arquivos a modificar:**
- [ ] `models.py` - Estender Julgado com novos campos
- [ ] `llm_processor.py` - Adicionar extractors
- [ ] `converter.py` - Gerar ID, timestamps e campos padrão

**Testes:**
- [ ] Rodar conversão: `python converter.py exemplos/Informativo1214.docx`
- [ ] Validar novo JSON em `exemplos/Informativo1214.json`
- [ ] Verificar presença de todos os campos críticos

---

## 7. ROADMAP DE ENRIQUECIMENTO

Campos que podem ser preenchidos posteriormente via APIs ou IA:
1. `classificacao` - Usar taxonomia STF
2. `questao` - Gerar via LLM (Claude/GPT)
3. `comentario` - Sintetizar texto via LLM
4. `conteudo_fixacao` - Extrair tópicos via LLM
5. `modified_by_users` - Rastrear edições
6. `tema_julgado` - Classificar automaticamente
