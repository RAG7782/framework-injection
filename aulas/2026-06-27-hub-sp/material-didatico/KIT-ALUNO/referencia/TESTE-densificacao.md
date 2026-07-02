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

O erro fatal: assumir que DSc alta ⇒ DSd alta. Nem sempre. O teste separa as duas.

---

## O protocolo (reprodutível — não "impressão")

> A versão ingênua ("digita o termo isolado e vê o que vem") **falha no seu próprio critério**:
> é priming disfarçado de teste (uma amostra estocástica que se auto-aprova). Para virar teste,
> precisa de repetição e de um julgamento externo. Aqui está a versão que passa na catraca.

**Passo 1 — Isolar.** Envie ao modelo-alvo **só o termo**, sem prompt, sem contexto:
> `diagnóstico clínico`  ·  `rating interno`  ·  `gambiarra`  ·  `stress test`

**Passo 2 — Repetir N vezes** (mínimo 3, ideal 5), em sessões limpas (sem memória entre elas).
Isto controla a estocasticidade: um termo verdadeiramente denso "acende a mesma galáxia" toda vez.

**Passo 3 — Ler a vizinhança que acende.** Em cada resposta, anote os conceitos que o modelo
traz espontaneamente. Classifique:
- **Denso (DSd alta):** o modelo traz **método/prática/estrutura** do especialista — os passos,
  as ferramentas, os critérios do domínio. Ex.: "diagnóstico clínico" → anamnese, exame físico,
  hipótese diagnóstica, exames complementares, diagnóstico diferencial.
- **Raso (DSd baixa):** o modelo devolve **definição genérica de dicionário/Wikipédia**, ou
  varia muito entre as N rodadas. Ex.: "gambiarra" → "solução improvisada" e para por aí.

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

## Atalho com ferramenta

O `/ds-meter` já distingue DSc de DSd e dá o score com justificativa — use-o para uma primeira
leitura. O teste manual das N rodadas é a **prova empírica** quando o score estiver na fronteira,
ou quando você trocar de modelo-alvo (a DSd muda de modelo para modelo — lembre do interpretante:
um modelo chinês tem DSd diferente de um modelo americano para o mesmo termo).

## A armadilha final (ilusão de conhecimento)

Assumir cegamente que o jargão ultra-específico do seu escritório se traduz em DSd na máquina é
**a receita pronta para a alucinação**: você usa uma sigla complexa, a IA não a tem representada,
e — para não deixar em branco — preenche o vazio com informação inventada. O teste de densificação
é o antídoto: **prove a densidade antes de confiar nela.**
