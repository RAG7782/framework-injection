# Gabarito Lakatosiano — onde cada modalidade mora no seu FI

> **O que esta página resolve** (apontamento do peer-review 2026-06-27): o aluno entende a
> epistemologia lakatosiana (núcleo/cinturão/borda) E entende as 5 modalidades, mas **trava
> na hora de montar o prompt** — não sabe onde encaixar cada modalidade. Este gabarito é a
> ponte: transforma a teoria num **layout de FI**. A teoria vira design de interface.
>
> **Lastro:** estrutura lakatosiana do programa (núcleo duro / cinturão protetor / borda) +
> as 5 modalidades do FI. `[AF]` o mapeamento modalidade→zona é uma proposta didática derivada
> desse material — usar como andaime (Vygotsky), não como dogma. Ajuste ao seu domínio.

---

## A ideia em uma frase

**As 5 modalidades não têm o mesmo peso.** Umas são inegociáveis (se a IA violar, você joga a
resposta fora); outras protegem o núcleo mas podem ser ajustadas; outras são só experimento.
Lakatos dá o nome dessas 3 camadas. Este gabarito diz qual modalidade vai em qual camada.

---

## O gabarito (as 3 zonas × as 5 modalidades)

```
┌─────────────────────────────────────────────────────────────────────┐
│  NÚCLEO DURO  ·  inegociável  ·  violou → DESCARTA a resposta inteira │
│  ───────────────────────────────────────────────────────────────────│
│  • DECLARATIVA  → o que a IA PODE saber (ontologia, hierarquia de     │
│                   fontes). Fora disso = alucinação → descarte.        │
│  • ÉTICA        → o que a IA NUNCA faz (guardrails, compliance).      │
│                   Cruzou a cerca = descarte.                          │
│  ▸ tende a ENFORCEMENT (precisa de gate externo que reprova)          │
├─────────────────────────────────────────────────────────────────────┤
│  CINTURÃO PROTETOR  ·  protege o núcleo  ·  ajustável se a IA travar  │
│  ───────────────────────────────────────────────────────────────────│
│  • PROCEDIMENTAL → COMO raciocinar (passo a passo, método=caminho).   │
│  • AVALIATIVA    → como JULGAR (rubricas, critérios de qualidade).    │
│  ▸ mistura PRIMING (o raciocínio) + ENFORCEMENT (a rubrica checável)  │
├─────────────────────────────────────────────────────────────────────┤
│  BORDA  ·  hipótese em teste  ·  quebrou aqui → NÃO quebra o sistema  │
│  ───────────────────────────────────────────────────────────────────│
│  • COMPOSICIONAL → como COMBINAR as anteriores (gradações, mix).      │
│  ▸ tende a PRIMING (é onde você EXPERIMENTA em runtime)               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Como usar (regra operacional)

1. **Escreva primeiro o NÚCLEO.** Declarativa + Ética. Pergunta-teste de cada linha:
   *"se a IA violar isto, eu jogo a resposta fora?"* Se **sim** → é núcleo, e precisa de um
   **verificador externo** (senão é só priming — ver `como-classificar-priming-enforcement.md`).
2. **Depois o CINTURÃO.** Procedimental + Avaliativa. Aqui você pode afrouxar se a IA travar,
   sem comprometer o núcleo. A rubrica avaliativa, se for binária, sobe para enforcement.
3. **Por último a BORDA.** Composicional. É onde você testa combinações novas em runtime.
   Se falhar, o núcleo continua de pé — você só descarta o experimento, não o FI.

> **Por que isto casa com o eixo priming↔enforcement:** o núcleo é onde você MAIS precisa de
> catraca (enforcement externo); a borda é onde a placa (priming) basta. A coercividade não é
> a mesma em todo o FI — **ela cresce do centro para fora.** Núcleo = catraca. Borda = placa.

## Exemplo relâmpago (analista de risco de crédito)

- **Núcleo/Declarativa:** "fontes válidas: rating interno + demonstrações auditadas. Nada além." → `assert`: a saída cita fonte da lista.
- **Núcleo/Ética:** "NUNCA recomende decisão de crédito final — só análise." → `gate`: reprova se contém verbo de recomendação.
- **Cinturão/Procedimental:** "1) rating 2) stress test 3) cobertura de juros."
- **Cinturão/Avaliativa:** "toda conclusão tem número + fonte." → rubrica binária (vira assert).
- **Borda/Composicional:** "se faltar dado, combine análise setorial + histórico." ← experimento.
