# Teste de densificação — o termo é denso PARA O MODELO, ou só para você?

> **O que esta página resolve** (apontamento do peer-review 2026-06-27): a poda sintática manda
> "não quebre o conceito-chave" e a densidade manda "use o termo denso" — mas **como o aluno SABE
> se o termo que ele acha denso é denso de verdade no modelo-alvo?** "Gambiarra" é densíssima para
> o brasileiro (DSc alta) e pode ser um vetor quase vazio para um modelo treinado na Califórnia
> (DSd baixa). Sem esse teste, a pessoa poda o entorno confiando num termo oco → o prompt colapsa.
> "Entra pouco, sai linguiça."
>
> **Lastro:** distinção **DSc (cultural) × DSd (distribucional)** do `DSc-DSd-DISTINCTION.md` +
> `ds-meter`. `[AF]` o protocolo N-amostras abaixo é uma proposta para tornar o teste **reprodutível**
> — porque a versão ingênua ("mande o termo e veja o que acende") é ela mesma estocástica: roda duas
> vezes, dá respostas diferentes. Um teste que não se repete não é teste — é impressão.

---

## A distinção que o teste mede

- **DSc — densidade cultural:** quanto o termo carrega numa comunidade humana. ("gambiarra",
  "jeitinho", jargão do seu escritório.) **Você sente essa.**
- **DSd — densidade distribucional:** quanto o termo carrega **na representação do modelo-alvo**.
  Depende de como o modelo foi treinado. **É esta que importa para o FI.**

O erro fatal: assumir que DSc alta ⇒ DSd alta. Nem sempre. E o inverso também existe — "leveraged
buyout" tem DSc baixa para o leigo mas DSd **altíssima** no modelo (corpus financeiro
superrepresentado). O modelo às vezes sabe mais que o informante cultural. **O teste separa as duas
densidades e diz qual é a que você tem na mão.**

---

## O gancho conceitual: o teste ingênuo falha no próprio critério que ele impõe

Antes do protocolo, o ponto que amarra tudo. A regra de enforcement do FI é: **prove antes de
confiar.** Ora — a versão ingênua do teste ("digita o termo isolado e vê o que acende") **viola
exatamente essa regra.** Ela é *uma única amostra estocástica* que se auto-aprova: roda uma vez, o
modelo cospe algo bonito, e você conclui "denso". Roda de novo, vem outra coisa. Você não provou
densidade — você viu **um sorteio** e chamou de medida.

É a mesma armadilha que o FI combate no prompt do aluno, agora escondida dentro da própria
ferramenta de auditoria. Um teste que não se repete não prova nada; ele *performa* rigor. A correção
é o que torna isto um teste de verdade: **repetição (controla o acaso) + julgamento externo binário
(controla o viés de quem olha).** É por isso que o protocolo abaixo tem N rodadas e uma tabela de
veredito — não por burocracia, mas porque sem os dois ele recai na impressão que dizia estar medindo.

---

## O protocolo (reprodutível — não "impressão")

**Passo 1 — Isolar.** Envie ao modelo-alvo **só o termo**, sem prompt, sem contexto, sem "explique",
sem "o que você sabe sobre". Só o termo, cru:
> `diagnóstico clínico`  ·  `rating interno`  ·  `gambiarra`  ·  `stress test`

O isolamento é deliberado: com contexto, você mesmo injeta a densidade que queria medir (priming).
Cru, só acende o que o modelo **já carrega** — que é o que você quer saber.

**Passo 2 — Repetir N vezes** (mínimo 3, ideal 5), em sessões limpas (sem memória entre elas — abra
uma nova conversa a cada rodada, ou o modelo lê a própria resposta anterior e converge artificialmente).
Isto controla a estocasticidade: um termo verdadeiramente denso **acende a mesma galáxia toda vez**;
um termo oco varia de rodada para rodada porque o modelo está improvisando por cima do vazio.

**Passo 3 — Ler a vizinhança que acende** (com critério operável — ver seção abaixo). Em cada
resposta, anote os conceitos que o modelo traz espontaneamente e classifique-os pelos sinais concretos.

**Passo 4 — Veredito (o julgamento externo, binário):**

| Sinal nas N rodadas | Veredito | Ação |
|---|---|---|
| Traz método/estrutura do domínio, **consistente** entre rodadas | **DSd ALTA** | pode podar o entorno — o termo aguenta o peso sozinho |
| Definição genérica, ou **varia muito** entre rodadas | **DSd BAIXA** (só DSc) | **não pode podar** — ancore com descrição explícita (as "muletas descritivas") |

> **Regra de bolso:** pode com segurança só o que sobreviveu ao teste. Se o termo é denso só
> para você (DSc) e não para o modelo (DSd), **a poda vai falhar** — o modelo preenche o vazio
> com invenção. A dor de descrever o que o termo "deveria" carregar é o sinal de que ali há DSd
> baixa: é exatamente o entorno que você NÃO pode cortar.

---

## Como ler a vizinhança sem chutar — o critério operável

"Ler o que acende" soa subjetivo. Não é, se você procurar **sinais concretos** em vez de "sentir".
A pergunta objetiva é uma só: *o modelo devolveu o **método do domínio** ou a **entrada de dicionário**?*

**Sinais de DSd ALTA (método do domínio acendeu) — conte quantos aparecem:**
- [ ] **Passos ou sequência de trabalho** — o modelo lista *o que o especialista faz, em ordem*
      (não o que a coisa *é*). Ex.: anamnese → exame físico → hipótese → exames complementares.
- [ ] **Ferramentas/instrumentos nomeados** do ofício (não genéricos): "current ratio", "súmula
      vinculante", "diagnóstico diferencial", "cobertura de juros".
- [ ] **Critérios de decisão / trade-offs** — quando usar X e não Y, o que conta como bom/ruim.
- [ ] **Vocabulário que puxa mais vocabulário** — um termo técnico acende três outros do mesmo campo
      (spreading activation). A galáxia tem estrutura, não é uma nuvem solta.
- [ ] **Consistência entre as N rodadas** — o mesmo núcleo reaparece; muda a redação, não o conteúdo.

**Sinais de DSd BAIXA (só acendeu o verbete) — bandeiras vermelhas:**
- [ ] **Paráfrase de dicionário** e ponto: "solução improvisada", "análise de uma situação".
- [ ] **Hedging genérico**: "depende do contexto", "existem várias abordagens" — o modelo tapa buraco.
- [ ] **Deriva entre rodadas**: rodada 1 fala de uma coisa, rodada 3 de outra sem núcleo comum.
- [ ] **Sinônimos laterais em vez de método**: "gambiarra" → "hack", "workaround", "puxadinho" — troca
      a palavra, não entrega a prática.

**A régua binária:** **≥ 3 sinais verdes consistentes → DSd ALTA.** Predominância de bandeiras
vermelhas, ou verde que não se repete → **DSd BAIXA.** Não é nota de 0 a 10; é passou/não-passou,
porque a decisão que ele alimenta também é binária: *podo ou não podo o entorno?*

---

## Exemplo trabalhado ponta a ponta — "anamnese" (passa) vs "sinergia operacional" (falha)

Duas rodadas completas, lado a lado, para você ver o veredito nascer dos sinais — não de opinião.
*(Respostas abreviadas e representativas; o padrão é o que importa, não a redação exata do seu modelo.)*

### Termo A — `anamnese` (candidato a DSd ALTA)

| Rodada | O que o modelo trouxe (espontâneo, termo isolado) |
|---|---|
| 1 | "Entrevista clínica inicial: queixa principal, história da doença atual (HDA), antecedentes pessoais e familiares, revisão de sistemas, hábitos de vida. Precede o exame físico." |
| 2 | "Coleta estruturada da história do paciente — identificação, QP, HDA, história patológica pregressa, medicações em uso. Base para a hipótese diagnóstica." |
| 3 | "Primeira etapa da consulta: escuta e interrogatório dirigido; alimenta o raciocínio clínico e o diagnóstico diferencial." |

**Leitura pelos sinais:** passos em ordem ✓ · instrumentos nomeados (QP, HDA, revisão de sistemas) ✓ ·
vocabulário que puxa vocabulário (diagnóstico diferencial, raciocínio clínico) ✓ · núcleo estável nas
3 rodadas ✓. **4 sinais verdes consistentes.**
**Veredito: DSd ALTA.** → Você **pode podar**: escreva `faça a anamnese` e o modelo reconstrói a cena
inteira sozinho. Não precisa listar "pergunte a queixa principal, depois o histórico…" — isso já está
dentro do termo, para o modelo.

### Termo B — `sinergia operacional` (candidato a DSd BAIXA — jargão de PowerPoint corporativo)

| Rodada | O que o modelo trouxe (espontâneo, termo isolado) |
|---|---|
| 1 | "Ganhos de eficiência quando áreas ou empresas trabalham juntas; o todo rende mais que a soma das partes." |
| 2 | "Integração de processos para reduzir custos e evitar redundâncias. Comum em fusões e aquisições." |
| 3 | "Colaboração entre equipes que gera valor adicional; depende do contexto do negócio." |

**Leitura pelos sinais:** paráfrase de dicionário ✗ · hedging ("depende do contexto") ✗ ·
deriva (rodada 1 = eficiência abstrata, rodada 2 = M&A, rodada 3 = colaboração de equipes — sem núcleo
metodológico comum) ✗ · **nenhum passo, nenhuma ferramenta, nenhum critério de decisão.** Zero sinais
verdes estáveis.
**Veredito: DSd BAIXA (é DSc — vive nos slides, não no método).** → Você **NÃO pode podar**. Se
escrever só `avalie a sinergia operacional`, o modelo preenche o vazio com generalidade plausível
(exatamente a alucinação que o teste existe para pegar). **Ancore:** troque por um frame que o modelo
represente de fato — `quantifique a redução de custos por eliminação de funções redundantes e
consolidação de fornecedores pós-fusão` — ou mantenha as muletas descritivas ao redor do termo.

> **O contraste em uma frase:** "anamnese" carrega o **método** dentro de si na representação do
> modelo; "sinergia operacional" carrega só um **rótulo** — brilha na sala de reunião (DSc), apaga
> no vetor (DSd). Mesma aparência de "termo técnico"; densidade distribucional oposta. **Só o teste
> das N rodadas distingue os dois — o olho, não.**

---

## O teste multi-modelo — a DSd muda de modelo para modelo (e como provar isso)

DSd não é propriedade do termo; é propriedade do **par (termo, modelo)**. Um modelo americano e um
modelo chinês têm DSd diferente para "gambiarra"; um modelo grande tem DSd mais alta que um pequeno
para *quase tudo* (representações mais profundas). Se você troca de modelo-alvo, **o teste precisa ser
refeito** — o resultado de um não transfere para o outro. Isto é a *cross-model variance* do
`DSc-DSd-DISTINCTION.md`, feita à mão.

**Protocolo multi-modelo (variação do de cima):**

1. Escolha **o mesmo termo** e **2 modelos** (ex.: um frontier de fronteira e um modelo pequeno/local;
   ou um treinado majoritariamente em inglês vs um multilíngue).
2. Rode as **N rodadas em cada modelo**, sessões limpas, termo isolado — exatamente igual.
3. Preencha a mesma grade de sinais para cada modelo, separadamente.
4. Compare os vereditos.

**Grade de comparação (exemplo — termo `jeitinho`):**

| | Modelo A (frontier, multilíngue) | Modelo B (pequeno, EN-dominante) |
|---|---|---|
| Sinais verdes | traz o frame cultural brasileiro: informalidade, contorno de regra, negociação social ✓✓✓ | mapeia para "workaround"/"little way", perde a camada social ✗ |
| Consistência N rodadas | estável | deriva |
| **Veredito** | **DSd média-alta** | **DSd baixa** |

**Leitura da divergência:**
- **Vereditos iguais e altos** → termo robusto; a poda é segura em ambos.
- **Vereditos divergentes** (passa num, falha no outro) → **a DSd é instável para esse termo** — trate
  como DSd baixa por precaução e ancore, *a menos que você fixe o modelo-alvo* e teste só nele.
- **Regra operacional:** você não poda para "um modelo genérico". Você poda para **o modelo que vai
  rodar em produção.** Teste nesse. A densidade é dele, não da média.

---

## Atalho com ferramenta

O `/ds-meter` já distingue DSc de DSd e dá o score (1.0–5.0) com justificativa — use-o para uma
**primeira leitura rápida** e para pegar o alerta `dsc×dsd` (termo culturalmente rico mas
distribucionalmente raro). O teste manual das N rodadas é a **prova empírica** quando (a) o score do
`ds-meter` cai na fronteira (perto de 3.0), (b) você troca de modelo-alvo, ou (c) o termo é jargão
local/regional/de escritório — os casos onde a estimativa do medidor é menos confiável.

> **Honestidade (G6):** nem o `ds-meter` nem este teste provam que o **output** vai ficar melhor. Eles
> medem o **input** — se o termo ativa o frame no modelo. Densidade ≠ eficácia. O teste responde "posso
> podar o entorno sem o prompt colapsar?", não "esse prompt é bom".

---

## Exercício final (faça agora, antes de fechar a página)

Pegue **dois termos do seu próprio domínio**: um que você *aposta* que é método puro, e um que você
*suspeita* que é só jargão bonito da sua bolha. Sugestões para calibrar a intuição antes de escolher os
seus:

- **Aposte em passar (DSd alta):** `due diligence` · `conciliação bancária` · `revisão por pares` ·
  `teste A/B`
- **Aposte em falhar (DSc alta, DSd baixa):** a sigla interna do seu setor · `entregável` · `alinhamento
  estratégico` · o apelido que só sua equipe usa para um processo

**Roteiro (10 minutos):**

1. Rode o protocolo das N rodadas (mín. 3, sessões limpas) para **cada** termo, no modelo que você usa de verdade.
2. Preencha a grade de sinais verdes/vermelhos de cada um.
3. Dê o veredito binário (DSd ALTA / BAIXA) por termo.
4. **Para o que falhou:** reescreva-o em um frame que o modelo represente de fato (traduza para
   alto-DSd) OU escreva as muletas descritivas que você teria que manter ao redor dele.
5. **Bônus multi-modelo:** rode o termo que passou em um segundo modelo (menor, ou de outra língua). Ele
   ainda passa? Se não — você acabou de ver a DSd mudar de dono na sua frente.

**Gabarito de raciocínio (não de resposta — a sua depende do seu modelo):** se o termo que você jurava
ser denso derivou entre rodadas ou só devolveu dicionário, ele era **DSc, não DSd** — você o sentia
denso, o modelo não. Esse é o achado que salva o prompt: você ia podar o entorno de um termo oco. Agora
não vai.

---

## A armadilha final (ilusão de conhecimento)

Assumir cegamente que o jargão ultra-específico do seu escritório se traduz em DSd na máquina é
**a receita pronta para a alucinação**: você usa uma sigla complexa, a IA não a tem representada,
e — para não deixar em branco — preenche o vazio com informação inventada, fluente e errada. O teste
de densificação é o antídoto, e o gancho fecha o círculo: o FI exige *prove antes de confiar*; este
teste é você aplicando essa mesma exigência à sua própria matéria-prima. **Prove a densidade antes de
podar em cima dela.**
