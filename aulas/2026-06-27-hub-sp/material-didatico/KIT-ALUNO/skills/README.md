# Skills da Aula — Framework Injection (Academia Lendária)

As 4 skills que o aluno leva para casa. Uma para cada momento da forja.

| Skill | O que faz | Quando usar |
|---|---|---|
| **`/fi-forja`** | gera um Framework Injection canônico (8 seções + 7 instrumentos) a partir de um pedido cru | "transforma esse pedido em FI" |
| **`/ds-meter`** | mede a densidade semiótica (1.0–5.0) e **justifica** os critérios | "quão denso é esse prompt?" |
| **`/fi-enforce`** | acha onde o prompt só induz vs obriga, e cria os critérios externos que faltam | "como isso vira enforcement?" |
| **`/fi-tempera`** | ataca o FI para fortalecê-lo (forjar→martelar→recozer→resfriar) | "tempera e fortalece meu FI" |

## O fluxo da aula (as 4 se encadeiam)

```
1. /fi-forja "seu pedido cru"   → nasce o FI canônico
2. /ds-meter no cru e no FI     → vê a densidade subir (e por quê)
3. /fi-enforce no FI            → escala a [VERIFICAÇÃO] de priming p/ enforcement
4. /fi-tempera no FI            → ataca e fortalece (último passo, entregável)
```

São **independentes** (cada uma roda sozinha) mas **componíveis** (o output de uma
alimenta a próxima). O projeto do workshop é forjar o SEU FI passando pelas quatro.

## Instalação

Copie a pasta `aula/` para o diretório de skills do seu Claude:
- **Claude Code (terminal):** `~/.claude/skills/` ou `~/.aiox/skills/`
- Depois, invoque com `/fi-forja`, `/ds-meter`, `/fi-enforce`.

As skills funcionam **100% só com o agente** — zero instalação de Python, zero setup.

## Backend opcional (para quem tem Python)

Quem tiver o `promptforge.py` ganha o número exato e reproduzível da densidade:
`python promptforge.py --comparar "seu prompt"`. Sem isso, as skills estimam pelos
critérios explícitos (e mostram a régua). O método é o mesmo; o Python só fecha o número.

## Princípios (herdados do programa de pesquisa)

- **Atualizado por dentro, simples por fora** — usam o estado da arte (RFI = FI × DA,
  o eixo de coerção semântica, bridge_width rigoroso) sem despejar acrônimos no aluno.
- **Densidade ≠ eficácia** — a DS mede o que você diz, não garante o que a IA devolve.
- **Nunca cravar número não-verificado** — as skills dão o score do SEU prompt,
  medido agora; não inventam comparações "N× melhor".
- **Enforcement é onde se verifica, não a palavra** — uma ordem forte sem verificador
  externo é só priming disfarçado.

---
*Aula Framework Injection · Academia Lendária / Hub SP · v1.0.0 · Renato Aparecido Gomes*
