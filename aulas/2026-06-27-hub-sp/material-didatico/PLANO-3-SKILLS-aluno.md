# Plano — 3 skills do aluno (tripé do Framework Injection)

> **Função:** plano de implementação das 3 skills que os alunos usarão na aula. Escrito enquanto Renato revisa os docs-fonte. **Nada implementado ainda — plano para aprovação.**
> **Princípio de design:** estas são skills de ALUNO — deliberadamente mais simples que o ecossistema FIG (`forja` 289 linhas, `forja-pro` 359, `fig/forge-pro` 332). Alvo: cada SKILL.md ≤ ~150 linhas, uso em 1 comando, zero setup.
> **Descoberta-chave:** o motor já existe. `promptforge.py` (670 linhas) já tem `syntactic_pruning()`, `sde_operations()`, `calculate_ds()`, `generate_fi_machine/human()`. As 3 skills **destilam e expõem** esse motor de forma didática — não reescrevem do zero. `[AF]`

## ⚠️ REQUISITO DE PRIMEIRA ORDEM — atualização ao estado da arte (decisão 2026-06-27)

O `promptforge.py` é de **8-jun**. Houve refinamentos substanciais DEPOIS, que as skills DEVEM incorporar. **Princípio: atualizado por dentro, simples por fora** — o aluno se beneficia do estado da arte sem ver os acrônimos de pesquisa.

**Refinamentos pós-8-jun a embutir (verificados nos arquivos):**
1. **SCA (Semantic Coercion Axis)** — o eixo priming↔enforcement renomeado (paper L2 v0.5, 13-jun; nome de Goldberg/coerção construcional). Dois vetores: **P2E** (priming→enforcement, ascendente — é o que a Skill 3 opera) e **E2P** (enforcement→priming, calibração HARD→SOFT por domínio). → *Embutido na lógica da Skill 3; o aluno vê "atravessar a ponte", não "P2E".*
2. **bridge_width rigoroso** — definição operacional: regra **enforceable** = condicional decidível e verificável; **cognitive** = orientação que prima mas não vincula. → *Skill 3 usa essa definição exata.*
3. **RFI = FI × DA** — o artefato canônico é Reasoning Framework Injection = conteúdo cognitivo (FI) × eixo de entrega (DA). Confirma a DA como eixo ortogonal transversal. → *Skill 1 gera um RFI, não só um FI.*
4. **Density ≠ Efficacy** (estudo σ*) — "um número real não é automaticamente invariante". → *Skill 2 mede densidade SEM prometer que densidade = qualidade do output.*
5. **P-VEX + limited-efficacy veto** — 4º critério do classificador enforceable (veto sobre delegação-a-lei-futura), triangulado (Fleiss κ=0.53). → *Skill 3 aplica o veto ao propor asserts.*

**REGRA DE HONESTIDADE (G6, decisão 2026-06-27):** as skills **NUNCA cravam número de comparação não-verificado**.
- ❌ Proibido: "N× melhor que o controle", citar o **0.33** (achado G6: esse controle não tem proveniência — mede 0.0 sob o mesmo classificador).
- ✅ Permitido: o score real do prompto do aluno, medido naquele momento.
- Fonte: `PAPER-L2-CODEXDRIVER-BRIDGE-WIDTH-DRAFT.md` §G6.

---

## A arquitetura: por que 3, e como se relacionam

As 3 skills mapeiam os 3 eixos da aula — e formam uma **cadeia de dependência**, não 3 ilhas:

```
   Skill 1 — FORJAR          Skill 2 — MEDIR           Skill 3 — ATRAVESSAR
   (gera o FI canônico)      (mede a densidade)        (priming → enforcement)
        │                          ▲                          ▲
        │  usa internamente ───────┘                          │
        └──────────────  chama para escalar a [VERIFICAÇÃO] ──┘
```

- **Skill 2 (DS) valida a Skill 1** — depois de forjar, o aluno mede e vê o número subir.
- **Skill 3 (Enforcement) completa a Skill 1** — a `[VERIFICAÇÃO]` do FI gerado nasce como priming; a Skill 3 a escala para enforcement.

**Decisão de design pendente (a 1ª pergunta a você):** as 3 são *independentes* (cada uma roda sozinha, o aluno encadeia manualmente) ou a Skill 1 *chama* a 2 e a 3 internamente? Recomendo **independentes mas componíveis** — mais simples de ensinar ("agora rode a skill 2"), e cada uma é um conceito didático isolado. Mas registro a alternativa.

---

## SKILL 1 — `fi-forja` (gerador de FI canônico, versão aluno)

**Objetivo.** Pegar um pedido cru do aluno e devolver um FI na forma canônica (as 8 seções + os 7 instrumentos), simples o suficiente para um iniciante usar sozinho. É o "Prompt-Forge como skill, mais simples".

**O que a diferencia do FIG/forja-pro (a canonicidade NÃO se degrada, a interface sim):**
| FIG / forja-pro (avançado) | fi-forja (aluno) |
|---|---|
| têmpera adversarial multi-papel | sem têmpera (isso é a skill /forja, separada) |
| roteamento multi-modelo, fallback | 1 caminho só |
| classificação fina + métricas internas | classificação simples (domínio + modalidade) |
| ~330-360 linhas | alvo ≤150 linhas |
| pressupõe o forjador | guia o iniciante passo a passo |

**Operações que mantém (a integridade canônica):**
1. Poda sintática (instrumento 2) — limpa o pedido cru.
2. Classifica domínio + modalidade (Declarativo/Procedimental/Avaliativo/Ético/Composicional).
3. Gera as 8 seções: `[PAPEL][OBJETIVO][MÉTODO][CONTEXTO][FONTES][OUTPUT][CONSTRAINTS][VERIFICAÇÃO]`.
4. Aplica a **posicionalidade** (âncoras nas bordas, curva-U) — instrumento 7.
5. Inclui **MetaBlock** (instrumento 6).
6. Aplica a regra da **coda condicional** (re-ancora termo denso, OU MetaBlock encerra se Ético).
7. Entrega **dual-legibilidade**: FI-máquina (denso) + FI-humano (rotulado).

**Input (interface reduzida):**
```
/fi-forja "seu pedido cru aqui"
   [opcional] --dominio juridico|codigo|financeiro|pesquisa|geral
   [opcional] --executor forte|medio   (calibra densidade — Adaptive FI)
```

**Output:**
```
1. FI-máquina (prosa densa, pronto pra colar na IA)
2. FI-humano (as 8 seções rotuladas, pra você entender)
3. DS antes → depois (chama a Skill 2)
4. Aviso: "a [VERIFICAÇÃO] está como priming — rode /fi-enforce para escalar"
```

**Exemplo I/O (caso-trilho):**
- Input: `/fi-forja "faça uma análise de risco de crédito"`
- Output: o FI de 8 seções do `caso-trilho-risco-credito.md`, com DS 1.3→4.4 e o aviso de enforcement.

---

## SKILL 2 — `ds-meter` (medidor de densidade semiótica + justificativa)

**Objetivo.** Medir a DS de um prompt OU de um termo, dar o score (1.0–5.0), **e justificar os critérios** — o que você pediu explicitamente: não só o número, mas *por que* esse número.

**O diferencial (a justificativa é o coração):** as outras ferramentas dão o número; esta **explica a medida**. Para cada avaliação, devolve:
1. O score (1.0–5.0).
2. **Os critérios aplicados** — quais termos são densos, quais são genéricos, por quê.
3. A distinção **dsc × dsd** quando relevante (termo culturalmente rico mas distribucionalmente raro = alerta).
4. Sugestões de operação SDE para subir o score (densify/rarefy/rotate/subtract/blend).

**Como mede (transparente, não caixa-preta):** usa `calculate_ds()` do promptforge como base, mas **expõe o raciocínio**:
- razão método/superfície (quanto de método por palavra)
- presença de termos-âncora de domínio (dsd alta)
- penaliza genéricos ("fazer", "coisa", "análise" solta)
- premia termos que ativam frame (Fillmore) — "rating interno", "stress-test"

**Input:**
```
/ds-meter "prompt ou termo a medir"
   [opcional] --dominio   (mede dsd no domínio certo)
   [opcional] --comparar "versão A" "versão B"   (antes/depois)
```

**Output (o que torna a skill única):**
```
DS: 4.4 / 5.0

POR QUÊ (critérios):
  ✓ "rating interno" — termo-âncora financeiro, dsd alta (ativa frame bancário)
  ✓ "stress-test em 3 cenários" — método explícito, não vago
  ✗ "análise" (sozinho) — genérico, dsd baixa → considere densificar
  
dsc × dsd: "rating interno" tem dsc e dsd altas no domínio financeiro ✓
           (se fosse um jargão local, alertaria: dsc alta, dsd baixa)

SUGESTÃO SDE: aplicar DENSIFY em "avaliar" → "auditar com rating"
              subiria ~0.3
```

**Exemplo I/O:**
- Input: `/ds-meter --comparar "faça uma análise de risco" "aplique rating interno com stress-test"`
- Output: `DS 1.3 → 4.2`, com a justificativa termo a termo.

---

## SKILL 3 — `fi-enforce` (consultor priming → enforcement)

**Objetivo.** Pegar um prompt (cognitivo, cheio de "deveria") e ajudar o aluno a **identificar hipóteses de enforcement** e criar os **critérios externos** que fazem a travessia priming→enforcement. É a aplicação prática do `FONTE-classificacao-priming-enforcement.md`.

**O que faz (o método dos 2 níveis + 3 perguntas):**
1. Lê cada linha do prompt e aplica o **teste de 3 perguntas** (condição binária? · verificador externo? · reprova se falha?).
2. Classifica cada cláusula: PRIMING · PRIMING DISFARÇADO · ENFORCEMENT.
3. Para cada **PRIMING DISFARÇADO** (a "catraca de papelão"), **propõe o ASSERT executável** que falta — o verificador externo, calibrado ao contexto do prompt.
4. Calcula o **bridge_width** antes/depois.

**O coração (o que você pediu):** "criar critérios externos, de acordo com o contexto do prompt". A skill **gera a hipótese de enforcement contextual** — não um assert genérico, mas o `cmd:`/`test`/`grep`/schema certo para *aquele* prompt.

**Input:**
```
/fi-enforce "prompt ou FI a analisar"
```

**Output:**
```
ANÁLISE DA PONTE (bridge_width atual: 0.0)

Linha: "NUNCA recomende sem os 5 eixos"
  → PRIMING DISFARÇADO (parece regra, nada reprova)
  → HIPÓTESE DE ENFORCEMENT:
     ASSERT: a saída contém as 5 seções [LIQUIDEZ][ALAVANCAGEM]...[RATING]
     cmd: grep -qE "liquidez|alavancagem|rentabilidade|stress|rating" saida.md
     → agora REPROVA se faltar um eixo. Atravessou para enforcement. ✓

Linha: "considere os cenários" 
  → PRIMING (cognitivo, por design — mantém como CHECAGEM)

bridge_width: 0.0 → 0.5  (1 de 2 verificáveis cruzou)
```

**Conversão prosa → assert (obrigatória, exemplo):**
- Prosa: *"garanta que cita as fontes"*
- Assert: `grep -cE "\[(auditado|benchmark|estimativa)\]" saida.md` ≥ 2 → reprova se < 2 fontes rotuladas.

---

## DECISÕES DE PLANO (para você, quando voltar da revisão)

1. **Formato:** skills `.md` puras (instrução para o agente, como renato-pi) ou skills com **script Python** anexo (como o promptforge)? As `.md` são mais simples de compartilhar e não exigem ambiente; o Python dá número real e reproduzível. **Recomendo `.md` + reaproveitar o promptforge.py como backend opcional** (a skill funciona só com o agente; quem tiver Python tem o número exato).

2. **Onde moram:** `~/.aiox/skills/fig/` (junto do ecossistema FIG) ou uma pasta nova `~/.aiox/skills/aula/` (isoladas, fáceis de empacotar para os alunos)? Recomendo **pasta nova `aula/`** — empacota e distribui sem arrastar o resto.

3. **Independentes vs encadeadas:** as 3 rodam sozinhas (aluno encadeia) ou a Skill 1 chama a 2 e a 3? Recomendo **independentes mas componíveis**.

4. **Nomes:** `fi-forja` · `ds-meter` · `fi-enforce` — ou prefere outros? (evitei "forge" para não colidir com o FIG).

5. **Distribuição ao aluno:** as skills viram um `.zip` que o aluno descompacta em `~/.claude/skills/` ou `~/.aiox/skills/`? Ou um repositório? Ou colável no Claude.ai? Isso decide o formato final.
