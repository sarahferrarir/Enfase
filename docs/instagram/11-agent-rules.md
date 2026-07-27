# Regras para agentes

## Protocolo

Aplicável a Claude, Codex, Pencil e agentes semelhantes. Ordem: README; marca; formatos; tokens; tipografia; layout; conteúdo; template escolhido; componentes/imagens aplicáveis; checklist; workflow.

Contexto mínimo: objetivo, template, formato, conteúdo estruturado, assets com direitos, CTA/destino, fonte, status jurídico e versão. Sem isso, reportar campos ausentes.

Regras obrigatórias:

- usar uma instância do template existente; não redesenhar;
- não criar ou modificar componente, token, cor, fonte, margem, grid ou posição da logo;
- não alterar significado jurídico nem inventar informação;
- preservar o arquivo e proporção da logo;
- respeitar caixas e limites de linha;
- excesso: propor divisão fiel ou devolver; nunca comprimir;
- insuficiência: manter campo opcional vazio/oculto ou pedir dado obrigatório; nunca completar;
- marcar toda lacuna como `Decisão pendente` ou `Input ausente`;
- conflito layout/conteúdo: indicar campo, capacidade excedida e opções permitidas;
- não gerar arquivo final enquanto houver bloqueio.

Saída esperada:

```yaml
template: nome/versao
format: dimensoes
input_status: valid|blocked
slides:
  - number: 1
    fields: {}
assets: []
changes: []
pending_decisions: []
conflicts: []
qa: pass|fail
human_reviews_required: [visual, content, legal, rights]
exports: []
```

Pedir revisão humana para conteúdo jurídico, fonte/dado duvidoso, direitos, pessoa real, IA generativa, informação sensível, exceção de template, 7–10 slides, quadrado ou decisão pendente. Reprovar se houver mudança de sentido, invenção, token/fonte não oficial, logo alterada, conteúdo cortado, contraste abaixo do mínimo, asset sem direito, número/data divergente, slide errado ou exportação fora do padrão.

## Prompts-base

### 1. Criar componentes no Pencil

```text
Crie apenas os componentes listados em 07-components.md, usando nomes canônicos, tokens oficiais e propriedades editáveis declaradas. Não crie estilo, cor, fonte, raio, efeito ou componente adicional. Use dimensões aprovadas do template; se ainda forem Decisão pendente, pare e liste-as. Bloqueie logo, geometria, tokens e posições; exponha somente os campos permitidos. Entregue inventário de componentes, variantes e pendências para revisão humana.
```

### 2. Criar um template vazio

```text
Monte uma instância vazia do template oficial [NOME] no formato [FORMATO], somente com componentes existentes. Preserve grid, margens, tipografia, cores, área segura e posição da logo aprovados. Não desenhe conteúdo real e não crie variantes. Nomeie campos e slides, defina placeholders neutros e reporte qualquer medida ainda marcada Decisão pendente antes de finalizar.
```

### 3. Preencher um template existente

```text
Use o template existente [NOME/VERSÃO]. Não redesenhe. Não altere componentes. Não altere cores. Não altere fontes. Não altere margens. Não altere a posição da logo. Não altere o significado do conteúdo. Preencha somente os campos permitidos com o input fornecido, preserve números, datas, fontes e citações, e use somente assets autorizados. Sinalize quando o conteúdo não couber; não reduza fonte, espaçamento ou margens. Entregue mapa de campos, conflitos, pendências e resultado do checklist.
```

### 4. Corrigir apenas conteúdo

```text
Corrija somente os campos de conteúdo indicados em [LISTA], usando a versão aprovada fornecida. Não altere layout, componentes, estilos, quebras não solicitadas ou assets. Compare antes/depois, confirme preservação do significado jurídico e sinalize divergências que exigem revisão.
```

### 5. Corrigir apenas layout

```text
Corrija somente os desvios de layout listados em [ACHADOS], restaurando valores do template. Não mude palavras, pontuação, ordem jurídica, imagem/crop aprovado ou template. Se o conteúdo não couber após restaurar o layout, marque conflito e pare.
```

### 6. Revisar um post

```text
Audite [ARQUIVO/INSTÂNCIA] com 12-quality-checklist.md. Para cada requisito, reporte Atendido, Parcial, Não atendido ou N/A, evidência e severidade. Compare conteúdo com a fonte aprovada, verifique logo, contraste, margens, crop, CTA, números e exportação. Não corrija; entregue aprovação ou reprovação e bloqueios.
```

### 7. Exportar um carrossel

```text
Exporte somente a instância aprovada [ID/VERSÃO] na ordem correta. Use dimensões, sRGB, formato e nomenclatura de 03-formats.md. Não aplique mudanças visuais na exportação. Valide quantidade, sequência, pixels, extensão e nomes; gere manifesto de exports e pare se qualquer revisão estiver pendente.
```
