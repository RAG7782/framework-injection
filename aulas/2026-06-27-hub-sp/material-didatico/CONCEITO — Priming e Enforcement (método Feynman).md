---
date: 2026-06-21
type: R
title: "Priming e Enforcement (conceito canônico, método Feynman) — Framework Injection"
project: framework-injection / artesanato-digital
confidence: alta
tags: [framework-injection, priming, enforcement, harness, feynman, conceito-canonico, intencao-delegada, artesanato-digital, didatico, H3-bridge]
links:
  - "../BLUEPRINT-FI-HARNESS-BRIDGE.md"
  - "2026-06-21-R-quarto-chines-searle-intencionalidade.md"
  - "handoffs/2026-06-20-X-aula-fi-v15-conceito-artesanato.md"
---

# Conceito Canônico — Priming e Enforcement (método Feynman)

> **Proveniência:** CONSOLIDA o que já estava fixado no corpus — fronteira ontológica do `BLUEPRINT-FI-HARNESS-BRIDGE.md` §2 ("o harness constrange; o FI induz", linha 37-46) + leitura do priming como ato de delegação (documento canônico Artesanato Digital, §intenção delegada). Não cunhado do zero: destilado e dado forma didática. Inferência minha marcada como tal.

## Critério-mestre (a navalha, não-circular)
> **"O agente PODE desobedecer?"**
> - **Sim** (deveria, mas é livre p/ ignorar) → **PRIMING**
> - **Não** (o sistema não deixa passar) → **ENFORCEMENT**

## Fundamento etimológico (funda o conceito; não o altera)
A oposição já está inscrita nas raízes latinas — verificado em etymonline/Wiktionary.
- **PRIMING ← lat. *primus* ("o primeiro")** ← PIE *\*per-* ("adiante, antes"). Sentido técnico ~1600: "realizar a primeira operação, preparar" (o *primer* do pintor antes da tinta; carregar a arma antes do disparo). → priming é **o gesto do que vem ANTES e PREPARA**: ordem e precedência no *tempo*, sem força.
- **ENFORCEMENT ← lat. *in-* + *fortis* ("pôr força dentro / tornar forte")** ← fr.ant. *enforcier* ← lat.tardio *infortiāre*. Sentido jurídico "compelir à obediência" atestado desde 1640. Mesma raiz de força/forte/fortaleza. → enforcement é **infundir uma FORÇA que torna a regra inabalável**: da ordem da *força*, não do tempo.
- **Síntese canônica:** *primus* (tempo: precede, prepara) → *fortis* (força: impõe, não cede). O FI é a arte de fazer a **preparação prévia (*primus*) escalar até a força inabalável (*fortis*)** — e essa é exatamente a passagem estocástico→determinístico. A etimologia FUNDA a distinção predispor vs. constranger.

---

## Âncora única (método Feynman): a ESTAÇÃO DE METRÔ
Um só modelo de mundo p/ os dois conceitos — a pessoa não troca de mente no meio.
> **A cena:** estação de metrô com uma multidão de passageiros. Cada passageiro = um caminho possível da resposta da IA. O modelo é uma *distribuição* de saídas, não uma só.

## PRIMING

**(1) Núcleo:** predispor a IA — enquadrar, densificar, dar método — p/ que ela *tenda* a responder de um jeito. Indução, não obrigação. Modelo livre p/ ignorar; só tornou um caminho mais provável.

**(2) Feynman (metrô):** priming é a **SINALIZAÇÃO da estação** — placas, setas no chão, cordões de fila, anúncios. **Não impede** ninguém de ir para o lado errado (um teimoso pode furar), mas a multidão *tende* a escoar pela seta. Não elimina caminhos: **reordena as probabilidades** — desloca a massa da multidão p/ a plataforma certa. Continua estocástico.

**(3) Técnico:** operação linguística do FI, vive **no texto** do prompt/contexto. Densificação semiótica, papel, hierarquia de fontes, `[META-RACIOCÍNIO]` — predispõem a distribuição de saída (deslocam os *logits*/softmax) sem garanti-la. **Probabilístico e violável por natureza.**

**(4) Exemplo:** `"Antes de responder, identifique a suposição mais crítica que, se falsa, invalidaria a resposta."` O modelo *deveria* fazer — e provavelmente fará. Mas se esquecer, **nada o impede**; a resposta sai assim mesmo. Priming puro.

---

## ENFORCEMENT

**(1) Núcleo:** constranger a IA — bloquear, executar, verificar. Obrigação, não sugestão. Mecanismo fora do texto que **não deixa** a resposta passar se a condição falha. Agente **não pode** desobedecer.

**(2) Feynman (mesma estação):** enforcement é a **CATRACA.** Sem bilhete válido, **não gira** — não importa intenção, pressa ou teimosia: o caminho não-autorizado **deixa de existir como possibilidade**. A catraca não torna o caminho certo *mais provável* (isso é a sinalização) — ela torna o errado **impossível**. Ela **colapsa a distribuição**: antes, muitos passageiros possíveis (estocástico); depois, só passam os que cumprem a regra (determinístico no ponto de verificação).

**(3) Técnico:** vive **no runtime do harness físico** (código), não no texto. É um *gate*: teste programático que **reprova** a saída. **Binário e não-violável.** Separa "o modelo deveria verificar" de "o sistema obriga a verificação a existir".

**(4) Exemplo:** gate **G4** que roda `curl`/`pytest`/`docker ps` e **reprova** a resposta se a prova programática falha. O modelo pode *dizer* "está funcionando"; o gate executa o teste de verdade e, se falha, a resposta **não é aceita**. Não há "deveria"; há "obriga".

---

## A sequência (isomorfismo) + a passagem estocástico → determinístico
> **A sinalização (priming) faz a multidão *tender* à plataforma certa; a catraca (enforcement) garante que *só* quem cumpre a regra passa.** A 1ª reordena probabilidades; a 2ª elimina o que não cumpre. Juntas: fluxo caótico (estocástico) → fluxo verificado na saída (determinístico).

| Na estação | No Transformer (mecanismo real) |
|---|---|
| Multidão de passageiros | Distribuição de probabilidade sobre próximos tokens (softmax) |
| Sinalização (priming) | Prompt/contexto desloca os *logits* — sobe a prob. de certas continuações. **Continua estocástico.** |
| Catraca (enforcement) | *Gate* **fora do modelo** (harness) que testa a saída e **reprova/refaz** se falha. **Aqui nasce o determinismo.** |

**Honestidade técnica (inferência marcada):**
- **Priming sozinho NUNCA torna o Transformer determinístico** — só remodela a distribuição. Nem `temperature=0` dá determinismo forte (reduz variância; a natureza segue probabilística).
- **O determinismo só entra pelo enforcement** porque ele **não vive dentro do modelo, vive fora** (no harness). Não é propriedade injetada no Transformer; é propriedade **imposta na fronteira de saída**.
- **Releitura de H3:** o FI é a ponte onde a sinalização (priming/estocástico) **escala até virar** catraca (enforcement/determinístico). `[VERIFICAÇÃO]` no texto = sinalização; quando *dispara um gate G4 executável* = catraca. **A passagem estocástico→determinístico é a sinalização virando catraca.**

---

## Tabela contrastiva (canônica)

| Dimensão | **Priming** (indução) | **Enforcement** (constrangimento) |
|---|---|---|
| Verbo-núcleo | predispõe, enquadra, densifica | bloqueia, executa, verifica |
| O agente pode desobedecer? | **Sim**, em princípio | **Não** |
| Onde habita | texto do FI (prompt/contexto) | runtime do harness físico (código) |
| Natureza lógica | probabilístico, violável | binário, não-violável |
| Analogia Feynman (âncora única: metrô) | a sinalização da estação (setas, placas) | a catraca da estação |
| Efeito na distribuição | reordena probabilidades (estocástico) | colapsa a distribuição (determinístico) |
| Exemplo | "antes de responder, identifique a suposição crítica" (*deveria*) | gate G4 reprova se prova programática falha (*obriga*) |
| Falha típica | modelo ignora e ninguém percebe | nenhuma — ou passa, ou é barrado |

## A ponte (H3 — por que importa)
Tese central do FI: o priming **pode escalar até virar** enforcement. `[VERIFICAÇÃO]` num FI **hoje** é priming (modelo *deveria* verificar); **deveria** virar enforcement (dispara gate G4 que *obriga*). Esse ponto de transição — indução linguística convocando constrangimento físico — é o que o Framework Injection nomeia e o harness sozinho não teoriza.

> **Frase-síntese (já no corpus):** *"O priming é o ato de delegar a intenção; o enforcement é a intenção delegada virando mundo."*
> Searle: priming = ato ilocucionário de instituir a intenção no substrato; enforcement = intenção materializada numa barreira não-burlável.
