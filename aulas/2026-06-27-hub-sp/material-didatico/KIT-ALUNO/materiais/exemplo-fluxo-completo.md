# Exemplo — o fluxo completo das 4 skills em ação

> As 4 skills do kit, rodando em sequência no mesmo caso (análise de risco de
> crédito). Este é o caminho que você percorre no workshop com o SEU caso.

---

## Ponto de partida — o pedido cru

```
faça uma análise de risco de crédito
```
Telegráfico. Densidade ~1.5. O modelo vai chutar categorias, sem método.

---

## 1 · `/fi-forja "faça uma análise de risco de crédito"`

Nasce o Framework Injection canônico (FI-humano, rotulado):

```
[PAPEL] analista de risco de crédito sênior (metodologia de rating interno bancário)
[OBJETIVO] parecer de solvência que sustente decisão de concessão/recusa
[MÉTODO] 1. liquidez (current/quick ratio vs threshold)
         2. alavancagem (debt-to-equity, cobertura de juros)
         3. geração de caixa
         4. stress-test em 3 cenários (base/adverso/severo)
         5. rating consolidado por eixo
[CONTEXTO] decisão de comitê de crédito, empresa de médio porte
[FONTES] balanço auditado > não-auditado > benchmark setorial > estimativa
[OUTPUT] tabela por eixo (valor/threshold/veredito) + stress-test + rating + justificativa
[CONSTRAINTS] nunca recomendar sem os 5 eixos · nunca inventar número · sinalizar distress
[VERIFICAÇÃO] ASSERT ≥2 fontes citadas · CHECAGEM os 3 cenários foram cobertos?
[META-RACIOCÍNIO] suposição crítica · inferência vs dado · perguntar se faltar demonstrativo
```

---

## 2 · `/ds-meter` — mede e justifica

```
DS: 1.5 → 4.5  (+200%)   [número real do promptforge.py, verificado 2026-06-27]

POR QUÊ:
  ✓ "rating interno", "current/quick ratio", "cobertura de juros" — termos-âncora
    financeiros, dsd alta (ativam o frame bancário)
  ✓ "stress-test 3 cenários" — método numerável, não vago
  ✗ no cru: "faça", "análise", "risco" soltos — pidgin, dsd baixa

⚠ DS mede o que você DIZ (input), não garante o que a IA DEVOLVE.
```

---

## 3 · `/fi-enforce` — atravessa a ponte

```
ANÁLISE DA PONTE (bridge_width: 0.0 → 0.5)

"ASSERT ≥2 fontes citadas"  → PRIMING DISFARÇADO (diz ASSERT, nada reprova)
  → cmd: grep -cE "\[(auditado|benchmark|estimativa)\]" saida.md  ≥ 2  ✓ vira enforcement

"nunca recomende sem os 5 eixos"  → PRIMING DISFARÇADO
  → cmd: grep -qiE "liquidez" && ... && grep -qiE "rating"  ✓ vira enforcement

"os 3 cenários foram cobertos?"  → PRIMING (cognitivo, por design — fica CHECAGEM)
```

---

## 4 · `/fi-tempera` — ataca e fortalece

```
MARTELO (Auditor): 2 ataques
  • "'solvência' sem horizonte temporal — 12 meses? 5 anos?"
  • "ASSERT '≥2 fontes' não diz fontes de quê"
RECOZER: ambos sobrevivem ao contra-ataque → viram correção
RESFRIAR (Sentinela): 0 alucinações (o FI não inventou números)
Índice de Confiança: 1.0

Correções aplicadas:
  • [MÉTODO] → "solvência em horizonte de 12 meses"
  • [VERIFICAÇÃO] → "ASSERT ≥2 fontes rotuladas por tipo"
```

---

## O resultado

Você saiu de **"faça uma análise de risco"** (6 palavras, densidade 1.5, zero método,
zero verificação) para um **Framework Injection temperado**: método em 5 eixos,
hierarquia de fontes, 2 verificações que de fato obrigam, e zero alucinação.

Você não escreveu um prompt melhor. **Você codificou — e temperou — um método.**

> Os números (DS 1.5→4.5, bridge_width 0→0.5) são do seu próprio FI, medidos no
> momento. Não são comparações com nenhum "controle" — são o retrato do que você fez.
