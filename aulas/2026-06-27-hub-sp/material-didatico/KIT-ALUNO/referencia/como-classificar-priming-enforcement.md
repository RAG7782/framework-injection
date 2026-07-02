# Fonte canônica — Como classificar Priming vs Enforcement (sem achismo)

> **Função:** documento-fonte para as lâminas. Resolve o apontamento crítico de 2026-06-27: *"qual é o elemento técnico que identifica enforcement, sem depender de interpretação da pessoa?"*
> **Tese central (a que tira o achismo):** enforcement **não é uma propriedade da palavra** — é uma propriedade de **onde a regra é verificada**. Por isso a classificação tem dois níveis: a *pista* (sintática, lê-se no texto) e o *veredito* (ontológico, decide a verdade).
> **Lastro:** critério-mestre do `CONCEITO — Priming e Enforcement (método Feynman).md` + nota do `caso-trilho` ("o ASSERT é priming que escalou até virar enforcement"). `[AF]` a formalização em 2 níveis é minha, derivada desse material — marcada como tal.

---

## O problema que esta página resolve

Se eu peço *"escreva um prompt e diga o que induz e o que constrange"*, e a pessoa olha só o texto, ela vai achar que `"NUNCA recomende investimento"` é enforcement (parece uma ordem forte). **Está errado** — e esse erro é a porta do achismo. A aula precisa de um critério que uma máquina poderia aplicar.

---

## NÍVEL 1 — A PISTA (sintática · lê-se na superfície do texto)

Marcadores que sugerem que a cláusula **foi escrita com intenção de constranger**. São pistas, não veredito.

| Marcador no texto | Tende a... | Exemplo |
|---|---|---|
| Verbo imperativo de proibição/obrigação ("NUNCA", "SEMPRE", "deve") | parecer enforcement (mas geralmente é priming) | "NUNCA invente número" |
| Condição **binária e checável** ("contém X", "≥ 2 fontes", "tem a seção Y") | poder virar enforcement | "a saída contém [RATING]" |
| Comando executável explícito (`cmd:`, `test -f`, `grep -q`, `jq`, `pytest`) | **ser enforcement** (se o harness roda) | `cmd: grep -q "rating" saida.md` |
| Referência a artefato fora do modelo (arquivo, exit code, schema, lei, sensor) | **ser enforcement** | "exit code 0" · "valida contra o schema JSON" |
| Verbo cognitivo/de observação ("considere", "reflita", "avalie se") | **ser priming** | "avalie se cobriu os 3 cenários" |
| Densificação/enquadramento (papel, método, hierarquia de fontes) | **ser priming** | "[PAPEL] analista sênior que aplica rating interno" |

**Regra de leitura do Nível 1:** imperativo forte ≠ enforcement. O que aproxima do enforcement é a **condição ser binária E haver um artefato externo checável** — não o tom da frase.

---

## NÍVEL 2 — O VEREDITO (ontológico · decide a verdade)

Uma pergunta só, binária, auditável por máquina:

> ## **"Existe um mecanismo FORA do modelo que REPROVA a saída se a condição falhar?"**
> - **SIM** → ENFORCEMENT (o agente não pode desobedecer — o gate barra)
> - **NÃO** → PRIMING (o agente deveria, mas pode ignorar — nada barra)

Este é o critério-mestre. Ele **sobrepõe** o Nível 1: por mais imperativo que o texto pareça, se nada externo reprova, **é priming**.

---

## A MATRIZ (junta os dois níveis — é o que mata o achismo)

| A cláusula tem condição binária checável? | Existe verificador externo que reprova? | Classificação | Por quê |
|---|---|---|---|
| Não (é vaga/cognitiva) | — | **PRIMING** | nada a verificar; só induz |
| Sim | Não (é só uma frase no prompt) | **PRIMING disfarçado** | parece regra, mas nada barra — "priming que ainda não escalou" |
| Sim | Sim (`cmd:`/test/parser/schema) | **ENFORCEMENT** | a condição binária + o gate externo = constrange de fato |
| Sim, mas só o modelo se autoavalia | "verificador" é o próprio LLM | **PRIMING** (erro confiante!) | LLM julgando a si = priming fingindo enforcement; fonte do erro |

> **A linha 2 (PRIMING disfarçado) é o uau didático.** É onde a pessoa aprende que escreveu "enforcement" mas entregou priming — e como escalar: anexar um verificador externo. **`bridge_width` mede exatamente a fração de cláusulas que cruzaram da linha 2 para a linha 3.**

---

## O TESTE DE 3 PERGUNTAS (o que o aluno aplica na microaplicação — Feynman)

Para cada linha de um prompt, pergunte em ordem:

1. **"Tem uma condição que dá pra checar com sim/não?"** Não → PRIMING. Pare.
2. **"Quem checa é algo FORA do modelo?"** (um comando, um teste, um arquivo, uma lei) Não → PRIMING (disfarçado, se a condição era binária). Pare.
3. **"Se falhar, a resposta é REPROVADA?"** Sim → ENFORCEMENT.

Três perguntas binárias. Zero adjetivo. Zero interpretação. **Uma máquina poderia rodar isso** — é a prova de que não é achismo.

---

## ANALOGIA FEYNMAN (a âncora única — coerente com o metrô já existente)

- **Priming = a placa "PROIBIDO ENTRAR".** Forte, imperativa — mas é tinta na parede. Um teimoso passa. A placa não tem braços. (= imperativo no texto, sem gate)
- **Enforcement = a catraca.** Não importa o que diz a placa: sem bilhete, não gira. A catraca tem o braço físico que barra. (= condição binária + verificador externo que reprova)
- **PRIMING disfarçado = uma catraca de papelão.** Tem o formato de catraca, está escrito "catraca" — mas não trava ninguém. É o `"NUNCA faça X"` sem harness. **A aula ensina a trocar o papelão por aço** = anexar o `cmd:`.

> **A passagem priming→enforcement = trocar a placa pela catraca.** O `bridge_width` conta quantas placas viraram catracas de verdade.

---

## EXEMPLO COMPLETO (no caso-trilho de risco de crédito)

| Linha do FI | Tem condição binária? | Verificador externo? | Veredito |
|---|---|---|---|
| `[PAPEL] analista de risco sênior` | não | não | **PRIMING** (enquadra) |
| `NUNCA recomende sem os 5 eixos` | sim (5 eixos preenchidos?) | não, se só texto | **PRIMING disfarçado** |
| `a saída contém [RATING] e [STRESS-TEST]` | sim | não, se só texto | **PRIMING disfarçado** |
| `cmd: grep -q "rating" saida.md && grep -q "stress" saida.md` | sim | **sim** (grep reprova) | **ENFORCEMENT** ✓ |
| `CHECAGEM: os 3 cenários foram cobertos?` | não (cognitiva) | não (o modelo observa) | **PRIMING** (por design) |

**Leitura:** este FI tem 1 cláusula que cruzou a ponte (o `grep`) e 2 que *poderiam* cruzar (estão como "priming disfarçado" — basta anexar um teste). `bridge_width` ≈ asserts executáveis / total de verificação. **A microaplicação do Ciclo 1 é: pegar uma linha "priming disfarçado" e escalá-la para enforcement anexando o verificador.**

---

## CONSEQUÊNCIA PARA A AULA (corrige o furo do Ciclo 1)

O exercício do Ciclo 1 **não** pode ser "olhe o texto e diga o que induz/constrange" (reintroduz achismo). Tem que ser:

> **"Aplique o teste de 3 perguntas a cada linha. Ache a linha que VOCÊ ACHAVA que constrangia mas é priming disfarçado. Escale-a: anexe o verificador externo que falta."**

Isso transforma a classificação subjetiva em procedimento de 3 passos binários — e ensina o gesto central do FI (escalar priming a enforcement) na própria mão do aluno. **É o critério técnico, não-achístico, que você pediu.**
