# Documentação Do Design System

Esta pasta contém a documentação completa do Design System do Ênfase.

Cada arquivo possui uma responsabilidade específica. A divisão evita concentrar todo o sistema em um único documento muito grande e facilita a leitura por humanos e agentes de IA.

O [`../../DESIGN.md`](../../DESIGN.md) da raiz continua sendo o ponto de entrada principal do projeto.

## Estrutura Da Documentação

| Arquivo | Responsabilidade | Quando consultar |
| --- | --- | --- |
| [`01-brand.md`](01-brand.md) | Define marca, personalidade visual e direção de arte. | Ao decidir tom visual, imagens ou expressão institucional. |
| [`02-principles.md`](02-principles.md) | Registra os princípios gerais do sistema. | Ao tomar decisões de design ou resolver dúvidas de prioridade. |
| [`03-tokens.md`](03-tokens.md) | Documenta cores, espaçamentos, bordas, sombras e breakpoints. | Ao aplicar ou revisar valores visuais reutilizáveis. |
| [`04-typography.md`](04-typography.md) | Define famílias, hierarquia e regras tipográficas. | Ao criar títulos, textos, cards, tabelas ou interfaces editoriais. |
| [`05-layout.md`](05-layout.md) | Orienta container, grid, seções, fundos e fluxo visual. | Ao estruturar páginas, seções ou layouts responsivos. |
| [`06-components.md`](06-components.md) | Define componentes genéricos e política de reutilização. | Ao criar, alterar ou escolher componentes. |
| [`07-motion.md`](07-motion.md) | Documenta transições, loading, disabled e reduced motion. | Ao implementar estados animados ou interações. |
| [`08-content.md`](08-content.md) | Orienta tom, headings, CTAs, links, SEO e FAQ. | Ao escrever ou revisar conteúdo de interface. |
| [`09-accessibility.md`](09-accessibility.md) | Centraliza semântica, teclado, ARIA, foco e contraste. | Ao implementar ou auditar acessibilidade. |
| [`10-responsive.md`](10-responsive.md) | Define diretrizes para desktop, tablet e mobile. | Ao adaptar layouts e componentes entre viewports. |
| [`11-page-types.md`](11-page-types.md) | Descreve templates e orientações por tipo de página. | Ao criar páginas públicas, internas, editoriais ou comerciais. |
| [`12-application-pages.md`](12-application-pages.md) | Orienta ferramentas, dashboards, planners, trackers e apps. | Ao criar interfaces operacionais ou áreas internas. |
| [`13-business-rules.md`](13-business-rules.md) | Separa regras de negócio, produtos, carreiras e restrições. | Ao lidar com dados comerciais, acadêmicos ou institucionais. |
| [`14-agent-rules.md`](14-agent-rules.md) | Define regras específicas para agentes de IA. | Antes de agentes criarem, editarem ou auditarem interfaces. |
| [`15-audit.md`](15-audit.md) | Define método de auditoria, severidade, evidência e score. | Ao revisar conformidade com o Design System. |
| [`16-implementation.md`](16-implementation.md) | Orienta implementação, dados, ativos e componentes compartilhados. | Ao transformar o sistema em código ou organizar ativos. |
| [`17-current-implementation.md`](17-current-implementation.md) | Registra o estado atual consolidado da implementação. | Ao comparar o padrão desejado com o que existe hoje. |
| [`18-decision-tree.md`](18-decision-tree.md) | Ajuda a escolher estrutura, componentes e regras N/A. | Ao decidir arquitetura de página ou fluxo. |

## Ordem Recomendada De Leitura

Normalmente não é necessário ler todos os arquivos.

Para uma primeira leitura, comece por:

1. [`01-brand.md`](01-brand.md)
2. [`02-principles.md`](02-principles.md)
3. [`03-tokens.md`](03-tokens.md)
4. [`06-components.md`](06-components.md)

Depois, consulte apenas os documentos relacionados à tarefa.

## Qual Documento Devo Abrir?

### Quero criar uma nova página

1. [`11-page-types.md`](11-page-types.md)
2. [`06-components.md`](06-components.md)
3. [`03-tokens.md`](03-tokens.md)
4. [`05-layout.md`](05-layout.md)

### Quero criar uma ferramenta ou dashboard

1. [`12-application-pages.md`](12-application-pages.md)
2. [`06-components.md`](06-components.md)
3. [`05-layout.md`](05-layout.md)
4. [`10-responsive.md`](10-responsive.md)

### Quero auditar uma interface

1. [`15-audit.md`](15-audit.md)
2. [`14-agent-rules.md`](14-agent-rules.md)
3. [`03-tokens.md`](03-tokens.md)
4. [`06-components.md`](06-components.md)

### Quero alterar a identidade visual

1. [`01-brand.md`](01-brand.md)
2. [`02-principles.md`](02-principles.md)
3. [`03-tokens.md`](03-tokens.md)
4. [`04-typography.md`](04-typography.md)

### Quero alterar regras de negócio

1. [`13-business-rules.md`](13-business-rules.md)

### Quero entender como o site funciona hoje

1. [`17-current-implementation.md`](17-current-implementation.md)

### Quero implementar componentes

1. [`06-components.md`](06-components.md)
2. [`16-implementation.md`](16-implementation.md)

### Quero entender decisões de layout

1. [`05-layout.md`](05-layout.md)
2. [`18-decision-tree.md`](18-decision-tree.md)

## Relação Entre Os Documentos

```text
DESIGN.md
↓
docs/design/README.md
↓
arquivos numerados
```

- [`../../DESIGN.md`](../../DESIGN.md) é o ponto de entrada do projeto.
- Este README é o índice da documentação de design.
- Os arquivos numerados contêm os detalhes.

## Boas Práticas

- Consulte apenas os documentos necessários para a tarefa.
- Evite duplicar conteúdo entre arquivos.
- Mantenha responsabilidades separadas.
- Atualize a documentação quando novos componentes forem criados.
- Preserve a numeração para manter estabilidade de referências.
