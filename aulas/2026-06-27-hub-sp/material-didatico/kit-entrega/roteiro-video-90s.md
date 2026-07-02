# Roteiro — Vídeo 90s (demo A/B do Prompt-Forge)

> **Objetivo:** provar o salto cru→FI em 90 segundos, sem depender da demo ao vivo (que pode falhar). Serve de fallback no painel (Bloco 4) e de material de divulgação. **Tarefa-trilho:** análise de risco de crédito (o mesmo exemplo do analista, já ancorado no Bloco 2 — a plateia reconhece).

## Estrutura (90s, 5 cenas)

| Tempo | Cena | Tela | Narração (voz over) |
|---|---|---|---|
| 0–12s | **Gancho** | terminal limpo + a pergunta crua digitada | "Você pede assim pra IA: *'faça uma análise de risco de crédito da empresa X'*. E recebe… isto." |
| 12–32s | **Braço A (cru)** | resposta genérica rolando: categorias inventadas, sem método, sem hierarquia de fonte | "Categorias inventadas. Sem método. Sem hierarquia de fonte. Nenhuma verificação. É o pidgin: telegráfico, torcendo pra dar certo." |
| 32–42s | **A virada** | comando: `python promptforge.py --domain financeiro "análise de risco de crédito empresa X"` | "Agora não comando mais forte. Eu *disponho o método*. Passo o cru pelo Prompt-Forge." |
| 42–68s | **Braço B (FI)** | o FI denso aparecendo: `[PAPEL]` analista · `[MÉTODO]` liquidez/alavancagem/stress-test · `[FONTES]` hierarquia · `[VERIFICAÇÃO]` ASSERT | "Olha o que sai: papel, método de 6 cláusulas, hierarquia de fontes, e uma verificação que *obriga*. Isto é priming densificado — e o ASSERT é onde ele vira enforcement." |
| 68–90s | **O delta + fecho** | split-screen A vs B lado a lado; destaque no número da densidade | "Mesma pergunta. Mesmo modelo. O delta é visível e se mede. Você não comandou mais forte — você dispôs o método. **Isso é o Artesanato Digital.**" |

## Notas de produção
- **Tela:** screencast real do terminal (asciinema ou QuickTime). Fonte grande (≥18pt) — legível no projetor.
- **Ritmo:** corte seco entre A e B no segundo 32 — o contraste é o argumento.
- **Sem música** competindo com a narração; se houver, instrumental baixo.
- **Legenda queimada** (burn-in) recomendada — sala barulhenta / silenciosa indiferente.
- **Plano B do plano B:** se nem gravar der, o split-screen estático (print A | print B) já carrega 80% do impacto.
- **Honestidade (G4):** o "número da densidade" no fecho deve ser o real do Prompt-Forge naquele run — não inventar. Se não tiver número, mostre o delta de cláusulas (0 método → 6 cláusulas).
