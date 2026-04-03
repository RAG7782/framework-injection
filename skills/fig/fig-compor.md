# FIG Compor — Compositor de Framework Injections

Analisa duas ou mais Framework Injections e tenta compô-las em uma FI unificada, identificando sinergias, conflitos e interferências. Investiga o problema aberto de composição de frameworks.

## Argumento: $ARGUMENTS

Formato: `/fig-compor [FI-1] [FI-2]` ou `/fig-compor [caminho/para/fi-1.md] [caminho/para/fi-2.md]`

Se vazio: "Forneça duas Framework Injections que deseja compor (cole ou indique os arquivos)."

---

## EXECUÇÃO

### PASSO 1 — Análise individual

Para CADA FI, extraia:
- Identidade/persona
- Princípios inegociáveis
- Definições críticas
- Cercas e exclusões
- Protocolo de raciocínio
- Arquitetura de delivery

---

### PASSO 2 — Detecção de interferências

Compare bloco a bloco:

| Bloco | FI-1 | FI-2 | Relação |
|---|---|---|---|
| Identidade | [persona 1] | [persona 2] | Compatível / Conflitante / Complementar |
| Princípios | [lista] | [lista] | Compatível / Conflitante / Complementar |
| Definições | [termos] | [termos] | Compatível / Conflitante / Complementar |
| Cercas | [proibições] | [proibições] | Compatível / Conflitante / Complementar |
| Raciocínio | [protocolo] | [protocolo] | Compatível / Conflitante / Complementar |
| Delivery | [formato] | [formato] | Compatível / Conflitante / Complementar |

**Tipos de interferência:**

- **Conflito direto** — FI-1 diz "sempre faça X", FI-2 diz "nunca faça X"
- **Conflito de precedência** — ambas definem prioridades incompatíveis
- **Conflito de definição** — mesmo termo, definições diferentes
- **Conflito de delivery** — formatos de saída incompatíveis
- **Redundância** — ambas dizem a mesma coisa (custo de tokens sem ganho)
- **Sinergia** — uma FI complementa a outra sem conflito

---

### PASSO 3 — Estratégia de composição

Para cada conflito, proponha resolução:

| Conflito | Estratégia | Resultado |
|---|---|---|
| (descrição) | Priorizar FI-1 / Priorizar FI-2 / Fundir / Criar hierarquia / Separar por contexto | (como fica) |

Estratégias disponíveis:
1. **Priorizar** — uma FI prevalece sobre a outra naquele bloco
2. **Fundir** — combinar os dois blocos em um novo
3. **Hierarquizar** — criar regra de precedência ("em contexto X, usar FI-1; em contexto Y, usar FI-2")
4. **Separar** — manter como FIs independentes (composição não é viável nesse bloco)

---

### PASSO 4 — Gerar FI composta (se viável)

Se a composição é viável (maioria dos blocos compatíveis ou complementares):
- Gere a FI unificada
- Marque claramente quais blocos vieram de qual FI
- Submeta a `/tempera` (a composição pode ter introduzido novos conflitos)

Se a composição NÃO é viável:
- Documente por que não funciona
- Sugira alternativa (ex: usar em sequência, não simultaneamente)

---

### PASSO 5 — Relatório de composição

```
RELATÓRIO DE COMPOSIÇÃO
========================
FI-1: [nome]
FI-2: [nome]
Viabilidade: VIÁVEL / PARCIAL / INVIÁVEL

SINERGIAS: [X blocos complementares]
CONFLITOS: [Y blocos conflitantes]
REDUNDÂNCIAS: [Z blocos redundantes]

ESTRATÉGIA ADOTADA: [descrição]

FI COMPOSTA: [sim/não]
  Se sim: IC da composição: [valor]
  Se não: alternativa recomendada: [descrição]

ACHADO TEÓRICO:
  [O que essa composição revela sobre interferência entre frameworks — contribuição para o gap acadêmico]
```

---

## VALOR ACADÊMICO

Cada execução do `/fig-compor` gera dados para o problema aberto: "Quando múltiplos frameworks são injetados simultaneamente, eles compõem aditivamente ou interferem?" Documentar resultados sistematicamente contribui para o paper.
