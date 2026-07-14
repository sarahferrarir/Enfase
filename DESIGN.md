---
version: "2.1"
status: "active"
name: "Ênfase Design System"
website: "https://cursoenfase.com.br/"
entrypoint: true
---

# Ênfase Design System

Este arquivo é o ponto de entrada do Design System do Ênfase. Ele resume as regras críticas e aponta para a documentação detalhada em [`docs/design/`](docs/design/).

Use este arquivo para decidir o que ler primeiro. Não trate este resumo como substituto dos documentos detalhados quando a tarefa envolver implementação, auditoria, conteúdo, negócio ou componentes compartilhados.

## Objetivo

Garantir que qualquer interface do Ênfase pareça pertencer ao mesmo ecossistema: clara, jurídica, editorial, responsiva, acessível, confiável e consistente.

O Design System cobre:

- landing pages, páginas institucionais e páginas de curso;
- blogs, artigos e documentação;
- dashboards, ferramentas, planners, trackers e portais;
- áreas internas, aplicações administrativas e sistemas web.

## Prioridade Das Fontes

Quando houver conflito, aplicar esta ordem:

1. dados oficiais e regras de negócio atuais;
2. código e tokens oficiais do projeto;
3. componentes e estilos oficiais do Figma;
4. documentação em [`docs/design/`](docs/design/);
5. este resumo;
6. inferência do agente, somente quando não houver fonte melhor.

## Regra De Linguagem

Use sempre **"o Ênfase"**. Não use artigo feminino para a marca.

## Regras Críticas

- Não inventar preços, descontos, datas, prazos, vagas, bônus, cashback, links, telefones, professores, credenciais, produtos, carreiras, depoimentos, aprovações, estatísticas, regras acadêmicas, FAQs ou imagens atribuídas a pessoas reais.
- Separar fato, inferência e dúvida.
- Marcar como `N/A` regras que não se aplicam ao tipo de interface.
- Não tratar ausência de hero, pricing, prova social ou footer comercial como erro em dashboards, ferramentas ou aplicações internas.
- Não criar identidade paralela para campanha, produto ou ferramenta.
- Reutilizar tokens e componentes antes de criar variações novas.
- Não alterar componentes compartilhados sem avaliar impacto.
- Não afirmar responsividade, fonte carregada ou acessibilidade visual sem evidência ou teste compatível.

## Princípios Essenciais

- Função antes da decoração.
- Hierarquia forte.
- Tipografia editorial com PT Serif para títulos e Montserrat para interface.
- Simplicidade operacional em ferramentas e dashboards.
- Consistência sobre novidade.
- Leitura como prioridade.
- Controles grandes, claros e acessíveis.

## Tokens Essenciais

Consulte os detalhes em [`03-tokens.md`](docs/design/03-tokens.md).

| Papel | Token | Valor |
| --- | --- | --- |
| Fundo | `background` | `#FFFFFF` |
| Texto principal | `ink` | `#160023` |
| Texto secundário | `muted` | `#675F78` |
| Ação principal | `primary` | `#FF2759` |
| Hover de ação | `primary-hover` | `#D6224C` |
| Roxo institucional | `purple` | `#200140` |
| Roxo escuro | `purple-dark` | `#170030` |
| Dourado | `gold` | `#D6B56D` |
| Linha | `line` | `#20014024` |
| Container | `layout.container` | `min(100% - 40px, 1200px)` |

## O Que Ler

- Marca ou direção visual: [`01-brand.md`](docs/design/01-brand.md) e [`02-principles.md`](docs/design/02-principles.md).
- Cores, espaçamento, bordas, sombras ou breakpoints: [`03-tokens.md`](docs/design/03-tokens.md).
- Fontes, hierarquia e escala: [`04-typography.md`](docs/design/04-typography.md).
- Container, grid, seções e fundos: [`05-layout.md`](docs/design/05-layout.md).
- Componentes, variantes e política de reutilização: [`06-components.md`](docs/design/06-components.md).
- Animações, estados e loading: [`07-motion.md`](docs/design/07-motion.md).
- Texto, CTAs, headings e SEO editorial: [`08-content.md`](docs/design/08-content.md).
- Semântica, ARIA, teclado, foco e contraste: [`09-accessibility.md`](docs/design/09-accessibility.md).
- Desktop, tablet e mobile: [`10-responsive.md`](docs/design/10-responsive.md).
- Templates por tipo de página: [`11-page-types.md`](docs/design/11-page-types.md).
- Dashboards, ferramentas e aplicações: [`12-application-pages.md`](docs/design/12-application-pages.md).
- Produtos, carreiras e restrições comerciais: [`13-business-rules.md`](docs/design/13-business-rules.md).
- Regras específicas para agentes de IA: [`14-agent-rules.md`](docs/design/14-agent-rules.md).
- Auditoria, severidade, evidência e score: [`15-audit.md`](docs/design/15-audit.md).
- Implementação, dados e ativos: [`16-implementation.md`](docs/design/16-implementation.md).
- Estado atual confirmado do site/código: [`17-current-implementation.md`](docs/design/17-current-implementation.md).
- Escolha de estrutura por contexto: [`18-decision-tree.md`](docs/design/18-decision-tree.md).

## Índice Completo

1. [Marca](docs/design/01-brand.md)
2. [Princípios](docs/design/02-principles.md)
3. [Tokens](docs/design/03-tokens.md)
4. [Tipografia](docs/design/04-typography.md)
5. [Layout](docs/design/05-layout.md)
6. [Componentes](docs/design/06-components.md)
7. [Motion](docs/design/07-motion.md)
8. [Conteúdo](docs/design/08-content.md)
9. [Acessibilidade](docs/design/09-accessibility.md)
10. [Responsividade](docs/design/10-responsive.md)
11. [Tipos de Página](docs/design/11-page-types.md)
12. [Application Pages](docs/design/12-application-pages.md)
13. [Business Rules](docs/design/13-business-rules.md)
14. [Agent Rules](docs/design/14-agent-rules.md)
15. [Auditoria](docs/design/15-audit.md)
16. [Implementação](docs/design/16-implementation.md)
17. [Implementação Atual](docs/design/17-current-implementation.md)
18. [Árvore de Decisão](docs/design/18-decision-tree.md)

## Checklist Mínimo Para Agentes

Antes de concluir qualquer trabalho:

- identificar tipo de interface, objetivo, público e ação principal;
- ler os arquivos detalhados aplicáveis;
- verificar dados de negócio antes de usar;
- reutilizar tokens e componentes existentes;
- avaliar regras aplicáveis e marcar exceções como `N/A`;
- validar semântica, foco, teclado, contraste e responsividade;
- listar arquivos afetados;
- separar fato, inferência e dúvida;
- não alterar código de projeto quando a tarefa for apenas documentação.
