# Ficha de Governanca — Protocolo de Lapidacao Iterativa

## Ficha Tecnica

| Campo | Valor |
|---|---|
| **Nome** | Protocolo de Lapidacao Iterativa |
| **Versao** | 3.0 (17 operacoes + micro-consolidacao) |
| **Data de criacao** | 2026-04-03 |
| **Autor** | Renato Aparecido Gomes |
| **Gerada via** | FIG — Framework Injection Generator |
| **IC (Indice de Confianca)** | 0.91 |
| **Testes adversariais** | 11/11 (8 OK, 3 CONCERN mitigados) |
| **Skill path** | ~/.claude/commands/lapidacao.md |
| **Dominio** | Refinamento de outputs cognitivos |
| **Tipo FI** | Operacional-analitica |
| **Ecossistema** | Artesanato Digital |

## Anatomia do Protocolo

| Metrica | Valor |
|---|---|
| Operacoes core | 14 |
| Operacoes condicionais | 3 (OP15 Implementabilidade, OP16 Falsificabilidade, OP17 Precedentes) |
| Total de operacoes | 17 |
| Clusters | 4 (Mapeamento, Stress-Test, Analise Estrutural, Meta-Analise) |
| Micro-consolidacoes | 3 (entre clusters A-B, B-C, C-D) |
| Consolidacao final | 1 (ao fim de cada pass) |
| Passes maximos | 3 (Descoberta → Refinamento → Polimento) |
| Modos de execucao | 3 (auto, interativo, progressivo) |

## Limites Declarados

1. **Nao adequado para respostas triviais:** calculos, fatos, tarefas simples nao se beneficiam.
2. **Risco de over-engineering:** mitigado por convergencia honesta, anti-bloat e simplificacao ativa (OP8).
3. **Premissa de competencia:** assume que o usuario tem contexto para avaliar refinamentos.
4. **Contextos de urgencia:** usar --passes 1.
5. **Divergencia infinita:** empiricamente sempre ha mais — praticante decide quando parar.
6. **OP17 depende de web:** indisponivel em sessoes offline.

## Riscos

| Risco | Probabilidade | Impacto | Mitigacao |
|---|---|---|---|
| Over-engineering | Media | Medio | Anti-bloat + OP8 (Simplificacao) + convergencia honesta |
| Aceitacao acritica | Baixa | Alto | Gate de entrada por julgamento artesanal |
| Passes vazios | Baixa | Baixo | Regra inegociavel: declarar convergencia |
| Fadiga do praticante | Media | Medio | Modos interativo/progressivo + --passes N |
| Micro-consolidacao superficial | Media | Alto | Regra: micro-consolidacao produz versao, nao lista |
| Condicionais forcadas | Baixa | Medio | Regra: declarar "nao aplicavel" em vez de forcar |

## Protocolo de Revisao

- **Revisao de rotina:** A cada 6 meses, verificar se as 17 operacoes continuam produtivas.
- **Revisao por feedback:** Se praticantes reportarem operacoes consistentemente improdutivas, investigar.
- **Revisao por evolucao:** Se modelos de IA mudarem drasticamente, reavaliar a espiral.
- **Versionamento:** Mudanca estrutural (adicionar/remover operacao, mudar clusters) = nova versao + re-tempera.

## Quem Pode Modificar
- Autor original (Renato Aparecido Gomes)
- Praticantes avancados de AD, com justificativa documentada
- Qualquer modificacao deve passar por tempera (minimo 7 testes universais)

## Historico de Versoes

| Versao | Data | Mudanca |
|---|---|---|
| 1.0 | 2026-04-03 | Versao inicial: 7 operacoes, 3 passes |
| 2.0 | 2026-04-03 | Pos-tempera: gate de entrada, modo urgencia, convergencia |
| 3.0 | 2026-04-03 | 17 operacoes (14 core + 3 condicionais), 4 clusters, micro-consolidacao, principio do edificio |
