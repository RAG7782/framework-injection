# Fonte canônica — Glossário integral do Framework Injection (para as lâminas)

> **Função:** documento-fonte de TODOS os termos e conceitos da aula, cada um em **tri-camada: Definição técnica → Analogia Feynman → Exemplo prático** (no caso-trilho de risco de crédito, para continuidade).
> **Princípio (decisão 2026-06-27):** completude na fonte, curadoria no palco. Tudo está aqui; o facilitador decide o que usar. Itens marcados `▸ aprofundamento` são puláveis sem quebrar o fio.
> **Rigor:** definições EXTRAÍDAS dos arquivos (sem inferência sobre termos canônicos). Fontes citadas por item. Onde inferi, está marcado `[INF]`.
> **Lastro principal:** `DSc-DSd-DISTINCTION.md` · `BLUEPRINT-FI-HARNESS-BRIDGE.md` · `GAGNE-FI-TEMPLATE.md` · `investigation-output-window.md` · `CONCEITO — Priming e Enforcement.md` · papers Zenodo (DOIs no corpus).

---

# PARTE I — A FORMA CANÔNICA: os 7 instrumentos do ofício

> **Distinção que a aula DEVE fazer explícita** (resolve a confusão atual entre os slides e o pipeline):
> - **Ordem da forma canônica = por importância conceitual** (SDE é o instrumento-mor, nº1).
> - **Ordem do pipeline de forja = por execução temporal** (poda é o passo 1; SDE é o passo 4).
> Não são contraditórias — são dois eixos. A aula apresenta os dois e diz qual é qual.

---

## 1 · DENSIDADE SEMIÓTICA (SDE — Semiotic Density Engineering)

**Definição técnica.** A operação de fazer cada palavra carregar mais método — substituir termos genéricos por termos de alta carga semântica. Mas "carga" tem **dois eixos** (Paper 9, DOI 10.5281/zenodo.19382350; `DSc-DSd-DISTINCTION.md`):

- **dsc — densidade semiótica cultural:** quanto um termo carrega **numa comunidade humana** (frames, protótipos, conotações, narrativas). É relativa à cultura. (Rótulo canônico: *cultural*, fiel ao `DSc-DSd-DISTINCTION.md` — "Cultural Semiotic Density".)
- **dsd — densidade semiótica distribucional:** quanto o termo carrega **na representação de um modelo específico** (a riqueza da vizinhança do termo no espaço de embeddings do modelo). É relativa ao modelo, medível.
- **A relação:** `dsd` é uma **compressão com perda** de `dsc`, feita pelo treino. Um termo pode ter `dsc` altíssima e `dsd` baixa (culturalmente rico, mas raro para o modelo) — ou o inverso.

**Objetivo técnico.** Densificar o prompt para subir a `dsd` **do modelo-alvo** — não a `dsc`. É isso que ativa o frame certo na máquina.

**As 5 operações da SDE** (`W7`): Densify · Rarefy · Rotate · Subtract · Blend. **(A Poda Sintática NÃO é uma operação SDE — é o instrumento nº2, separado. Confirmado 2026-06-27: SDE = 5 operações; alinhar o Painel que hoje cita 6.)**

**Analogia Feynman.**
- `dsc` = o quanto uma palavra significa **para uma pessoa daquela cultura**. "Gambiarra" para um brasileiro carrega um mundo (improviso, classe, identidade, orgulho-vergonha).
- `dsd` = o quanto a **mesma palavra** significa **para o modelo**. Num modelo treinado em inglês, "gambiarra" é quase oca — vira só "hack".
- **Densificar bem = escolher a palavra que é densa NA CABEÇA DO MODELO**, não só na sua. Se você usa um termo denso pra você mas raro pro modelo, você acha que carregou método e não carregou nada.

**Exemplo prático (caso-trilho).**
- Cru: *"faça uma análise de risco"* → "análise" e "risco" são genéricos (dsd média).
- Densificado: *"aplique metodologia de **rating interno** com **stress-test** em 3 cenários e **cobertura de juros**"* → cada termo ativa um frame técnico rico no modelo (dsd alta no domínio financeiro).
- **Erro a evitar:** usar um jargão de nicho que SÓ você conhece (dsc alta, dsd baixa) — o modelo não ativa o frame.

> ▸ **aprofundamento (anexo):** fórmulas `dsc(t,L)=|F_L(t)|/|t|` e `dsd(t,M)=S(N_ε(e_M(t)))/|t|_tokens`; divergência inversa (ex.: "leveraged buyout" — o modelo sabe mais que o humano médio); DSSD (Domain-Specific Semiotic Density) quando o domínio é a variável condicionante.

---

## 2 · PODA SINTÁTICA (SP — Syntactic Pruning)

**Definição técnica.** Remoção deliberada de redundância sintática do prompt **sem alterar o payload semântico** (`DSc-DSd-DISTINCTION.md` §Terminology: termo emprestado de ML/neural pruning). Tira fillers, hesitações, pidgin redundante. **Podar ≠ resumir** — resumir perde informação; podar tira só o ruído.

**Objetivo técnico.** Limpar o sinal antes de carregá-lo. Aumenta a razão densidade (menos tokens, mesmo significado).

**Analogia Feynman.** Tirar a ferrugem da lâmina antes de afiá-la. Você não muda o aço (o sentido) — só remove o que não é aço (o ruído). Resumir seria *encurtar a lâmina*; podar é *limpá-la*.

**Exemplo prático.**
- Cru: *"então tipo, eu queria que você meio que analisasse, sei lá, esse contrato aí pra mim, né"*
- Podado: *"analise este contrato"* — sinal preservado, ruído removido.

---

## 3 · CODEPROMPT (encoding do método em estrutura)

**Definição técnica.** A codificação do método de raciocínio em **estrutura** — o prompt organizado como código/lógica, não como prosa solta. Transforma instrução em arquitetura legível e auditável. `[INF parcial]` a definição operacional canônica vem do injetor; confirmar nome oficial (ver nota CMP abaixo).

**Objetivo técnico.** Dar ao método uma **forma** que coage a interpretação (lastro: Goldberg, Construction Grammar — a construção coage o sentido). Estrutura > prosa porque a estrutura é reaproveitável e verificável.

**Analogia Feynman.** A diferença entre *contar* uma receita de boca ("põe um tanto de farinha, sei lá") e *escrever* a receita estruturada (ingredientes / quantidades / passos numerados). A segunda não depende da sua memória nem da boa vontade de quem lê — a forma carrega o método.

**Exemplo prático.** O bloco `[MÉTODO] 1. liquidez 2. alavancagem 3. stress-test` não é "texto sobre o método" — é o método *encodado em estrutura numerada* que o modelo executa em ordem.

> **Nota de nomenclatura (verificar com Renato):** a memória registra **CMP — Cognitive Metaprogramming** como acrônimo a adotar dentro do FI. Confirmar se CodePrompt e CMP são o mesmo instrumento, sinônimos, ou camadas distintas.

---

## 4 · DELIVERY ARCHITECTURE (DA) — duas faces

**Definição técnica — FACE 1 (instrumento do FI, o `[OUTPUT]`).** A especificação da **forma de entrega** dentro do FI: profundidade, formato, estrutura e critérios de sucesso da saída. **Transversal, não só jusante:** está presente **desde a formulação** do FI (define o objetivo lá no início) E fecha (a forma final). Gagné mapeia como Evento 2 "informar objetivos" + Evento 6 "elicitar performance" (`GAGNE-FI-TEMPLATE.md` Bloco 7).

**Definição técnica — FACE 2 (camada arquitetural própria).** A disciplina de **planejar, estruturar, orquestrar e validar outputs completos que excedem uma única chamada ao LLM**, mantendo coerência e fidelidade ao framework injetado (`investigation-output-window.md` §5.2; paper DA, DOI 10.5281/zenodo.19939303). É **maior que o FI** — uma camada do ecossistema, para o problema da janela de saída.

**Objetivo técnico.** Face 1: garantir que o modelo saiba *o que produzir* e *como*, desde o começo. Face 2: entregar o que o modelo *sabe* produzir mas não consegue de uma vez só.

**Analogia Feynman.**
- Face 1 = a **planta da casa** entregue ao pedreiro **antes** da obra: já diz quantos cômodos, o acabamento, o formato. Não é algo que se decide no fim — guia desde a fundação.
- Face 2 = o **mestre de obras** que coordena entregar uma casa grande demais para um dia de trabalho: divide em etapas, mantém a planta coerente entre elas.

**Exemplo prático (Face 1, caso-trilho).** `[OUTPUT] Tabela por eixo (liquidez/alavancagem/rentabilidade) com valor, threshold e veredito; seção de stress-test; rating final + 1 parágrafo` — isto foi definido **junto** do objetivo, não no fim. É o que faz o modelo mirar a entrega certa desde o primeiro token.

> ▸ **aprofundamento:** Face 2 (orquestração multi-chamada, SYMBIONT, o problema da output window) — citar só se a sala perguntar sobre outputs longos.

---

## 5 · AGENT-FIRST DEVELOPMENT (superfície legível por agente)

**Definição técnica.** Projetar a saída (especialmente código) para ser **legível e operável por um agente de IA**: nome único no codebase, erro nunca silenciado, módulo auto-contido. Métrica associada: **DS-d de código** `DS-d = 1 / grep_hits` (quanto mais único o nome, mais alta a densidade — menos colisões). `[lastro: W12; corpus Agent-First Development]`.

**Objetivo técnico.** Reduzir o "Reading Debt" do agente — a distância entre o que o código diz e o que o agente consegue ativar. Código legível por agente = menos ambiguidade, menos erro de runtime.

**Analogia Feynman.** Organizar a oficina para que **outro artesão** (o agente) ache cada ferramenta sem perguntar: cada ferramenta tem um lugar único (nome único), nada está quebrado em silêncio (erro nunca engolido), cada bancada é completa em si (módulo auto-contido).

**Exemplo prático.** Função com nome único (`grep` retorna 1 hit, não 40), `except` que diz qual valor falhou e o esperado — em vez de `catch {}` mudo.

> ▸ **aprofundamento / cinturão:** só para quem forja código. Pular para plateia não-técnica.

---

## 6 · METABLOCK (a camada de metacognição)

**Definição técnica.** A seção que **não fala do domínio — fala do processo de raciocínio**. Instrui o modelo a: identificar a suposição crítica que invalidaria a resposta; sinalizar inferência vs afirmação; perguntar sob ambiguidade; calibrar confiança (`W13`, `L11`). É **priming puro** (induz metacognição; nada externo reprova).

**Objetivo técnico.** Fazer o modelo pensar sobre o próprio pensar antes de entregar — reduz erro confiante.

**Analogia Feynman.** O checklist mental do piloto **antes de decolar**: não é sobre o destino (o domínio), é sobre *o estado do próprio voo* — "o que eu estou supondo que, se falso, derruba tudo?". É o avião checando o avião.

**Exemplo prático (caso-trilho).** `[META-RACIOCÍNIO] identifique a suposição mais crítica (ex: qual fonte de dado, se falsa, inverteria o rating); sinalize dado verificado vs estimativa; se faltar demonstrativo essencial, pergunte antes de assumir.`

---

## 7 · REATUALIZAÇÃO DO TERMO DENSO (a coda — condicional)

**Definição técnica.** O fecho do FI **re-ancora o termo denso de domínio da abertura** (efeito de **recency** — a última coisa lida fica saliente; fecha o arco do FI). **Condicional ao tipo de FI** (`L11bis`, `W13`, injetor §4.4/STEP 7):
- **Regra geral:** o MetaBlock é penúltimo e a **coda densa** encerra, re-ancorando o conceito-âncora da abertura.
- **Exceção:** se o objetivo é **cognitivo/metacognitivo** (fi_type Ético / anti-alucinação), o **MetaBlock encerra** — porque aí a metacognição *é* o termo de maior carga.

**Objetivo técnico.** Aproveitar a curva-U da atenção (abertura + fecho = posições de maior saliência) para que o termo-mestre do domínio seja a primeira E a última coisa que o modelo "vê".

**Analogia Feynman.** O fim de uma boa palestra que **retoma a frase de abertura** — você sai com ela na cabeça (recency). Mas se a palestra foi sobre *como pensar* (não sobre um tema), o que deve ficar por último é o método de pensar, não o tema. A coda escolhe o que ecoa no fim.

**Exemplo prático.** FI de risco de crédito (domínio concreto) → a coda re-ancora *"rating de risco com rastreabilidade"*. FI anti-alucinação (metacognitivo) → o MetaBlock encerra, porque "não inventar" é a carga máxima.

---

## SÍNTESE DA PARTE I — os 7 × o eixo da ponte

| # | Instrumento | Lado da ponte | Eixo |
|---|---|---|---|
| 1 | Densidade Semiótica (SDE: dsc→dsd) | priming | densifica |
| 2 | Poda Sintática (SP) | priming | limpa |
| 3 | CodePrompt | priming | estrutura |
| 4 | Delivery Architecture | priming↔ (abre E fecha) | forma de entrega |
| 5 | Agent-First | priming | legibilidade agêntica |
| 6 | MetaBlock | priming (metacognição) | pensa o pensar |
| 7 | Reatualização/coda | fecho (recency) | re-ancora — condicional |

> **A VERIFICAÇÃO bicéfala** (ASSERTS + CHECAGENS) é o que atravessa para o enforcement — ver `FONTE-classificacao-priming-enforcement.md`. Os 7 instrumentos acima são priming; a ponte é a 8ª peça, a travessia.

---

# PARTE II — CONCEITOS TEÓRICOS (tri-camada · marcados por peso)

> Núcleo = a tese cai sem ele · Cinturão = enriquece · todos têm tri-camada (decisão "tri-camada para todos"). Os de menor peso vão como `▸ aprofundamento` (lâmina-anexo, puláveis).

## Linguísticos (por que densificar funciona)

### Frame Semantics — Fillmore (1982) · **núcleo**
- **Def:** uma palavra ativa um "frame" inteiro — uma cena estruturada de conhecimento. "Vender" ativa comprador, mercadoria, preço, troca.
- **Feynman:** dizer "garçom" acende a cena inteira do restaurante na sua cabeça — mesa, menu, conta, gorjeta — sem precisar descrever nada disso. A palavra é o interruptor da cena.
- **No FI:** o termo-chave certo ativa o frame de método inteiro no modelo. "Rating interno" acende a cena bancária completa.

### Construction Grammar / coerção construcional — Goldberg (1995, 2006) · **núcleo**
- **Def:** a *forma* de uma construção carrega sentido e **coage** a interpretação — independente das palavras.
- **Feynman:** o molde "X deu Y para Z" já te força a entender que houve transferência, mesmo com palavras inventadas ("ele deu um blark para ela"). A estrutura manda no sentido.
- **No FI:** a estrutura do FI (as 8 seções, a ordem) *coage* o modelo a raciociná-lo daquele jeito. É o lastro teórico de "estrutura > conteúdo".

### Prototype Theory — Rosch (1975) · cinturão
- **Def:** categorias têm membros mais centrais (protótipos) e mais periféricos. "Pardal" é mais "ave" que "pinguim".
- **Feynman:** se peço "desenhe um pássaro", você desenha algo perto do pardal, não um avestruz. O protótipo é o centro de gravidade da categoria.
- **No FI:** usar termos prototípicos nas âncoras ativa a categoria com mais força.

### Conceptual Blending — Fauconnier & Turner (2002) · cinturão
- **Def:** a mente funde dois espaços mentais e gera estrutura **emergente** (nova, que não estava em nenhum dos dois).
- **Feynman:** "cirurgião-açougueiro" — funde dois frames e cria um terceiro sentido (um cirurgião desastrado) que não está nem em "cirurgião" nem em "açougueiro".
- **No FI:** compor dois FIs gera capacidade emergente — o FI composicional.

### Conceptual Metaphor — Lakoff & Johnson (1980) · cinturão
- **Def:** pensamos um domínio nos termos de outro ("tempo é dinheiro" → "gastar/poupar tempo").
- **Feynman:** você "constrói" um argumento, "ataca" uma tese, "defende" uma posição — pensa debate como guerra sem perceber. A metáfora estrutura o raciocínio.
- **No FI:** transferir método entre domínios via metáfora (a "ponte", a "forja", a "têmpera" — tudo metáfora estruturante).

### Distributional Semantics — Firth (1957) · cinturão (base da dsd)
- **Def:** "you shall know a word by the company it keeps" — o sentido de um termo é dado pelos termos com que coocorre.
- **Feynman:** você entende uma palavra nova pela companhia dela na frase, mesmo sem dicionário. O contexto é a definição.
- **No FI:** é a base teórica da `dsd` — a densidade distribucional É a "companhia" do termo no espaço do modelo.

### Spreading Activation — Collins & Loftus (1975) · cinturão
- **Def:** ativar um conceito propaga ativação para os conceitos vizinhos na rede semântica.
- **Feynman:** pense "médico" e "hospital", "enfermeira", "doença" já ficam meio acesos sem você querer. A ativação escorre pela rede.
- **No FI:** a carga densa de um termo-âncora se propaga pela rede, pré-ativando o frame inteiro.

## Semiótico

### Tríade do signo + interpretante — Peirce (1931–58) · **núcleo**
- **Def:** todo signo tem Primeiridade (qualidade), Secundidade (referente), Terceiridade (interpretante — o efeito gerado). + 2 conceitos autorais seus: **interpretante algorítmico** (a IA como gerador de interpretante) e **semiose projetada** (desenhar o signo pelo interpretante que se quer gerar).
- **Feynman:** uma placa de trânsito (signo) só "funciona" pelo que faz o motorista *fazer* (o interpretante). Você não desenha a placa pela beleza — desenha pelo comportamento que quer causar.
- **No FI:** *signo pobre → resposta estocástica · signo rico → resposta quase-determinística.* Você forja o prompt (signo) mirando a resposta (interpretante) que quer induzir.

## Pedagógicos

### Zona de Desenvolvimento Proximal / scaffolding — Vygotsky · **núcleo**
- **Def:** a distância entre o que o aprendiz faz sozinho e o que faz com apoio estruturado (andaime). O andaime é retirado quando não é mais preciso.
- **Feynman:** as rodinhas da bicicleta — sustentam até a criança pedalar sozinha, depois saem. O FI é a rodinha que estrutura o raciocínio do modelo.
- **No FI:** o FI é o *scaffolding* — dá ao modelo a estrutura que ele ainda não tem sozinho (mais forte em modelos médios; ver Adaptive FI).

### Carga cognitiva — Sweller · **núcleo**
- **Def:** a memória de trabalho é limitada; aprendizagem falha quando a carga *extrínseca* (ruído) consome o espaço da carga *intrínseca* (o conteúdo real).
- **Feynman:** tentar fazer conta de cabeça enquanto alguém fala números aleatórios no seu ouvido — o ruído ocupa o espaço do raciocínio. O FI tira o ruído.
- **No FI:** o FI elimina a carga extrínseca (o modelo não gasta capacidade adivinhando o que você quer) — sobra capacidade para o método.

### Jogos de linguagem — Wittgenstein · cinturão
- **Def:** o sentido de uma palavra é seu uso dentro de uma "forma de vida" / prática — não há sentido fora do jogo.
- **Feynman:** "água!" significa coisas diferentes no restaurante, no deserto e na aula de química — o jogo define o sentido. Não há significado avulso.
- **No FI:** o FI ensina ao modelo *qual jogo* jogar — o domínio, as regras, o registro.

## Filosóficos

### Conhecimento tácito / Paradoxo do Artesão — Polanyi · **núcleo**
- **Def:** "sabemos mais do que conseguimos dizer" — a maestria é tácita, resiste à verbalização completa.
- **Feynman:** você sabe andar de bicicleta mas não consegue *escrever* a regra do equilíbrio de forma que outro aprenda só lendo. O saber está no corpo, não nas palavras.
- **No FI:** **por que a IA não cria o próprio framework** — criar o framework exige externalizar o tácito, e isso é o ato humano. O FI *é* a externalização do tácito; a IA opera dentro, mas não gera a externalização.

### Intencionalidade intrínseca vs derivada — Searle (1983) · **núcleo**
- **Def:** só mentes têm intencionalidade *intrínseca* (querer de verdade); artefatos têm intencionalidade *derivada* (emprestada por quem os usa). O termostato "quer" 20°C só no modo "as-if".
- **Feynman:** o termômetro não "quer" nada — você é que delega a ele a função de medir. A intenção é sua, emprestada a ele.
- **No FI:** **a intenção delegada** — a IA executa, não pretende. Toda intenção no que ela faz foi delegada por um humano. A intenção é o que não se terceiriza.

### Wu wei / passividade ativa — Laozi (Tao Te Ching) + Zhuangzi · **núcleo** (o princípio do ofício)
- **Def:** a ação sem forçar — "dispor o vazio para a forma emergir". Não é passividade: é a ação que flui da disposição certa, não do empurrão.
- **Feynman:** o Cozinheiro Ding de Zhuangzi corta o boi achando os vazios entre as juntas — a lâmina nunca cega porque não força o osso, escoa pelo espaço. Michelangelo "leu a pedra e tirou o que sobrava".
- **No FI:** o artífice *dispõe* a ponte (prime denso, enforcement no lugar certo) e deixa a inteligência atravessar. Não empurra o resultado — constrói a travessia.

### A maestria que se cultiva — Sennett (The Craftsman) · cinturão
- **Def:** a habilidade do artesão se *cultiva* pela prática lenta, não se copia por instrução. É uma escola, não um tutorial.
- **Feynman:** ninguém vira marceneiro lendo um manual — vira serrando mil tábuas. A mão aprende o que o texto não ensina.
- **No FI:** o Artesanato Digital é uma escola (cultiva-se o ofício de forjar FIs), não um conjunto de dicas.

---

# PARTE III — TERMOS AUXILIARES (definição curta + Feynman + exemplo)

| Termo | Definição | Feynman | No caso-trilho |
|---|---|---|---|
| **Pidgin digital** | a língua telegráfica de contato com a IA ("analisa isso") — empobrecida | o pidgin do porto: serve pra negociar, não pra fazer filosofia | "faça uma análise de risco" = pidgin |
| **bridge_width** | `asserts/(asserts+checagens)` — fração da verificação que constrange (vs só induz) | quantas placas viraram catracas de verdade | o FI tem 1 `grep` que reprova / 3 verificações = 0.33 |
| **Têmpera (ciclo /forja)** | forjar→martelar→recozer→resfriar: ataca a obra para fortalecê-la | temperar o aço: o calor+choque não *checa* o metal, *transforma* pelo teste | o Auditor ataca o FI; só as críticas que sobrevivem entram |
| **Sentinela / Auditor Constitucional** | papéis da têmpera: Auditor martela (ataca), Sentinela resfria (classifica OK/alucinação) | o advogado do diabo (Auditor) e o juiz que sela (Sentinela) | separação de papéis: quem cria ≠ quem critica ≠ quem aprova |
| **Índice de Confiança** | métrica que o Sentinela calcula após excisar alucinações | a nota de pureza do aço após a têmpera | quão limpo o FI saiu do ataque |
| **Curva-U / recency** | atenção é maior na abertura e no fecho; o miolo afunda | você lembra o começo e o fim do filme, o meio borra | âncoras nas bordas do FI, miolo conectivo |
| **Instruction-first** | abrir o FI pela instrução-âncora ([OBJETIVO]), não por preâmbulo | dizer o pedido antes da história, não depois | `[OBJETIVO]` abre o FI |
| **Dual-legibilidade (FI-máquina vs FI-humano)** | o mesmo FI em dois registros: denso p/ a LLM, rotulado p/ você | a planta técnica e a maquete da casa — mesma casa, dois públicos | prosa densa (máquina) vs `[PAPEL][OBJETIVO]...` (humano) |
| **Anti-drift / projeção determinística** | o FI-humano é projeção do FI-máquina, nunca 2ª geração | a tradução juramentada: espelha o original, não reescreve | o rotulado deriva do denso, sem divergir |
| **Gate G4** | a prova programática que reprova se a verificação falha (curl/pytest/docker) | o detector de metal do aeroporto: não confia na sua palavra, testa | `grep -q "rating" saida.md` reprova se faltar |
| **Parameter Explosion** | confiar em defaults implícitos = causa nº1 de falha em runtime | montar o móvel sem ler quais parafusos — sobra peça, cai | `[OUTPUT]` explícito evita o modelo "adivinhar" o formato |
| **Engenharia de loops / agent loop** | gerar→verificar→repetir até um critério; o FI é a teoria de qualidade do loop | o loop é o motor; o FI é a teoria de qualidade do motor | ▸ aprofundamento (só se houver praticantes de loop) |
| **Lost-in-the-Middle** (Liu 2023) | modelos degradam no miolo de contextos longos | numa lista longa, você esquece o do meio | motiva a densidade posicional (em aberto) |
| **Programa de pesquisa (núcleo/cinturão/borda)** | Lakatos: núcleo protegido, cinturão revisável, borda viva | o castelo (núcleo), a muralha (cinturão), o canteiro de obras (borda) | a moldura da honestidade epistêmica da aula |

---

# CONCEITOS DE MÉTODO/EPISTEMOLOGIA (núcleo da postura)

| Conceito | Def + Feynman | No programa |
|---|---|---|
| **Programa de pesquisa (Lakatos)** | um programa não é uma tese só; tem núcleo que se protege, cinturão que se revisa, borda onde se trabalha. Feynman: o cientista não joga fora a teoria por um experimento ruim — protege o núcleo, revisa a periferia | torna honesto dizer "isto não se sustentou nas premissas" sem "fracassou" |
| **Invariância à arquitetura** | a lei do ofício não depende do Transformer; vale para RNN-com-cache, o que vier. Feynman: a regra de carpintaria não muda se a madeira é pinho ou carvalho | a tese ampla do Artesanato Digital |
| **Inteligência híbrida / simbiose** | humano + IA produzem força que nenhum tem sozinho (Margulis/simbiogênese; Licklider 1960). Feynman: o líquen — fungo + alga viram um organismo que nenhum dos dois seria | o telos do programa |

---

# NOTAS DE VERIFICAÇÃO

**RESOLVIDAS (2026-06-27):**
1. ✅ **CodePrompt × CMP:** mantém **CodePrompt**; CMP fica de fora por ora.
2. ✅ **Rótulo dsc:** **cultural** (fiel ao arquivo EN "Cultural Semiotic Density"). "Conceitual" era lapso — corrigido.
3. ✅ **Operações SDE:** **5 operações** (densify/rarefy/rotate/subtract/blend); **Poda Sintática é instrumento separado (nº2)**, não operação SDE. **Pendência de propagação:** o Painel (L1E/L11bis) hoje sugere 6 — alinhar para 5 ao montar o deck.

**PENDENTE (decisão sua):**
4. **Agent-First:** universal ou só-código (cinturão)? Hoje tratado como cinturão (▸ aprofundamento, pulável para plateia não-técnica). Confirmar se quer assim ou se Agent-First é instrumento universal.
