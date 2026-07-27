# Sistema Visual do Instagram do Ênfase

## Propósito e escopo

Esta pasta é a fonte de verdade autossuficiente para transformar conteúdo pronto em posts verticais, posts quadrados, carrosséis, stories e capas de reels do Ênfase. Ela orienta pessoas e agentes de IA, especialmente o Pencil, na composição, revisão e exportação; não autoriza reescrita jurídica, criação de fatos, campanhas ou identidade nova.

## Leitura obrigatória

Para qualquer peça: `01-brand.md`, `03-formats.md`, `04-tokens.md`, `05-typography.md`, `06-layout.md`, `09-content.md`, `10-templates.md`, `11-agent-rules.md` e `12-quality-checklist.md`. Para fotografia, leia também `08-images.md`; para criar ou alterar componentes, `07-components.md`; para operação completa, `13-workflow.md`.

Ordem recomendada: marca e objetivos; formatos, tokens, tipografia e layout; componentes e imagens; conteúdo e templates; regras de agentes, qualidade e fluxo.

## Como usar

Humanos devem entregar conteúdo no contrato de `09-content.md`, escolher um dos três templates oficiais e registrar aprovação. Agentes devem ler os arquivos obrigatórios, validar o input, reutilizar o template sem redesenho, preencher somente campos permitidos e produzir relatório de pendências e QA. Uma regra marcada **Decisão pendente** não pode ser completada por inferência.

## Arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| `01-brand.md` | Identidade, tom e logo |
| `02-objectives.md` | Objetivos, MVP e sucesso |
| `03-formats.md` | Pranchetas, corte e exportação |
| `04-tokens.md` | Cores, espaços e efeitos |
| `05-typography.md` | Famílias e hierarquia |
| `06-layout.md` | Grid e composição |
| `07-components.md` | Biblioteca reutilizável |
| `08-images.md` | Fotografia, ilustração e IA |
| `09-content.md` | Contrato e integridade do conteúdo |
| `10-templates.md` | Três templates oficiais |
| `11-agent-rules.md` | Restrições e prompts-base |
| `12-quality-checklist.md` | Critérios verificáveis de QA |
| `13-workflow.md` | Produção, aprovação e manutenção |

## Termos

- **Regra de marca:** princípio confirmado e invariável entre canais.
- **Regra de Instagram:** aplicação operacional definida nesta pasta.
- **Template:** composição oficial bloqueada, com campos editáveis.
- **Componente:** unidade nomeada e reutilizável do template.
- **Token:** valor visual nomeado; não é ajustado por publicação.
- **Campo:** conteúdo substituível sem alterar o componente.
- **Área segura:** região em que conteúdo crítico deve permanecer; seus valores ainda precisam de aprovação.
- **Conteúdo crítico:** logo, título, identificação, CTA, número, fonte ou informação cuja perda muda compreensão.
- **Decisão pendente:** dado não confirmado; requer validação humana antes de produção final.

O ativo oficial está em `assets/logo-enfase.avif`. É uma cópia sem modificação e é a única versão disponível neste sistema.
