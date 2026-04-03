# Protocolo de Lapidacao Iterativa

FI gerada via FIG em 2026-04-03. IC: 0.91. Versao 3.0.

## Arquitetura

```
CLUSTER A (Mapeamento)     → 4 ops → Micro-Consolidacao A
CLUSTER B (Stress-Test)    → 4 ops → Micro-Consolidacao B
CLUSTER C (Analise Estrut) → 3+1* ops → Micro-Consolidacao C
CLUSTER D (Meta-Analise)   → 3+2* ops → Consolidacao Final

* = operacoes condicionais
```

17 operacoes | 4 clusters | 3 micro-consolidacoes | ate 3 passes | 3 modos

## Artefatos

| Arquivo | Fase FIG | Conteudo |
|---|---|---|
| `perfil-cognitivo.md` | Fase 1 | Perfil do autor e contexto |
| `ontologia.md` | Fase 1 | Estrutura ontologica |
| `matriz-densidade.md` | Fase 2 | Termos densos + SDE |
| `fi-v1.md` | Fase 3 | FI pre-tempera (7 ops, historica) |
| `fi-v2-temperada.md` | Fase 4 | FI pos-tempera (17 ops, versao final) |
| `relatorio-tempera.md` | Fase 4 | 11 testes adversariais |
| `governanca.md` | Fase 6 | Ficha tecnica, limites, riscos |

## Skill Operacional

`~/.claude/commands/lapidacao.md` — invocar com `/lapidacao`

## Uso

```
/lapidacao                    → lapida ultima resposta (auto, 3 passes, 17 ops)
/lapidacao --interativo       → operacao por operacao
/lapidacao --progressivo      → pass por pass
/lapidacao --passes 1         → modo urgencia (1 pass)
/lapidacao --full             → ativa todas as condicionais
/lapidacao [texto]            → lapida texto especifico
```
