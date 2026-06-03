# 📚 ÍNDICE DE DOCUMENTAÇÃO - Conversor STF com LLM/Ollama

Guia completo de documentação do projeto. Comece por aqui! 👇

---

## 🎯 Para Quem Quer APENAS USAR

**Comece com:**
1. **README.md** — Como instalar, rodar, customizar
2. **GUIA_TESTE.md** — Passo a passo para testar

**Comando rápido:**
```bash
python -m src.converter exemplos/Informativo1214.docx
```

---

## 🔧 Para Quem Quer ENTENDER TUDO

**Leia nesta ordem:**
1. **ARQUITETURA_PIPELINE.md** ← **COMECE AQUI** 
   - Visão de alto nível
   - Cada arquivo explicado em detalhes
   - Fluxo completo passo a passo
   - **Contém o prompt COMPLETO**

2. **RESULTADOS_FINAIS.md**
   - Métricas de execução
   - Antes vs depois
   - Problemas corrigidos
   - Aprendizados

3. **README.md**
   - Referência rápida
   - Troubleshooting
   - Comparação de modelos

---

## 📋 LISTA DE DOCUMENTOS

### 1. **ARQUITETURA_PIPELINE.md** — Documento Principal
```
Seções:
├─ Visão Geral (fluxo em diagrama ASCII)
├─ Arquitetura de Alto Nível
├─ Estrutura de Arquivos Detalhada:
│  ├─ schemas.py (modelos Pydantic)
│  ├─ document_reader.py (lê DOCX)
│  ├─ text_preprocessor.py (limpeza)
│  ├─ chunker.py (divisão inteligente) ⭐ NOVO
│  ├─ ollama_client.py (cliente Ollama)
│  ├─ llm_processor.py (LLM com prompts) ⭐ COM PROMPT COMPLETO
│  ├─ validator.py (10 validações) ⭐ NOVO
│  ├─ utils.py (utilitários)
│  ├─ converter.py (orquestrador)
│  └─ schemas.py (modelos)
├─ Fluxo Completo Passo a Passo (com exemplos)
├─ Métricas de Execução (exemplo real)
├─ Decisões Arquiteturais Importantes
├─ Como Rodar
└─ Customização

🔑 LEIA ESTE DOCUMENTO PARA ENTENDER: Como funciona cada módulo, por quê cada decisão
```

### 2. **RESULTADOS_FINAIS.md** — Métricas e Comparação
```
Seções:
├─ Métricas de Execução (antes/depois)
├─ Comparação: Antes vs Depois (tabela)
├─ Análise das Mudanças (por componente)
├─ Exemplo de Julgado Melhorado
├─ Problemas Corrigidos (com detalhes)
├─ Lista de 10 Validações
├─ Detalhamento do Pipeline Revisado
├─ Aprendizados
└─ Próximos Passos

🔑 LEIA ESTE DOCUMENTO PARA ENTENDER: O quê mudou, por quê melhorou, métricas finais
```

### 3. **README.md** — Guia de Uso Prático
```
Seções:
├─ Objetivo
├─ Arquitetura (resumida)
├─ Pipeline (diagrama)
├─ Uso Rápido
├─ Resultado (formato JSON)
├─ Configuração Detalhada
├─ Testando
├─ Debug / Troubleshooting
├─ Comparação: Antigo vs Novo
├─ Estrutura do Projeto
├─ Próximos Passos
└─ Referências

🔑 LEIA ESTE DOCUMENTO PARA: Usar o pipeline, customizar, resolver problemas
```

### 4. **GUIA_TESTE.md** — Instruções Passo a Passo
```
Seções:
├─ O Que Foi Implementado (checklist)
├─ Como Testar (4 passos)
├─ Entendendo o Pipeline (fluxo de execução)
├─ Customizações Possíveis
├─ Casos de Teste Esperados
├─ Debug se Algo Falhar
├─ Métricas de Sucesso
└─ Referências

🔑 LEIA ESTE DOCUMENTO PARA: Fazer funcionar pela primeira vez, testar tudo
```

### 5. **RESUMO_IMPLEMENTACAO.md** — Visão Geral Rápida
```
Seções:
├─ Status Geral
├─ O Que Foi Criado (10 módulos)
├─ Dependências
├─ Como Rodar (resumido)
├─ Customizações
├─ Possíveis Ajustes
├─ Comparação Antigo vs Novo
└─ Documentação Disponível

🔑 LEIA ESTE DOCUMENTO PARA: Visão geral rápida, status do projeto
```

---

## 🎓 Roteiros de Leitura

### Roteiro 1: "Quero Usar Agora"
```
1. README.md (Uso Rápido section)
2. GUIA_TESTE.md (PASSO 1-4)
3. Execute: python -m src.converter exemplos/Informativo1214.docx
4. Pronto!
```
**Tempo:** ~15 minutos

### Roteiro 2: "Quero Entender o Sistema"
```
1. ARQUITETURA_PIPELINE.md (Visão Geral)
2. ARQUITETURA_PIPELINE.md (Estrutura de Arquivos - todo)
3. ARQUITETURA_PIPELINE.md (Fluxo Completo)
4. RESULTADOS_FINAIS.md (Problemas Corrigidos)
5. Código: src/llm_processor.py, src/validator.py
```
**Tempo:** ~1-2 horas

### Roteiro 3: "Quero Debugar um Problema"
```
1. README.md (Troubleshooting)
2. GUIA_TESTE.md (Debug se Algo Falhar)
3. ARQUITETURA_PIPELINE.md (Fluxo Completo)
4. Código: src/converter.py (logging statements)
```
**Tempo:** ~30 minutos

### Roteiro 4: "Quero Customizar o Prompt"
```
1. ARQUITETURA_PIPELINE.md (seção llm_processor.py)
2. Código: src/llm_processor.py (SYSTEM_PROMPT, JULGADO_EXTRACTION_PROMPT)
3. Teste: python -m src.converter exemplos/Informativo1214.docx
4. Refine: repita até funcionar
```
**Tempo:** ~1-3 horas (iterativo)

---

## 🔑 Documentos Chave por Tópico

### "Qual é o pipeline?"
→ ARQUITETURA_PIPELINE.md → "Arquitetura de Alto Nível" + "Fluxo Completo Passo a Passo"

### "Como cada arquivo funciona?"
→ ARQUITETURA_PIPELINE.md → "Estrutura de Arquivos e Responsabilidades"

### "Qual é o prompt da LLM?"
→ ARQUITETURA_PIPELINE.md → seção "llm_processor.py" → "System Prompt" + "Julgado Extraction Prompt"

### "Como customizar?"
→ README.md → "Configuração Detalhada"

### "Como testar?"
→ GUIA_TESTE.md → "Como Testar"

### "O que mudou?"
→ RESULTADOS_FINAIS.md → "Análise das Mudanças"

### "Como rodar?"
→ README.md → "Uso Rápido"

### "Está dando erro, como debugar?"
→ README.md → "Troubleshooting"
→ GUIA_TESTE.md → "Debug se Algo Falhar"

---

## 📊 Estrutura de Documentos

```
Documentação/
├─ README.md                      ← Ponto de entrada (referência prática)
├─ GUIA_TESTE.md                  ← Passo a passo para testar
├─ ARQUITETURA_PIPELINE.md        ← Explicação técnica COMPLETA
├─ RESULTADOS_FINAIS.md           ← Métricas e aprendizados
├─ RESUMO_IMPLEMENTACAO.md        ← Visão geral rápida
└─ Este Arquivo (DOCUMENTACAO.md) ← Índice e roteiros
```

**Total: ~9000 linhas de documentação**

---

## 🎯 Informações Mais Importantes

### Prompt Completo para LLM

**System Prompt:**
```
Você é um especialista em jurisprudência do STF.
Tarefa: Identificar e extrair APENAS julgados principais.

REGRAS:
1. Retorne APENAS JSON válido
2. Julgado PRINCIPAL tem: classe + número + título + resumo
3. Dados INCOMPLETOS não retorne
4. Se número aparece DENTRO outro resumo, NÃO extraia
5. Se "resumo" é apenas "[Rcl 77.893...]", NÃO é julgado
6. Preserve texto, não resuma
```

**User Prompt (Extraction):**
```
Analise texto e identifique APENAS julgados PRINCIPAIS.

OBRIGATÓRIOS:
✓ classe_processo (ADI, RE, Rcl, etc)
✓ numero_processo (único, não múltiplo)
✓ titulo (substantivo, não vazio)
✓ resumo (50+ chars, não [referência])

OPCIONAIS:
- uf, ramo_direito, materia, relator, legislacao, ods_onu2030, data_julgamento

Retorne JSON com estrutura { "julgados": [...] }
```

### 10 Validações Rigorosas

1. ✅ Tem classe_processo?
2. ✅ Tem numero_processo?
3. ✅ Tem titulo?
4. ✅ Tem resumo?
5. ✅ Classe é válida?
6. ✅ Classe é única (não múltipla)?
7. ✅ Número é único (não múltiplo)?
8. ✅ Resumo NÃO é [referência]?
9. ✅ Resumo > 50 caracteres?
10. ✅ Título > 10 caracteres?

### Modelos Recomendados

| Modelo | RAM | Velocidade | Qualidade JSON | Recomendação |
|--------|-----|-----------|----------------|----------|
| qwen2.5:14b | 16GB | Médio | ⭐⭐⭐⭐⭐ | **MELHOR** |
| llama3.1:8b | 8GB | Rápido | ⭐⭐⭐⭐ | Bom |
| llama2:7b | 8GB | Rápido | ⭐⭐⭐ | Básico |

### Métricas Finais

```
Entrada:   Informativo1214.docx
Chunks:    18
Extraídos: 28
Válidos:   25 (89%)
Finais:    22 (após merge)
Taxa:      +92% melhor que v1
```

---

## 🚀 Quick Start

```bash
# 1. Ollama
ollama serve

# 2. Modelo
ollama pull qwen2.5:14b

# 3. Ativar env
source .venv/bin/activate

# 4. Rodar
python -m src.converter exemplos/Informativo1214.docx

# 5. Resultado
cat exemplos/Informativo1214.json | jq .
```

---

## ❓ FAQ Rápido

**P: Por quê validação rigorosa?**  
R: Para garantir qualidade. Sem validação: julgados incompletos passam.

**P: Por quê detectar headers?**  
R: Tamanho fixo quebra julgados no meio. Headers preservam contexto.

**P: Por quê 4 campos obrigatórios?**  
R: classe + número + título + resumo = julgado legítimo. Sem um desses: incompleto.

**P: Por quê temperature 0.1?**  
R: Dados precisam de consistência, não criatividade. 0.1 = quase determinístico.

**P: Como customizar o prompt?**  
R: Edit `src/llm_processor.py` → JULGADO_EXTRACTION_PROMPT, re-run.

**P: Quantos julgados esperar?**  
R: ~20-30 por informativo (vs ~2-10 na versão anterior).

---

## 📞 Referências

- [Ollama](https://ollama.ai)
- [Pydantic](https://docs.pydantic.dev/)
- [Mammoth](https://github.com/mwilliamson/python-mammoth)
- [STF](http://www.stf.jus.br)

---

**Versão:** 2.0 Final  
**Data:** 2026-05-25  
**Status:** Pronto para produção ✅
