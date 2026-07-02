# Lâmina(s) — O GREP como a ponte técnica (priming → enforcement)

> **Onde entra:** deck único, Bloco B/C, logo após "O eixo: priming → enforcement"
> (a navalha "pode desobedecer?") e ANTES / DENTRO do Ciclo 1 (microaplicação:
> ache o priming disfarçado e anexe o verificador). É a aterrissagem concreta do
> critério não-achístico.
> **Contexto do eixo:** o eixo priming↔enforcement é o **Semantic Coercion Axis
> (SCA)** — coerção semântica (nome de Goldberg: a construção *coage* o sentido).
> Vetor **P2E** = priming→enforcement (a travessia que o GREP materializa).
> **Fonte:** transcrição da explicação de GREP (sessão 2026-06-27) + FONTE-classificacao.
> **✅ DECISÃO (2026-06-27): VERSÃO A — 2 lâminas** ("Acreditar ou provar?" +
> "O grep é a tranca do portão"). A Versão B (1 lâmina) abaixo fica como registro,
> NÃO usar. Ao montar o deck, incorporar A1 + A2 no Bloco B/C, junto do Ciclo 1.

---

# VERSÃO A — 2 lâminas (recomendada)

## ━━━ LÂMINA A1 — "Acreditar vs. provar" ━━━

**Título:** `Acreditar ou provar?` (h2, brush)

**Kicker:** a ponte, na prática

**Corpo:**

> As duas frases **querem dizer a mesma coisa.** A diferença não está no conteúdo —
> está em **quem decide se foi cumprido.**

Bloco comparativo (componente `crufi`, lado a lado):

```
┌─ PROSA (priming disfarçado) ──────────┐   ┌─ EXECUÇÃO (enforcement) ──────────────┐
│ "a saída contém [RATING]               │   │ grep -q "rating" saida.md             │
│  e [STRESS-TEST]"                      │   │                                       │
│                                        │   │                                       │
│ Quem julga? O próprio modelo.          │   │ Quem julga? O grep — um processo      │
│ Ele lê, olha o que produziu, e         │   │ externo, determinístico, sem          │
│ "acha que cumpriu".                    │   │ interesse em agradar.                 │
│                                        │   │                                       │
│ Réu e juiz na mesma cabeça.            │   │ Um terceiro atesta por você.          │
└────────────────────────────────────────┘   └────────────────────────────────────────┘
```

**Fecho (destaque):**
> *"a saída contém [RATING]"* é uma **afirmação a ser acreditada.**
> `grep -q "rating"` é um **teste a ser executado.**
> Mesma intenção. Uma é **confiança**; a outra é **prova.**

**Rodapé (fonte):** É a distinção do critério não-achístico: a frase tem a forma de
condição binária ("contém ou não?"), mas sem verificador externo ela só *enquadra* o
comportamento — não o garante. Um modelo apressado escreve "o rating ficou implícito"
e se convence de que passou.

**Nota do facilitador (aside):** Este é o slide que dissolve o achismo. A plateia
sente a diferença na pele: todo mundo já "achou que cumpriu" uma tarefa. O modelo faz
igual — a menos que algo fora dele cheque.

---

## ━━━ LÂMINA A2 — "Como o grep vira a tranca" ━━━

**Título:** `O grep é a tranca do portão` (h2)

**Kicker:** de buscar a validar

**Corpo:**

GREP = **G**lobal **R**egular **E**xpression **P**rint — varre todas as linhas, casa
um padrão, imprime as que batem. O que o torna um *verificador* (e não só um
buscador) é o **exit code** — o número que todo programa devolve ao terminar:

Tabela (3 linhas, estilo `anatomia`):
```
exit 0   → sucesso: achou pelo menos uma linha     (binário o bastante para virar assert)
exit 1   → falha:   não achou nada
exit 2   → erro:    arquivo não existe / regex inválida
```

**A flag que faz a virada:**
> `-q` (quiet) = o botão que troca o grep de **buscador** para **validador.**
> Sem `-q`: imprime as linhas (para humano ler). Com `-q`: não imprime nada, só
> devolve o veredito 0/1 (para máquina decidir).

**O assert completo** (bloco `mono`):
```
grep -q "rating" saida.md && grep -q "stress" saida.md
```
Lido em voz alta: *"Achou rating? Sim → cheque stress. Achou? Sim → sucesso."*
O `&&` = E lógico: se **qualquer** um falhar, a cadeia inteira falha. É a condição
*"contém [RATING] E [STRESS-TEST]"* — agora **executável**, não interpretável.

**Fecho (a ponte, com seta vertical):**
```
INTENÇÃO   "a saída deveria ter rating e stress"
   │   (prosa — o modelo se auto-avalia → PRIMING)
   ▼
PONTE      grep -q "rating" && grep -q "stress"
   │   (shell — um terceiro avalia → exit 0/1)
   ▼
PROVA      PASS (0)  |  FAIL (1)
```

**Rodapé (a microaplicação — amarra com o Ciclo 1):**
> Para escalar uma linha de "priming disfarçado" a enforcement você **não muda a
> intenção — anexa o verificador.** A frase já tem a condição binária; falta-lhe a
> ponte. Acopla um `grep -q` e ela cruza. O `bridge_width` sobe porque mais uma
> cláusula deixou de **pedir confiança** e passou a **produzir prova.**

---

# VERSÃO B — 1 lâmina condensada (se preferir economia)

## ━━━ LÂMINA ÚNICA — "Acreditar vs. provar: o grep" ━━━

**Título:** `Acreditar ou provar?` (h2, brush)

**Corpo (topo — a distinção):**
> As duas frases querem dizer o mesmo. A diferença é **quem decide se foi cumprido.**

Comparativo lado a lado (`crufi`):
```
PROSA  "a saída contém [RATING]"        →  quem julga? o MODELO (réu e juiz)  →  PRIMING
SHELL  grep -q "rating" saida.md        →  quem julga? o GREP (terceiro externo) →  ENFORCEMENT
```

**Meio (o mecanismo, 1 linha):**
> `grep -q` devolve **exit 0** (achou) ou **1** (não achou) — um veredito binário que
> uma máquina lê. A flag `-q` troca o grep de *buscador* para *validador*. O `&&`
> encadeia: `grep -q "rating" && grep -q "stress"` = *"contém os dois, ou reprova"*.

**Fecho (destaque):**
> *"a saída contém X"* = afirmação a ser **acreditada** (o modelo se auto-atesta).
> `grep -q X` = teste a ser **executado** (um terceiro atesta). Confiança vs. prova.
>
> Escalar priming→enforcement: **não mude a intenção — anexe o verificador.**

**Rodapé:** O grep é a ponte técnica: converte uma afirmação *sobre texto* ("deveria
conter X") num veredito *sobre bytes* ("contém X: sim/não"). É o coração do
`bridge_width`.

---

# NOTA DE PRECISÃO (para o facilitador — G6)
- A definição de grep, exit codes, `-q` e `&&` são **alta certeza** (POSIX, estável
  há décadas) — pode afirmar sem ressalva.
- O exemplo (`saida.md`, tokens "rating"/"stress") é do caso-trilho — coerente com o
  resto da aula.
- **Honestidade a manter:** o grep é o exemplo *mais simples* de verificador externo.
  Outros: `jq` (JSON), `pytest` (testes), `test -f` (arquivo existe), validador de
  schema. O grep é a porta de entrada didática, não o único enforcement possível.
- **Não confundir o aluno:** enforcement não é "saber programar" — é "existir algo
  fora do modelo que reprova". O grep só torna isso *concreto e visível*.
