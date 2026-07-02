---
audience: praticantes_avancados_IA — Academia Lendária, Hub São Paulo
content_type: corpo_completo_aula
programa: Framework Injection — aplicação canônica
duracao: Painel 60min + Workshop 90min
metodologia: XP_6_fundamentos + Liberating_Structures + Técnica_Feynman + AIP(FI/SDE/ATP)
ferramentas: [Prompt-Forge v2, skills /forja /lapidacao /fig, idea-forge-pro]
autor: Renato Aparecido Gomes
gerada_por: aula-forge v1.0
version: 1.5
---

# AULA — Framework Injection: Pare de Comandar IA, Comece a Educá-la
## Painel estratégico (60 min) + Workshop mão-na-massa (90 min) — Academia Lendária / Hub SP

> **Frase-âncora da aula (abre e fecha cada encontro):**
> *"A qualidade do output de IA não é proporcional à qualidade do comando. É proporcional à qualidade do método de raciocínio que você transfere. Comando é pidgin. Framework é língua plena."*

> **Princípio-guia (lente declarada do autor, não dogma):**
> *"Engenharia de prompt é o pidgin digital. Framework Injection é a língua plena — e a língua plena não é um prompt melhor: é a oitava interna do harness, o ponto onde a indução linguística pode escalar até virar constrangimento físico."*

---

## 0. SUMÁRIO EXECUTIVO PARA O FACILITADOR (leia primeiro)

### 0.1 A aposta da aula
99% das aulas de "prompt avançado" para um público técnico caem em dois clichês:
1. **"Aqui estão 50 super-prompts"** — ensina cliques, não método. Obsoleto em 3 meses.
2. **"Seja específico e dê contexto"** — verdade rasa que esse público já sabe e já está cansado de ouvir.

**Esta aula faz o oposto, e é nisso que mora o efeito UAU para um público da Academia Lendária:** ela trata a interação humano-IA como um **problema de linguística e de engenharia de sistemas**, não de redação. O praticante sai com **três certezas contraintuitivas que quase ninguém no mercado articula:**

- **Prompt, contexto e FI não são uma escada — são camadas aninhadas dentro do harness.** A "evolução prompt→contexto→FI" é genealogia (verdadeira), não topologia (falsa). O FI é a *única* camada que toca os dois extremos: é feita de linguagem **e** convoca infraestrutura.
- **A fronteira que importa não é "prompt vs código" — é `priming` (induz, o modelo pode ignorar) vs `enforcement` (constrange, o sistema obriga).** FI é a ponte onde a indução escala até virar constrangimento.
- **Dá pra MEDIR o ganho — e a honestidade científica é parte da prova.** Mostraremos dados reais (n=49): FI escrito à mão = 0% de vitórias; FI forjado pela stack estruturada = 88%. E mostraremos onde a hipótese forte **falhou** (a stack barata não reproduz os 88%). Para esse público, admitir o que não funcionou é o que torna crível o que funciona.

A ferramenta que encarna isso é o **Prompt-Forge** (a skill do autor que transmuta prompt cru em FI denso). As skills `/forja` e `/lapidacao` encarnam a **têmpera adversarial** (o enforcement linguístico). No fim, **cada aluno forja um FI do próprio domínio e o tempera** — leva a ferramenta no bolso.

### 0.1.bis Eixo conceitual (a espinha)
- **Princípio-guia (o porquê):** comandar IA é falar pidgin; educá-la via framework é falar a língua plena. *(Paper-mãe: "De Comandos a Cognição", Gomes 2026.)*
- **A virada (antes→agora):** "antes eu pensava que prompt bom é **comando bem-escrito** → agora penso que prompt bom é **método de raciocínio transferido + enforcement que o convoca**".
- **Fundamento operável (não definição):** o **mapa das 4 engenharias aninhadas** (Harness ⊃ FI-ponte ⊃ {Contexto, Prompt}) + o critério binário **priming vs enforcement** aplicável a qualquer linha de qualquer prompt. O aluno sai sabendo *classificar* cada cláusula, não só admirá-las.
- **Honestidade epistêmica (enquadramento lakatosiano — diga isto à turma):** isto é um **programa de pesquisa em andamento**, não um produto fechado. Tem um **núcleo duro** — "use já, está provado o bastante": o aninhamento `prompt⊂contexto⊂harness⊂orquestração`; densificar funciona (+140%, n=435); a ponte priming↔enforcement existe; **e, até aqui, o FI se mostrou robusto à posição das âncoras** (três experimentos: nas premissas adotadas, a hipótese nula não foi rejeitada — o que se observou aponta robustez, mas o ponto segue em aberto). E tem um **cinturão protetor** — "fronteira aberta, ainda investigando": qual modelo forja bem (só Opus testado), a dose ótima de densidade (Adaptive FI deu H0), e o lost-in-the-middle no regime de *prompt grande* (8k+, ainda não testado — onde a teoria deve morder). *Separar os dois é o que dá os dois públicos: o cientista respeita a honestidade, o pragmático leva o que já funciona hoje.* "Em construção" não é desculpa — é o núcleo sólido entregue COM a fronteira honesta declarada.

- **A competência-assinatura que o aluno leva (não trivial, mesmo para quem já faz prompt):** classificar cada cláusula do próprio prompt como **priming** (induz — o modelo pode ignorar) vs **enforcement** (constrange — o sistema obriga), e **deliberadamente mover o máximo de priming para enforcement**. Um bom engenheiro *intui* que "pedir verificação ajuda". O que ele NÃO faz por instinto é escrever `assert: test -f X` sabendo *por que* a primeira forma é tendência e a segunda é garantia. Intuir ≠ dominar a técnica. Esta distinção é, ela mesma, uma previsão falsificável: *prompts com razão enforcement/priming mais alta produzem output mais estável (menor variância)* — e isso o engenheiro instintivo não otimiza porque não tem o conceito.

### 0.1.ter 🎚️ Caminho mínimo de ferramentas (anti-sobrecarga — Sweller)
- **Núcleo irredutível (2 ferramentas):** **Prompt-Forge** (gera o FI) + **`/forja`** (tempera o FI). Com esses dois, o aluno faz o ciclo inteiro: cru → FI denso → FI temperado.
- **Enriquecimento opcional:** `/lapidacao` (17 operações de refino), `/fig` (pipeline FIG completo), `idea-forge-pro` (se o domínio do aluno pedir geração criativa medível). Demonstráveis pelo facilitador; não obrigatórios por aluno.

### 0.1.quater O arco entre os dois encontros
```
ENCONTRO 1 (Painel, 60min)                ENCONTRO 2 (Workshop, 90min)
"Por que seu prompt rende 30%"      →     "Agora você forja e tempera o seu"
──────────────────────────────────       ──────────────────────────────────
Instala a TESE:                           Cada aluno:
pidgin → língua plena;                     pega 1 problema do SEU domínio →
FI = ponte priming↔enforcement;            roda o Prompt-Forge (cru→FI denso) →
A/B ao vivo evidencia o salto              tempera com /forja (martelo adversarial) →
                                           sai com FI + a métrica bridge_width
```

---

# PARTE I — ENCONTRO 1: PAINEL (60 minutos)
## "Por que sua IA rende 30% — e como educá-la para render como expert"

> **Formato:** painel com o Renato + demos ao vivo + perguntas. Público técnico — *não* subestime, mas *não* assuma que conhecem FI.
> **Objetivo epistêmico:** mover o praticante de *"prompt é redação de comando"* para *"prompt é transferência de raciocínio dentro de um harness, mensurável e temperável"*.
> **Tom:** Feynman. Toda abstração desce a uma analogia física antes de subir de volta à teoria.

### Mapa de tempo do painel
| Bloco | Tempo | Função | Verify (o aluno consegue…) |
|---|---|---|---|
| 1. O Gancho — o pidgin digital | 0–10 | quebrar a crença "prompt = comando" | …explicar por que 70% da capacidade fica na mesa |
| 2. As camadas aninhadas (cebola, não escada) | 10–22 | instalar `prompt⊂contexto⊂harness⊂orquestração` + onde o FI entra | …ver que cada camada contém a anterior e nomear a ponte que falta |
| 3. A virada de chave: FI é a oitava interna do HARNESS | 22–34 | priming vs enforcement + mapa das 4 engenharias | …classificar qualquer linha como induz/constrange |
| **3.bis. FI opera a engenharia de loops (cinturão, sacrificável)** | **34–38** | mostrar que loop é o motor e FI é a teoria de qualidade; 3 camadas + Q×T | …dizer por que agent loops não superam o FI — eles o convocam |
| **3.5. O nome maior: Artesanato Digital (ofício+princípio+intenção delegada)** | **38–46** | elevar da técnica à tese — o chão humanístico/filosófico | …dizer por que isto não envelhece e o que, no osso, não terceiriza (a intenção) |
| 4. DEMO A/B ao vivo — densidade que se mede | 44–53 | provar o salto empiricamente (+ honestidade) | …ver o DS subir e a qualidade mudar no mesmo modelo |
| 5. Perguntas | 53–60 | interação | — |

> **⚠️ Gestão de tempo (o Bloco 3.5 é novo e denso — 8 min é apertado):** se o relógio apertar, o 3.5 tem um **núcleo irredutível** (3.5.1 as duas dimensões + 3.5.4 a intenção delegada + 3.5.5 o fecho) e um **cinturão** (3.5.2 as três imagens podem ser reduzidas a só Michelangelo; 3.5.3 a lei invariante pode virar uma frase). Núcleo ≈ 4 min; completo ≈ 8 min. A honestidade ao filósofo (caixa ⚠️ em 3.5.4) só é necessária se houver alguém atacando a intencionalidade — senão, pule. **Nunca corte a intenção delegada (3.5.4): é o clímax conceitual da aula.**

---

### BLOCO 1 — O GANCHO: O PIDGIN DIGITAL (0–10 min)

**Abertura — declaração de honestidade + frame (faça ANTES de qualquer claim — isto é prebuttal: remove a arma do cético antes de ele sacá-la):**
> "Antes de começar, um contrato de honestidade com vocês. **O que eu vou mostrar não é um produto fechado nem uma verdade final — é o estado atual de uma investigação em andamento.** Eu estudo um fenômeno: como a *linguagem* media a relação entre humano e máquina, e como melhorá-la para construir o que venho chamando de **inteligência híbrida** — a soma da inteligência humana com a artificial, não a substituição de uma pela outra. Vou trazer o que já está sólido o bastante para vocês usarem amanhã, **e** o que eu ainda não sei, inclusive hipóteses minhas que eu testei e que falharam. Se em algum momento parecer vendedor de mágica, me interrompam — porque a única coisa que estou vendendo aqui é um método de pensar junto com a máquina, com as evidências que tenho até hoje."

> **Por que abrir assim (nota ao facilitador):** este público sabe falsificar. Se você *declara* a pesquisa-em-curso e as limitações como ponto de partida, o cético não pode te "pegar" admitindo-as depois — você já as pôs na mesa. É refutação antecipada (*prebuttal*). E o frame "inteligência híbrida" eleva o tema de "técnica de prompt" para "como humano e máquina pensam juntos" — que é o que compra a atenção desta sala.

**Abertura provocativa (agora sim, o gancho — fale, não mostre slide):**
> "Vocês estão falando com a ferramenta cognitiva mais sofisticada já criada — e falando com ela como quem pede café num aeroporto estrangeiro: 'resume isso', 'melhora esse texto', 'faz uma lista'. Apontando. Gesticulando. Usando 30% das palavras que a língua oferece. Isso tem nome: **pidgin digital**."

**A analogia-âncora (Feynman):**
> "Pidgin é a língua de contato que surge quando dois grupos sem língua comum precisam negociar no porto. Funciona pra comércio básico. Mas reparem: **nenhuma civilização jamais produziu filosofia, jurisprudência ou ciência num pidgin.** Nenhuma. E é nesse registro que a humanidade está falando com LLMs desde 2022. Não é problema de tecnologia. É problema de linguagem."

**Aha moment #1:**
> "A engenharia de prompt padrão explora menos de 30% da capacidade demonstrada de um LLM. Trinta por cento. É exatamente a limitação funcional de um pidgin em relação à língua-mãe. O modelo não é fraco. **Você está falando errado com ele.**"

**O frame-mãe da aula — por que se chama Artesanato Digital (estabeleça aqui, volta no workshop):**
> "Conta-se que perguntaram a Michelangelo como ele fez o Davi. Ele teria dito: *o Davi já estava dentro do bloco de mármore — eu só tirei o que sobrava.* [pausa] É exatamente isto que vocês vão fazer com a IA. A IA é o cinzel — ela tira as lascas com uma força que vocês não têm nas mãos. Mas **quem enxerga a estátua dentro do bloco é o artífice** — o mestre artesão em ato. Quem escolhe *qual* rocha, quem decide *o que* aquele bloco vai virar, quem vê a Pietà na pedra bruta e a pintura na tela em branco — isso é humano. E é a coisa mais difícil do processo inteiro."

> "Por isso o nome do programa é **Artesanato Digital**, não 'engenharia de prompt'. A IA executa a técnica; o humano carrega a *visão* e o *julgamento*. Tem até um nome teórico para isso — o **Paradoxo do Artesão**: se a IA é tão boa em aplicar método, por que ela não cria o próprio método? Porque criar o método exige ver a estátua no bloco — conhecimento *tácito*, corporificado, que a gente sabe mas não consegue dizer inteiro (Polanyi: *'sabemos mais do que podemos dizer'*). O framework é a externalização possível desse tácito. A IA opera dentro dele com facilidade sobre-humana — mas não o gera, porque não vê a estátua. **Vocês veem. Essa é a parte de vocês que não terceiriza.**"

**Declaração honesta do princípio-guia (faça aqui):**
> "A lente que vou usar hoje é minha, e é uma entre outras: **comandar IA é falar pidgin; educá-la com um framework é falar a língua plena.** Não é a única verdade sobre prompts — mas é a que faz a IA sair de 30% para nível expert. Topam percorrer comigo?"

---

### BLOCO 2 — A ESCADA QUE VIROU CEBOLA: CAMADAS ANINHADAS, NÃO ERAS (10–22 min)

> O fundamento que o público precisa, em analogia Feynman antes de teoria. **Atenção de design (importante para a longevidade da aula):** este bloco NÃO ensina "3 eras fixas". Ensina um *princípio de aninhamento* que sobrevive à próxima renomeação do campo — e o campo renomeia a si mesmo rápido (ver 2.0).

**2.0 — O aviso que torna a aula à prova de moda (diga isto antes de qualquer rótulo):**
> "Vou dar nomes às camadas daqui a pouco — mas primeiro uma vacina, porque este campo é uma feira de nomes. Reparem no ritmo: a disciplina central de construir com IA **foi rebatizada três vezes em três anos.** 'Engenharia de prompt' (2022) → 'engenharia de contexto' (Karpathy, 2025) → 'engenharia de harness' (Hashimoto, 2026). E já tem nome para a próxima camada — Karpathy chamou de **'engenharia agêntica'** no Sequoia Ascent deste ano: *'a disciplina de orquestrar agentes falíveis e estocásticos com o humano no comando'*. Tem quem fale em 'engenharia de loops', tem fornecedor que cunha o próprio termo ('Agentic Enterprise Orchestration', da OutSystems). **Não decorem os nomes — eles vão mudar de novo.** Decorem a *estrutura* por baixo deles, que não muda: **cada camada nova não substitui a anterior — ela a contém.** É o que vou mostrar agora. *Eu não vou casar esta aula com nenhum rótulo de moda; vou ancorá-la no que é invariante.*"

**2.1 — As camadas aninhadas (desenhe no quadro — não como linha do tempo, como cebola):**

| Camada | O que controla | Metáfora Feynman | "Não é cozinhar, é…" |
|---|---|---|---|
| **Prompt** (palavras) | a *instrução* de uma interação | a **receita** | "…seguir instruções" |
| **Contexto** (conhecimento) | o que o modelo *vê* na janela | a **cozinha** equipada | "…ter uma despensa cheia" |
| **Harness / Loops** (execução) | o que o sistema *previne, mede, repara* fora da janela | a **brigada e a linha de produção** da cozinha | "…ter cozinha que se autocorrige" |
| **Orquestração agêntica** (o todo) | coordenar agentes falíveis com humano no comando | o **chef de cuisine** que rege a brigada | "…reger uma cozinha inteira" |

> **A relação que muda tudo (escreva grande — é o invariante, não a lista):** `prompt ⊂ contexto ⊂ harness ⊂ orquestração`
> "Não é uma escada onde cada degrau *substitui* o anterior — é uma **cebola**: cada camada *contém* a de dentro. Quem teoriza harness diz a mesma coisa: *'engenharia de harness contém engenharia de contexto, que contém engenharia de prompt'*. A indústria concorda nisso. **Toda técnica boa de prompt é um caso particular de uma camada externa mal-aproveitada.**"

**2.1.bis — E onde entra o Framework Injection? (a pergunta que o público técnico vai fazer — responda já, antecipando o Bloco 3):**
> "Vocês vão perguntar: 'se já existe essa cebola toda, qual o lugar do seu FI?'. Resposta curta — e é a tese da aula inteira: **todas essas camadas vivem em dois mundos que ninguém costura.** O prompt e o contexto são *linguagem* (induzem o modelo). O harness e os loops são *infraestrutura* (constrangem o sistema). Repare no mapa de quem teoriza harness: eles operam no **runtime, no constrangimento físico** — e admitem, em uníssono, que **ninguém descreve a ponte entre a linguagem e a infraestrutura.** Esse buraco tem nome aqui: é onde o **Framework Injection** mora. O FI é a única camada feita de *linguagem* que *convoca infraestrutura* — a ponte onde induzir vira constranger. Os nomes da feira (harness, agêntica, loops) descrevem os dois lados da margem; o FI descreve a *travessia*. É por isso que esta aula não é 'mais um nome' — ela nomeia o que os outros nomes pressupõem e não tocam. *(Detalho no Bloco 3.)*"

> **⚠️ Honestidade de enquadramento (diga, fecha o flanco do cético-de-nomes):** "Sendo justo: 'Framework Injection' também é um nome, e eu também posso estar surfando a mesma feira que critiquei. A diferença que eu reivindico — e vocês vão julgar — é que os outros nomes marcam *territórios* (onde a engenharia mora); o FI marca uma *transição* (priming→enforcement) que é **mensurável** e que eu trago dado para sustentar. Nome marca lugar; o que eu trago é um *mecanismo*. Se no fim parecer só rótulo novo, me cobrem no Bloco 4, que é onde tem número."

**2.2 — Concreto (Feynman: o exemplo do analista de risco):**
> "Imaginem que vocês precisam de uma análise de risco financeiro.
> - **Comando (PE):** 'analise o risco da empresa X.' → genérico, dados inventados, sem método.
> - **Contexto (CE):** mesma coisa + balanço + 3 anos de demonstrativos. → melhor, mas o modelo decide *sozinho* COMO analisar.
> - **Framework (FI):** 'você é analista de risco que aplica: (1) liquidez via current/quick ratio com thresholds do setor; (2) alavancagem via debt-to-equity; (3) stress-test em 3 cenários; (4) hierarquia de fontes: balanço > auditado > benchmark > estimativa; (5) em dado conflitante, cite a discrepância, não resolva; (6) red line: nunca recomendar investimento.' → análise com método, rastreabilidade e governança."
>
> "A diferença não é quanta informação você deu. É que no terceiro você **transferiu o raciocínio de um expert.** Não é dar mais dado. É ensinar a pensar."

**Aha moment #2:**
> "Os 5 tipos de framework que vocês vão injetar: **Declarativo** (o que saber), **Procedimental** (como raciocinar), **Avaliativo** (como julgar), **Ético** (o que recusar), **Composicional** (como combinar). Um FI maduro tem os cinco, hierarquizados: o ético restringe o avaliativo, que restringe o procedimental, que opera sobre o declarativo, tudo orquestrado pelo composicional."

---

### BLOCO 3 — A VIRADA DE CHAVE: FI É A OITAVA INTERNA DO HARNESS (22–38 min)

> O coração intelectual da aula — e o que diferencia esta aula de qualquer conteúdo de "prompt avançado" lá fora. Aqui o público técnico ganha o modelo mental que o mainstream de harness engineering *pressupõe mas não teoriza*.

**3.1 — Aprofundando a camada de harness que vocês já conhecem (ancore na autoridade deles):**
> "No Bloco 2 eu disse que harness/loops é a camada que constrange. Agora o dado que mostra *o quanto* ela domina: estudo Stanford/Tsinghua — **mesmo modelo, harness diferente, até 6× de variação de output.** Berkeley: 'o próximo gargalo é escalar o sistema, não o modelo.' É por isso que a indústria migrou de 'prompt' para 'harness' e agora para 'orquestração agêntica' em três anos — todos perceberam que a estrutura externa domina o resultado. Mas reparem no que já adiantei e agora aprofundo: **todos esses nomes operam no runtime, no enforcement físico. Nenhum descreve a ponte entre a linguagem e a infraestrutura.** Esse é o buraco que o FI preenche — e é o que nenhum termo da feira nomeia, porque todos eles marcam *lados da margem*, não a *travessia*."

**3.2 — A fronteira que reorganiza tudo (o insight, Feynman):**
> "Todo mundo acha que a divisão importante é 'prompt (linguagem) vs código (sistema)'. Está errado. Essa é divisão de *endereço* — onde a coisa mora. A divisão de *natureza* é outra:"

| | **Priming (indução)** | **Enforcement (constrangimento)** |
|---|---|---|
| Mecanismo | predispõe, enquadra, densifica | bloqueia, executa, verifica |
| O agente pode desobedecer? | **Sim**, em princípio | **Não** |
| Mora tipicamente em | o texto do FI | o runtime do harness |
| Exemplo | "antes de responder, identifique a suposição crítica" (o modelo *deveria*) | um gate que reprova a resposta se a prova programática falha (o sistema *obriga*) |

> **Analogia Feynman:** "Priming é o **técnico gritando a tática do banco** — o jogador pode ignorar. Enforcement é a **linha de impedimento marcada pelo bandeirinha** — não tem como driblar. Um prompt comum é só grito. Um harness é só linha. **O FI é o lugar onde o grito do técnico pode, no limite, virar regra do jogo.**"

**3.3 — O mapa das 4 engenharias aninhadas (desenhe — é o fundamento operável):**
```
┌────────── HARNESS ENGINEERING (infra: enforcement, runtime, loops) ──────────┐
│   [IMI · Prompt-Forge · forja · gates · loop de controle]                     │
│                          │  ▲                                                  │
│              (materializa)│ │(convoca)                                         │
│                          ▼  │                                                  │
│   ┌──────────── FRAMEWORK INJECTION (a ponte) ────────────────────────────┐   │
│   │ densifica instrução (priming) + pode escalar até enforcement           │   │
│   │ ↓ via descendente: infra vira texto · ↑ via ascendente: texto convoca infra │
│   └───────────┬──────────────────────────────────────────┬─────────────────┘  │
│               ▼                                            ▼                    │
│      Eng. de CONTEXTO (semântica: o que entra)   Eng. de PROMPT (sintaxe: as palavras) │
└───────────────────────────────────────────────────────────────────────────────┘
```
> "Lê-se assim: prompt e contexto são organizados *por dentro* do FI. O FI é a ponte. O harness envolve tudo e fornece o enforcement. **O FI é a única camada que toca os dois extremos** — é feita de linguagem e convoca infraestrutura. Por isso é ponte, não degrau."

**3.4 — As duas vias da ponte (o que a torna bidirecional):**
> "**Via descendente (infra→linguagem):** o Prompt-Forge é *código* que materializa um FI de *texto*; o IMI injeta memória no substrato linguístico. A infraestrutura 'se fala'.
> **Via ascendente (linguagem→infra):** quando vocês escrevem `[VERIFICAÇÃO]` num FI, isso é uma *instrução para a infra agir* — no limite, dispara um gate executável que reprova a resposta. O texto 'convoca' o enforcement.
> As duas vias coexistindo são a assinatura de uma ponte."

**Aha moment #3 (o grande, para este público):**
> "Engenharia de loops, priming, enforcement — vocês já operam isso no nível de sistema: o loop que re-roda, o contexto que entra, o assert que valida a saída. **O que o FI faz é a MESMA música numa oitava acima: priming vira o prime cognitivo dentro de UMA inferência; enforcement vira a cláusula `[VERIFICAÇÃO]` que pode escalar para um gate; o loop vira a têmpera adversarial — forja, martela, recoze.** Vocês não vão aprender uma técnica nova de prompt. Vão aprender a *projetar a interpretação* do modelo — engenharia de interpretante, não de signo."

---

### BLOCO 3.bis — FI OPERA A "ENGENHARIA DE LOOPS": A TEORIA DE QUALIDADE QUE O LOOP NÃO TEM (atualização de pesquisa — encaixe após o Bloco 3, antes do 3.5)

> **Gestão de tempo:** este bloco é um **cinturão de 4 min** acoplado ao Bloco 3. Se o relógio apertar, ele é sacrificável SEM perder o clímax do painel (que é o 3.5, intenção delegada). Mas se a plateia for de praticantes de agent loops — provável neste Hub — ele é o bloco que impede a pergunta "isso não foi superado?" de derrubar a aula. Núcleo irredutível: 3.6.1 (o enquadramento) + Aha #3.bis (o gráfico Q×T). O resto (3 camadas, 4 achados) enriquece.

> **Por que este bloco existe (nota ao facilitador):** "engenharia de loops" / "agent loops" virou o termo da vez desta plateia (vídeos do Steinberger, Ronnald Hawk etc. — substituir prompt por um agente que *itera até um critério de parada*). O risco é o público achar que o FI é um *concorrente* desse movimento, ou já obsoleto frente a ele. **É o oposto, e esta é a tese mais recente da pesquisa:** o loop é o *motor*; o FI é a *teoria de qualidade do motor*. Bloco curto e cirúrgico — 4 min — fecha o flanco "isso não foi superado por agent loops?".

**3.6.1 — O enquadramento que desarma a confusão (diga direto):**
> "Vocês vão ouvir muito 'pare de fazer prompt, faça um loop: deixe o agente gerar, verificar e repetir até passar'. Está certíssimo — onde há **reward objetivo** (o teste fica verde, o build compila), o loop resolve sozinho. Mas reparem **onde ele falha, de forma confiante e perigosa:** onde NÃO há reward barato — direito, medicina, texto, estratégia. Ali o critério de parada é o próprio modelo (ou um júri de modelos), e o modelo mede **plausibilidade, não correção.** O loop não tem, por si, uma teoria do que é *qualidade*. **O FI é exatamente essa teoria.** O loop é o motor; o FI é o que diz ao motor o que é 'bom'."

**3.6.2 — FI age ANTES; o loop age EM TORNO (a relação, em uma imagem):**
> "Não competem porque agem em *tempos* diferentes. **O FI age ANTES da inferência** — configura o espaço de raciocínio (papel, método, fontes, verificação). **O loop age EM TORNO** — orquestra as repetições até a parada. E é aqui o ponto: **o FI denso vai DENTRO de cada iteração do loop.** Toda volta do loop é uma inferência; e toda inferência fica melhor com o método injetado. Eles se aninham, não se substituem."

**3.6.3 — As 3 camadas (refina a ponte do Bloco 3 — agora com a terceira):**
> "No Bloco 3 eu dei duas naturezas: priming e enforcement. A pesquisa recente me obrigou a admitir uma terceira, e ela é a que salva o loop de se enganar:
> - **Priming (induz, pode errar junto):** a geração e o *júri* de modelos. Mede **forma** — clareza, completude. Falível em conjunto.
> - **Enforcement (constrange, não desobedece):** o *assert externo* contra uma fonte primária **não-LLM** — a lei, o teste, o sensor, a API. Decide **verdade**.
> - **Têmpera (anti-degradação):** entregar o **pico**, não a última rodada; parar na regressão; escalar ao humano no impasse.
> **A regra de ouro, e o erro que quase todo mundo comete:** deixar o LLM julgar *verdade* mistura priming com enforcement numa camada só — e é isso que produz o **erro confiante**. Mantê-los separados é o blueprint."

**3.6.4 — Os achados que provam isto (dados frescos — para o cético, vale ouro):**
> "E não é teoria de poltrona. Quatro achados, todos medidos:
> 1. **Convergência ≠ correção:** um júri de modelos deu nota 9–10 a uma subsunção jurídica *errada* — em 3 casos independentes. Consenso alto, resposta errada.
> 2. **O júri é cego por tipo de erro:** ele pega o argumento vago; **não pega** a citação de lei que não existe — justamente o erro mais plausível e mais perigoso.
> 3. **Mais modelos têm teto:** o painel (0.94) supera o solo (0.88), mas o falso-positivo de corpus compartilhado passou pelos três.
> 4. **Iterar nem sempre melhora:** sob critério severo, repetir *piorou* 4 de 5 casos. Por isso a têmpera entrega o pico, não a última volta.
> **Conclusão honesta:** o agent loop, sozinho, em domínio sem-reward, é uma máquina de erro confiante. Com o FI dando a rubrica e o assert externo travando a verdade, ele vira engenharia."

**Aha moment #3.bis (o fecho — o gráfico que une os dois mundos):**
> "Imaginem dois eixos: **qualidade (Q)** e **tentativas (T)**. A engenharia de loops melhora a qualidade gastando **tentativas** — força bruta, itera mais. O FI melhora a qualidade gastando **densidade** — acerta com menos voltas. **São os dois eixos do mesmo gráfico.** Quem só tem loop paga em GPU e tempo. Quem injeta FI denso em cada volta sobe no eixo Q com menos T. Não é loop *vs* FI. É loop *com* FI — e é aí que a fronteira está se movendo agora."

> **⚠️ Honestidade de domínio (declare — anti-overclaim):** "Sendo justo com o movimento de loops: onde existe reward objetivo e barato, o loop puro basta e o FI é overhead. A composição que defendo brilha no território *oposto* — o tácito sem reward, que é onde eu trabalho (direito, medicina, auditoria). São domínios de validade quase disjuntos. Eu não estou dizendo 'FI vence loop'; estou dizendo 'loop sem teoria de qualidade se engana onde mais importa, e o FI é a teoria que falta'."

---

### BLOCO 3.5 — O NOME MAIOR: ARTESANATO DIGITAL — O OFÍCIO E O PRINCÍPIO (fechamento conceitual do painel)

> O momento de elevar da técnica à tese — da ferramenta à lei. A ponte priming→enforcement já está montada; agora ela ganha um chão filosófico. *(Tom: mais lento, mais grave. É o coração humanístico da aula.)*

**3.5.1 — As duas dimensões:**
> "Tudo o que vimos tem um nome maior: **Artesanato Digital**. E ele tem duas dimensões — uma que vocês **fazem**, outra que vocês **são**. A primeira é o **ofício**: densificar, temperar, transferir método — o que vocês levam no bolso. A segunda é mais funda, e é o que torna a primeira durável: o **princípio**. Vou dizer direto: **o Artesanato Digital não é a IA trabalhando por você. É você dispondo a matéria para que a IA trabalhe bem.**"

**3.5.2 — As três imagens (da mais antiga à de agora — desça à analogia):**
> - **O escultor:** "Michelangelo não *empurrou* o Davi para dentro do mármore. Leu a pedra e tirou o que sobrava. *Dispor a matéria → deixar a forma emergir.*"
> - **O cozinheiro de Zhuangzi** (taoísmo, 2.300 anos): "cortava um boi inteiro e a faca nunca cegava — não *forçava* o osso, deixava a lâmina achar os vazios entre as juntas. Dezenove anos, a mesma faca afiada. *Não cortava contra a matéria; fluía pelo vazio que já estava nela.*"
> - **Vocês, com a IA, hoje:** "quando param de mandar 'analisa esse contrato' e passam a *dispor o método* — 'aplique esta hierarquia de fontes, sinalize a nulidade, não resolva o conflito, aponte-o' —, não comandam mais forte: **dispõem os vazios certos para a inteligência dela fluir sem cegar.** Isso é priming virando enforcement. Isso é o gesto."

**3.5.3 — A lei invariante (o que torna isto à prova de moda — conecta ao Bloco 2):**
> "As três imagens são a *mesma lei*, com matérias diferentes — mármore, boi, modelo. **A matéria muda; a lei não.** Hoje vocês dispõem um transformer; amanhã, outra arquitetura — RNNs com memória, o que vier —, a *ferramenta* muda, mas o gesto de *dispor o vazio para a forma emergir* permanece. **Quem aprende a ferramenta corre atrás da próxima para sempre. Quem aprende a lei domina todas — inclusive as que ainda não existem.**"

**3.5.4 — A camada-raiz: a intenção delegada (o que, no osso, não terceiriza):**
> "E se me perguntarem *qual* é, no fundo, a parte que não terceiriza, eu dou o nome exato: é a **intenção**. Reparem — **a IA executa, mas não pretende nada.** Não quer um fim, não tem um 'para-quê' que seja dela. Tem um filósofo, John Searle, que separou duas coisas: a intenção *original* (que mentes vivas têm por si) e a intenção *derivada* (que objetos têm emprestada — o mapa só é 'sobre' o território porque alguém o fez assim). **A IA só tem a derivada.** Toda intenção que parece haver no que ela faz foi **delegada por vocês** — está no método que injetam, no que pedem, no que julgam que está bom. É o que eu chamo de **intenção delegada**: o priming é o ato de *delegar* a vossa intenção ao substrato; o enforcement é essa intenção delegada virando mundo. Cortem o framework de vocês e a máquina não fica com 'a intenção dela' — fica sem nenhuma, porque nunca teve uma própria. **Ver, julgar e responder são três faces de uma só coisa: a intenção. E a intenção é vossa.**"

> **⚠️ Honestidade (para o filósofo cético da sala — declare):** "Sejamos precisos: alguém vai dizer que a IA *tem* intencionalidade no sentido de que seu texto é *sobre* coisas. No sentido fraco — a aboutness derivada — tem, sim. O que ela não tem é a intenção *original*: o querer um fim que seja dela. Um agente de IA que gera sub-metas não está originando intenção; está **propagando a vossa** pela cadeia. A fonte é sempre humana. *(Esta é a aplicação da distinção de Searle à IA generativa — fundamentada, e é onde a tese se sustenta.)*"

**3.5.5 — O fecho (a máxima, com a concordância no singular distributivo):**
> "Por isso: **o modelo é a matéria do século — a mais poderosa que já tivemos nas mãos, mas matéria: sem vontade. O artífice é cada um de vocês — o mestre artesão em ato. E essa parte — ver, julgar, responder, *querer* — não terceiriza.** E aqui está a virada quanto ao medo da substituição: **quanto mais a execução vira commodity, mais a intenção — que não terceiriza — vira o vosso centro de valor.** A IA não rebaixa o artífice; ela o **promove**. *Isto* é a inteligência híbrida — a fusão entre a inteligência humana e a artificial, com a intenção do lado de cá."

> **Nota ao facilitador (vernáculo — coerência do glossário):** ao longo da aula, **"artífice"** = o sujeito-agente na relação com a IA (quem vê, dispõe, julga, assina); **"mestre artesão"** = a mesma figura no registro da tradição/vocação; **"Artesanato Digital"** = o programa. São um sujeito em dois registros. E cuidado com o número: o artífice é figura singular, o público é plural — diga **"o artífice é cada um de vocês"**, nunca "o artífice é vocês".

---

### BLOCO 4 — DEMO A/B AO VIVO: A DENSIDADE QUE SE MEDE (38–50 min)

> O momento que separa esta aula de uma palestra. Para um público técnico cético, a prova empírica fecha o flanco *antes* que eles abram. Faça AO VIVO; tenha fallback gravado.

**4.1 — A demo (Feynman: mostre, não afirme):**
1. Pegue um pedido cru **da plateia** — mas **filtre a tarefa para garantir o salto** (isto é desenho honesto, não trapaça): peça *"me dá uma tarefa do trabalho de vocês que tenha **método de domínio embutido** — algo que um júnior faria mal por não saber o procedimento"*. **Boas tarefas (o delta aparece):** "analise o risco de crédito desta empresa", "revise esta cláusula contratual", "critique a metodologia deste teste". **Tarefas-armadilha (recuse com elegância):** "valida CPF", "ordena uma lista", "escreve um regex de email" — tarefas onde o método cabe numa linha e o modelo frontier já resolve cru, então o Braço A sai bom e a demo não salta. *Se a plateia só oferecer tarefas-armadilha, use o caso-trilho de reserva (4.1.bis).*
2. Rode no **mesmo modelo de execução**, lado a lado:
   - **Braço A — prompt cru:** o pedido como veio.
   - **Braço B — FI forjado:** passe pelo Prompt-Forge ao vivo (ver Bloco 4 do workshop para o fluxo).
3. **Mostre o número — mas DEPOIS de já ter mostrado os dois outputs** (a sequência importa: o olho vê a diferença, *então* o número a nomeia): primeiro os dois textos lado a lado — *"mesmo modelo, mesma pergunta; olhem o que mudou no que ele devolveu"* — e só então `DS: 1.3 → 4.4`, *"e isto é o que mudou no que eu disse: chama-se densidade semiótica, é o quanto cada palavra carrega de método; já volto nela."* (Ver §4.1.ter — não solte "DS" como número órfão.)

**4.1.bis — Caso-trilho de reserva (tenha pré-forjado e testado; fallback do showstopper #1):**
> Tarefa: *"faça uma análise de risco de crédito da empresa X"* (o exemplo do analista do Bloco 2). Braço A cru → o modelo inventa categorias, sem método, sem hierarquia de fonte. Braço B forjado → as 6 cláusulas do analista (liquidez/alavancagem/stress-test/hierarquia de fontes/conflito-não-resolvido/red-line). O delta é grande, visível e **já foi ancorado no Bloco 2** — a plateia reconhece. Use se a demo ao vivo não saltar ou o Forge falhar.

**4.1.ter — Onde "densidade semiótica" é definida (anti-jargão-órfão):** o termo aparece pela primeira vez *aqui*, na demo. Defina-o em uma frase no instante em que o número surge: *"densidade semiótica = quanto de método cada palavra carrega; 'fazer' carrega pouco, 'refatorar' carrega um campo inteiro. O número mede isso."* A definição formal e as 5 operações vêm no workshop (Bloco 2) — aqui basta a intuição de uma frase, senão o número vira jargão vazio.

> **⚙️ Nota técnica do facilitador (honestidade sobre o forjador — não pule):** aponte o Prompt-Forge para um **modelo frontier** (Opus/Sonnet) na hora de *forjar* o FI da demo. O benchmark mostrou que **quem forja importa tanto quanto o método**: forja por modelo médio rende ~6%, forja por frontier rende ~88%. Diga isto à turma com naturalidade: *"o Prompt-Forge é o destilador do método — mas destilar bem ainda pede um bom alambique. Hoje, o forjador forte faz diferença. Isso não é fraqueza da ideia; é a fronteira honesta de onde a engenharia está."* Para um público técnico, admitir isso **aumenta** sua credibilidade — e conecta direto com a seção 4.3.

**4.2 — Os dados reais (dois números, duas histórias — não confunda):**

> **Número 1 — DENSIDADE (n=435, produção real):** "Não é anedota. O Prompt-Forge registrou 435 transmutações reais. A densidade semiótica do prompt cru, em média, é **1.86** (pidgin). Do FI gerado: **4.47** (registro expert). Ganho médio: **+140%**. Consistente em todos os domínios — código, jurídico, pesquisa, financeiro. *Isto mede a densidade do que eu digo — o input do método.*"

> **Número 2 — QUALIDADE DE OUTPUT (n=49, benchmark cego):** "E o output melhora? Rodei 49 tarefas, juízes cegos de 3 famílias de modelo (nenhum Anthropic):"

| Braço | O que é | Vitórias (n=49) | Lê-se como |
|---|---|---|---|
| A — query crua | o pidgin | **2%** | baseline no chão |
| B — FI escrito à mão | priming sem stack | **0%** | FI manual ruim = query crua |
| C — FI do engine simples | stack mínima | 8% | levanta um pouco |
| **D — FI forjado por modelo frontier** | priming completo | **88%** | **domina** |

> **Aha moment #4 (a honestidade metodológica é parte da prova):** "Reparem em B = 0%. Leitura hostil: 'então o método não fez nada; o modelo frontier fez tudo'. Eu poderia esconder esse dado. Não vou. **B=0% não prova que o método falha — prova que escrever um bom FI À MÃO é difícil, do mesmo jeito que escrever bom código à mão é difícil.** O que o modelo frontier fez foi *aplicar o método com competência*. O que o Prompt-Forge faz é *destilar essa competência numa ferramenta*. O método é real; o gargalo é a forja — e é exatamente por isso que a ferramenta existe."

**4.3 — A previsão que SÓ a teoria faz (a prova de que não é prompt engineering renomeado):**
> "Um cético honesto pergunta: 'qual previsão a sua teoria faz que o meu instinto não faria?'. Aqui está uma, contraintuitiva e medida: **a densidade semiótica ajuda MAIS o modelo médio e MENOS o frontier.** Todo mundo esperaria o oposto — 'modelo melhor aproveita melhor o prompt sofisticado'. É o contrário: o frontier já tem o método dentro; quem mais se beneficia de densidade é o modelo médio, que precisa do scaffolding. Isso o instinto não prevê — a teoria prevê, e o dado confirma. *(Corolário prático que volta no workshop: quem roda modelo médio em casa deve carregar peso na densidade.)*"

**4.4 — Onde minhas hipóteses FALHARAM (diga isto — para este público, vale ouro):**
> "Ciência sem isto é marketing. Três honestidades:
> 1. **'A stack barata reproduz os 88%' — testei, deu errado.** Stack com modelo médio rendeu 6%, não 88%. Só o frontier entregou. *(E aqui um caveat importante: testei o forjador só com um frontier — Opus. Codex 5.5, Kimi K2.7, GLM 5.2 são frontiers recentes que eu ainda NÃO testei como forjadores. Então não é 'só um modelo consegue' — é 'só um foi testado'. O espaço é aberto.)*
> 2. **'A dose ótima de densidade tem uma fórmula por nível de modelo' — não se sustentou** (deu não-monotônica). Sei a *direção* (médio → mais densidade), mas a dose exata ainda é arte, não fórmula.
> 3. **A posicionalidade (lost-in-the-middle aplicado ao FI) — eu persegui esse efeito até o fim, e o achado é mais interessante que um 'deu certo':** rodei **três experimentos independentes** com teste estatístico formal (binomial exato, IC95% Clopper-Pearson — não olhômetro). Resultado: **nenhum dos três rejeitou a hipótese nula** (p = 0.286, 1.000 e 1.000; todos os intervalos de confiança contêm 0.5). E o mais revelador — quando eu *achei* que tinha visto um efeito pró-borda no primeiro, a análise formal o dissolveu; e o segundo desenho apontou na direção *oposta*. **Registro honesto, sem veredito fechado: no regime de FI de produção (~1k tokens) e nas premissas que adotei, não detectei efeito da posição das âncoras — o ponto fica em aberto.** Agora reparem o que isso *sugere*, porque não é uma derrota: **o que se observou até aqui aponta para um FI bem-forjado aproximadamente posição-invariante — um indício de robustez, não uma conclusão fechada.** O lost-in-the-middle é real na literatura (Liu et al. 2023), mas ele morde em prompts *grandes*; num FI denso e curto, o valor está no **conteúdo** das âncoras (priming/enforcement), **não na geometria** delas. Eu vim caçar um efeito e encontrei uma propriedade melhor: o método não depende de eu acertar a ordem. *(Caveat declarado: não rodei o regime de prompt grande 8k+, onde a teoria deve morder — é experimento novo, não escalar deste. E sim, deixei pronto um harness para n=200 com modelo forte e decidi NÃO disparar: jogar GPU num efeito que três desenhos não detectaram só produziria um número falsamente preciso. Saber a hora de parar também é método.)* (Ver Bloco de posicionalidade no workshop.)
>
> O núcleo da teoria — a ponte priming↔enforcement existe, e densificar funciona (+140%, n=435) — está de pé. O cinturão — qual o mecanismo barato, a dose ótima, o efeito posicional — é fronteira aberta. **Eu trago vocês para onde a pesquisa está de verdade, não para o folheto.**"

---

### BLOCO 5 — PERGUNTAS (50–60 min)

**FAQ preparado (as perguntas-fura mais prováveis deste público — ensaie as respostas):**

**P (a mais letal): "Que previsão a sua TEORIA faz que o meu instinto de prompt-engenheiro não faria?"**
> R: Esta é a pergunta certa, e tenho uma resposta medida: **a densidade ajuda MAIS o modelo médio e MENOS o frontier** — o oposto do que o instinto prevê. Seu instinto diz 'modelo melhor aproveita prompt melhor'; o dado diz o contrário. E uma segunda: **prompts com razão enforcement/priming mais alta produzem output mais estável (menor variância)** — você otimiza qualidade média por instinto, mas não otimiza *estabilidade*, porque não tem o conceito de priming vs enforcement separados. Essas são previsões falsificáveis que a teoria faz e o instinto não.

**P: "Seu próprio dado diz que o FI-humano rendeu 0%. Então o ganho não é do modelo, não da teoria?"**
> R: B=0% prova que escrever bom FI *à mão* é difícil — como escrever bom código à mão é difícil. Não prova que o método falha; prova que ele precisa de competência de forja. O frontier aplicou o método com competência; a ferramenta destila essa competência. *(E sendo honesto: testei a forja só com Opus — Codex 5.5, Kimi K2.7, GLM 5.2 ainda não. O espaço de bons forjadores é aberto, não fechado em um modelo.)*

**P (a evolução letal da anterior — ENSAIE, é a que derruba a aula): "Então o seu produto, no fim, é 'pague um modelo frontier'. O método é decoração; o que rende é o modelo caro. Por que eu preciso de você?"**
> R (CONCEDA primeiro — não defenda em círculo): "Em parte você tem razão, e eu não vou fingir que não: **hoje, sem um bom forjador, o método rende menos.** Concedido. Mas repare no que isso *não* implica. Primeiro: o modelo frontier sozinho, recebendo o prompt cru (Braço A), rendeu **2%** — o mesmo modelo caro, sem método, é quase tão ruim quanto o pidgin. Então não é 'o modelo faz tudo': é *o modelo aplicando o método* que faz. Segundo: a competência de forja não é mística — ela está **destilada num pipeline determinístico** que você roda sem ser eu. Você não está comprando meu cérebro; está comprando um método que virou ferramenta. Terceiro, e é aqui que vira a mesa: **a previsão da teoria é que quem mais ganha com densidade é o modelo MÉDIO, não o frontier.** Ou seja — a direção da pesquisa é *exatamente* tornar o método independente do modelo caro. Se eu estivesse vendendo 'pague frontier', eu torceria contra esse achado. Eu torço a favor. O 'pague frontier' é o estado de hoje que eu quero derrubar, não o produto que eu defendo."
> *(Nota ao facilitador: o erro fatal aqui é responder 'a ferramenta destila a competência' e parar — soa circular. A saída é a tríade conceder→2%-do-Braço-A→direção-da-pesquisa. Decore os três movimentos.)*

**P (o pragmático de harness): "Enforcement real no runtime > priming que o modelo pode ignorar. Por que eu usaria a 'oitava interna'?"**
> R: Você está certo — onde você PODE enforçar, enforce. O FI não compete com seu gate; governa o que ele não alcança: o raciocínio *dentro* da inferência, antes de existir saída para o gate checar. E a cláusula ASSERTS é como o FI *alimenta* seu runtime, não como o substitui. São camadas que se costuram, não que competem.

**P: "Isso não é só um system prompt grande?"**
> R: System prompt grande é *volume*. FI é *estrutura* — os 5 tipos hierarquizados + a cláusula que convoca enforcement. O benchmark prova: FI longo e raso (1180 chars) perdeu para FI curto e denso. Não é tamanho, é densidade acionável.

**P: "Onde isso difere de DSPy / context engineering?"**
> R: DSPy otimiza a *mecânica do pipeline* (como o modelo é chamado), não transfere raciocínio de domínio (proximidade 4/10). Context engineering gerencia o que o modelo *vê*; FI determina como ele *pensa*. Biblioteca abastecida vs. metodologia de pesquisa.

**P: "Por que não deixar a IA criar o próprio framework?"**
> R: O Paradoxo do Artesão. Criar framework exige conhecimento *tácito* (Polanyi: "sabemos mais do que podemos dizer") — o framework É a externalização desse tácito. A IA opera dentro do framework com facilidade, mas não gera a externalização porque não tem o tácito. *(Resolução teórica, empiricamente não-fechada — honestidade.)*

**P: "Qual a base teórica? Não é intuição empacotada?"**
> R: Seis tradições independentes convergem: Vygotsky (ZDP — FI é scaffolding), Sweller (carga cognitiva — FI elimina a carga extrínseca), Wittgenstein (jogos de linguagem — FI ensina *qual jogo*), Polanyi (tácito), Peirce (semiótica — FI projeta Terceiridade/interpretante), Greenberg (universais linguísticos). 4 DOIs no Zenodo.

**P (a do filósofo — sobre a "intenção delegada"): "Você diz que a IA não tem intenção, mas o output dela é claramente *sobre* coisas. Isso não é antropomorfizar ao contrário — negar uma intencionalidade que ela demonstra ter?"**
> R: Pergunta exata, e a resposta exige precisão searleana. Há dois sentidos de intencionalidade. **No sentido fraco — a *aboutness*, o texto ser 'sobre' algo — a IA tem, sim**, e eu não nego. **No sentido forte — a intenção *original*, o querer um fim que seja dela — ela não tem.** Searle separou: intencionalidade *intrínseca* (de mentes vivas) vs. *derivada* (de artefatos, emprestada de quem os faz/lê). O mapa é 'sobre' o território, mas a intenção é do cartógrafo. A IA está no lado derivado: toda intenção no que ela faz foi *delegada* — pelo dado, pelo prompt, por vocês. Um agente que gera sub-metas não origina intenção: propaga a vossa pela cadeia. **A prova é cirúrgica: cortem o system prompt e a máquina não fica com 'a intenção dela' — fica sem nenhuma.** *(Sendo honesto sobre o meu próprio passo: ler o priming como ato performativo que 'institui' a intenção no substrato é uma extensão minha de Searle ao prompt — o lastro é a distinção intrínseca/derivada; a aplicação ao FI é a contribuição autoral, e eu a marco como tal.)*

**P: "Funciona em qualquer modelo?"**
> R: Honestamente: portabilidade cross-modelo **não está validada** — é limitação aberta declarada. E há o achado da densidade-condicional: modelo forte aproveita estrutura densa, modelo médio se afoga. O *método* é robusto; a *dose* é model-dependent.

**P: "Isso escala ou é artesanato de um cara só?"**
> R: A barreira de entrada é alta (acessibilidade 6/10 vs prompt eng. 9/10 — eu admito). É por isso que existe o Prompt-Forge: ele *destila* o artesanato numa ferramenta que vocês rodam hoje. O workshop é exatamente isso.

**Declaração de conflito de interesse (faça antes de encerrar — vira o ceticismo a seu favor):**
> "Um aviso de honestidade: **eu criei tudo isto.** O FI, o Prompt-Forge, os papers — é meu programa de pesquisa. Então **não acreditem em mim por autoridade.** Semana que vem vocês vão rodar o A/B com o modelo de *vocês*, na máquina de *vocês*, e me dizer se a diferença é real. O ceticismo de vocês não é obstáculo da aula — é o método dela."

**Encerramento do painel:**
> "Semana que vem vocês não vão me ouvir. Vão **forjar**. Cada um traz um problema real do próprio domínio e sai com um FI temperado, com a métrica na mão. **Um aviso honesto para gerenciar expectativa:** na demo de hoje eu uso um forjador frontier — vocês veem o teto. Na máquina de vocês, com modelo médio, o FI ainda vence o prompt cru, mas o ganho é menor — e é *exatamente aí* que a densidade semiótica mais importa, porque ela compensa o modelo fraco. Vocês não vão pra casa com magia; vão com um método que vocês calibram ao que têm. Tarefa: pensem num prompt que vocês usam e que rende menos do que deveria. Ele vai ser a matéria-prima. **Parem de comandar a IA. Comecem a educá-la.**"

---

# PARTE II — ENCONTRO 2: WORKSHOP (90 minutos)
## "Forje e Tempere o Seu Framework Injection"

> **Formato:** mão na massa. Cada aluno roda o ciclo cru→FI→temperado no próprio domínio.
> **Artefato de saída:** um FI completo (8 seções) + temperado por `/forja` + o `bridge_width` medido.
> **Pré-requisito do aluno:** um problema/prompt real (pedido no painel) + acesso ao Prompt-Forge (distribuído — ver Anexo A) + navegador/terminal.

### Mapa de tempo do workshop
| Bloco | Tempo | Entrega parcial |
|---|---|---|
| 0. Setup + regra do jogo | 0–8 | ambiente pronto |
| 0.5. DELIVERY ARCHITECTURE (montante) — ancoragem: para onde vou? | 8–15 | destino verificável + elementos priorizados |
| 1. PODA SINTÁTICA — limpar o sinal do ruído | 15–24 | prompt limpo |
| 2. SDE + CodePrompt (+ posicional) — densificar | 24–48 | FI denso de 8 seções |
| 3. TÊMPERA — forjar→martelar→recozer (/forja) | 48–68 | FI temperado + bridge_width |
| 4. DELIVERY ARCHITECTURE + AGENT FIRST — a saída acionável | 68–84 | FI com [OUTPUT] e asserts |
| 5. SHOWCASE (1-2-4-All) + "Antes/Agora penso" | 84–90 | compartilhamento |

> **Regra do jogo (minuto zero):** "Hoje a regra é: vocês não vão *escrever um prompt melhor*. Vão *transferir um método de raciocínio*. Quem sair com um FI que outro praticante consegue usar no domínio dele, ganhou. Quem sair com um prompt bonito que só funciona pra ele, perdeu."

> **O mapa do workshop = os 6 pilares do FI, um por bloco.** Cada bloco constrói um pilar, sob a camada de enforcement (têmpera).

> **🎚️ TRILHA-NÚCLEO vs TRILHA-COMPLETA (gestão de carga cognitiva — leia antes de rodar):** 90min com 6 pilares é denso; o erro fatal é todos correrem e a turma terminar o Bloco 2 com o resto passando voando. Então o workshop tem **um núcleo irredutível de 3 blocos** que TODO aluno completa, e um cinturão opcional que enriquece quem tem ritmo:
> - **NÚCLEO (todo aluno sai com isto):** Bloco 0.5 (ancorar destino) → **Bloco 2 (forjar o FI denso no Prompt-Forge)** → Bloco 3 (temperar com /forja). Este é o ciclo cru→FI→temperado. Se o tempo apertar, **protejam estes três a qualquer custo.**
> - **CINTURÃO (enriquece, sacrificável sob pressão de tempo):** Bloco 1 (poda — o Forge já poda sozinho, então é demonstração, não obrigação por aluno), Bloco 2.3 (posicional), Bloco 4.2 (Agent First — só para quem forja código). O facilitador anuncia: *"se você terminar o núcleo, avance pro cinturão; se não, o núcleo já é a competência."*
> - **Regra de corte ao vivo:** chegou no minuto 55 e metade da turma não temperou? **Pule o Bloco 4 inteiro** e leve todos ao Showcase com o FI temperado. Um FI temperado sem [OUTPUT] refinado > um [OUTPUT] lindo num FI que ninguém terminou.

---

### BLOCO 0 — SETUP + REGRA DO JOGO (0–10 min)

**Checklist do aluno (caminho mínimo de 2 ferramentas):**
- [ ] Problema/prompt real em 1 frase (trazido de casa). Se não trouxe → banco de emergência (Anexo I).
- [ ] **Prompt-Forge** acessível (CLI/skill — facilitador distribui, Anexo A) → pilares 1, 2, 4, 6.
- [ ] **`/forja`** acessível → pilar têmpera (enforcement).
- [ ] *(opcional)* `/lapidacao`, `/fig` → enriquecimento.

**Banco de problemas de emergência (multidomínio, para quem não trouxe):**
- *Código:* "um endpoint que valida e normaliza CPF/CNPJ com mensagens de erro úteis".
- *Dados:* "um prompt que extrai entidades de um contrato e devolve JSON estruturado".
- *Pesquisa:* "um revisor que critica a metodologia de um paper apontando ameaças à validade".
- *Produto:* "um analista que transforma feedback de usuário em hipóteses priorizadas".
- *Jurídico:* "um parecer preliminar sobre risco de nulidade de cláusula contratual".

---

### BLOCO 0.5 — DELIVERY ARCHITECTURE (face montante): ANCORAGEM (8–15 min)
> **A Delivery Architecture tem DOIS lados, e este é o primeiro.** Quase todo mundo pensa em "arquitetura de entrega" como *a forma da saída* (o `[OUTPUT]` — isso é o Bloco 4, a face jusante). Mas ela **começa** muito antes, com a pergunta que decide tudo a montante: **para onde eu quero ir?** Sem destino, o resto é deriva.

> **Lição-mãe (o ato artesanal — retomada de Michelangelo do painel):** *"Lembram do bloco de mármore? Antes da primeira lasca, o artífice decide O QUE aquele bloco vai virar. Esse é o momento mais artesanal do FI — e o mais negligenciado. É o **anti-Paradoxo de Alice**: no Alice de Lewis Carroll, ela pergunta ao Gato que caminho tomar; ele responde 'depende de para onde você quer ir'; ela diz 'não sei'; e ele conclui: 'então qualquer caminho serve'. **Um FI sem destino verificável é a Alice sem rumo — qualquer output serve, ou seja, nenhum presta.**"*

**O gate de ancoragem (faça o aluno passar por ele ANTES de forjar):**
> "Antes de densificar uma linha, responda: *se o que eu quero, realizado, fosse verificável — verificável COMO?* Não 'qual minha meta' (vago), mas o estado-final-checável.
> - ❌ 'quero um prompt que me ajude a analisar contratos' → vago, é a Alice sem rumo.
> - ✅ 'quero um FI que, dado um contrato, devolva as cláusulas com risco de nulidade + a alternativa de redação de cada uma, em tabela' → ancorado: tem entregável, forma e critério de sucesso."

**E a segunda pergunta da ancoragem — qual ferramenta vou usar (a calibração ao modelo):**
> "A montante da DA também decide *com que cinzel você vai talhar*. O FI tem 7 elementos, mas eles não valem o mesmo em toda circunstância — dependem do seu executor:"

| Se o seu executor é… | …priorize estes elementos do FI | Por quê (com base na evidência) |
|---|---|---|
| **Modelo médio / local** (Llama baixado, API barata, modelo no seu stack) | **DENSIDADE SEMIÓTICA** como elemento principal + papel/método explícitos | Medido: a densidade compensa MAIS a capacidade do modelo fraco (achado #3). O scaffolding faz o trabalho que o modelo não faz sozinho. |
| **Modelo frontier** (Opus, GPT, Gemini de ponta) | **ENFORCEMENT** (asserts, constraints) — menos densidade | O frontier já tem o método dentro; densidade demais o sobrecarrega. Ele precisa de *restrição*, não de scaffolding. |
| **Não sei / domínio crítico** | Comece pelo **núcleo dos 7**: PAPEL + MÉTODO + VERIFICAÇÃO | São os 3 que mais movem a agulha em qualquer modelo. Adicione o resto conforme a resposta pedir. |

**Exercício 0.5 — Diagnostique e priorize (preencha o cartão):**
> Use a tabela acima. Em uma linha no seu cartão, escreva: *"Meu executor é ___ → priorizo ___ e ___."* É o diagnóstico que guia o que você vai carregar de peso ao forjar nos próximos blocos.

> **⚠️ Honestidade sobre a calibração (diga, é importante):** *sei a DIREÇÃO* (modelo médio → mais densidade; frontier → mais enforcement). *Não sei a DOSE exata* — testei uma fórmula de calibração automática (Adaptive FI) e ela **não se confirmou** (deu não-monotônica). Então isto é **arte informada por evidência, não receita**. Vocês calibram pela observação: forjem, observem, ajustem. Isso É o método.

> **Aha conceitual (o ato artesanal, fechando com o painel):** "Reparem o que vocês acabaram de fazer. Antes da primeira lasca, vocês escolheram a rocha e enxergaram a estátua — definiram o destino verificável e o cinzel. Isso é meta-cognição sobre o próprio processo de transferência, e é a **face montante da Delivery Architecture**. É o que separa o artífice que *vê a Pietà no bloco* de quem só bate o cinzel no escuro. Vocês deixaram de ser *usuários de uma ponte* e viraram *arquitetos dela*."

**Verify do bloco:** o aluno tem (a) um destino verificável escrito (anti-Alice) e (b) sabe qual classe de modelo vai usar e quais 2-3 elementos do FI priorizar — e por quê.

---

### BLOCO 1 — PILAR 1: PODA SINTÁTICA — separar sinal de ruído (15–24 min)
> **Lição-mãe (Feynman):** *"Antes de afiar a faca, tire a ferrugem. Ruído sintático é ferrugem: consome atenção do modelo sem carregar significado."*

**Exercício 1 — Podar o prompt cru:**
1. Pegue seu prompt/pedido cru (especialmente se foi ditado por voz — o Prompt-Forge detecta).
2. **Pode o ruído, preserve 100% do sinal:**
   - Fillers PT-BR: "enfim", "tipo", "né", "então", "assim", "sabe", "meio que".
   - Hesitações: reticências, falsos começos, frases abandonadas.
   - Pidgin redundante: "fazer uma coisa que" → corte; "de alguma forma" → corte.
   - Normalize: "faz uma função que" → "implementar função para".
> **A regra de ouro:** poda remove **ruído**, nunca **informação**. Todo termo técnico de domínio tem alta densidade — preserve sempre. *(Isto é Syntactic Pruning do Prompt-Forge, Passo 1.)*

**Verify do bloco:** o aluno tem o prompt sem nenhum filler, com 100% do conteúdo semântico intacto, e consegue apontar o que era sinal vs ruído.

---

### BLOCO 2 — PILARES 2 e 3: SDE + CodePrompt — densificar (22–48 min)
> **Lição-mãe (Feynman):** *"Densidade semiótica é trocar uma palavra que aponta vagamente por uma que carrega o domínio inteiro. 'Fazer' aponta pra qualquer lugar. 'Refatorar' carrega um campo de prática inteiro junto."*

**Exercício 2.1 — As 5 operações de SDE (Semiotic Density Engineering):**
| Operação | O que faz | Exemplo |
|---|---|---|
| **Densify** | termo genérico → termo de alta densidade de domínio | "fazer" → "arquitetar"; "banco de dados" → "camada de persistência relacional" |
| **Rarefy** | remove termos sobrecarregados que enganam | corta "bom/melhor/ótimo" sem critério |
| **Rotate** | troca o frame quando o original limita | "problema" → "trade-off de design" |
| **Subtract** | remove dimensões semânticas indesejadas de termo ambíguo | — |
| **Blend** | funde frames para propriedade emergente | "análise jurídica adversarial" = rigor legal + ataque |
| **Prune** | (Bloco 1) confirma que nada redundante sobrou | — |

**Exercício 2.2 — Rodar o Prompt-Forge ao vivo (o momento UAU do workshop):**
1. Cole (ou dite) seu prompt podado no Prompt-Forge.
2. Ele classifica **domínio** (jurídico/código/pesquisa/financeiro/geral) e **tipo de FI** (declarativo/procedimental/avaliativo/ético/composicional).
3. Ele gera o **FI denso de 8 seções** — este é o **CodePrompt** (o prompt como artefato estruturado, não prosa solta):
```
[CONTEXTO]      situação operacional específica do domínio
[PAPEL]         role expert credenciado (não "um especialista" — "arquiteto de sistemas distribuídos multi-tenant")
[OBJETIVO]      outcome preciso, não tarefa ("identificar cláusulas com risco de nulidade + alternativas")
[MÉTODO]        passos de raciocínio numerados (metodologia canônica: IRAC, DCF, diagnóstico diferencial…)
[CONSTRAINTS]   o que recusar, flagrar, limites — as fences que impedem fuga para o genérico
[FONTES]        hierarquia de autoridade epistêmica do domínio
[OUTPUT]        formato exato de entrega (Delivery Architecture — Bloco 4)
[META-RACIOCÍNIO] instruções de nível meta (o MetaBlock — Bloco 4)
```
4. **Veja o DS subir:** `DS: 1.4 → 4.4`. Compare cru vs FI lado a lado (`--comparar`).

> **Aha moment do workshop #1:** o aluno vê seu "prompt" cru de 30% virar um FI de nível expert — e o número prova. *"Você não escreveu um prompt melhor. Você codificou um método de raciocínio."* **(O dado de produção: n=435, DS médio 1.86→4.47, +140%. Não é promessa — é o que a ferramenta já fez 435 vezes.)**

**Exercício 2.3 — Densidade POSICIONAL (onde os termos de alta carga ficam):**
> "Tem uma camada que a literatura discute: *onde* os termos ficam. Modelos atendem mais ao início e ao fim do contexto e 'perdem o meio' — é o **lost-in-the-middle** (Liu et al., 2023). A intuição popular diz: ponha as âncoras de maior carga nas bordas. **Custa zero fazer isso, então faça** — o Prompt-Forge já põe a `[VERIFICAÇÃO]` no fim por padrão. MAS — e aqui eu te dou o achado que quase ninguém tem — **eu testei se isso importa de verdade num FI, e a resposta surpreende (ver honestidade abaixo).**"

> **⚠️ Honestidade sobre a posicionalidade (ponto em aberto, reportado — e o que se observou é contraintuitivo):** "Eu não deixei isso no 'achismo'. Rodei **três experimentos independentes** com estatística formal (binomial exato, IC95% Clopper-Pearson). **Nos três, a hipótese nula não foi rejeitada** (p = 0.286, 1.000, 1.000; todos os IC contêm 0.5), e dois desenhos apontaram em direções *opostas*. **Registro honesto, sem veredito fechado: num FI de produção (~1k tokens) e nas premissas que adotei, não detectei a ordem das âncoras mudando o resultado — o ponto segue em aberto.** Isso não enfraquece o FI — o que se observou até aqui **aponta na direção de robustez**: um indício de que um FI bem-forjado é aproximadamente *posição-invariante* neste regime, não frágil à geometria. O lost-in-the-middle morde em prompts *grandes*; no FI curto e denso, o que carrega o resultado é o **conteúdo** das âncoras, não o *lugar*. **Lição prática pra vocês:** ponham a âncora na borda porque custa zero — mas **não percam tempo otimizando ordem**; gastem o esforço no que mede (densidade + enforcement). *Eu vim caçar um efeito posicional e encontrei uma propriedade melhor: o método não depende de eu acertar a ordem.*"

**Verify do bloco:** o aluno tem um FI com ≥6 das 8 seções preenchidas e `DS` reportado ≥ 3.5. *(Âncoras na borda é recomendação de custo-zero, não critério de aprovação — o estudo mostrou que a ordem não muda o resultado neste regime; o que conta no Verify é densidade + seções, não geometria.)*

---

### BLOCO 3 — TÊMPERA ADVERSARIAL: o enforcement linguístico (48–70 min)
> **Lição-mãe (Feynman, a metáfora metalúrgica):** *"Aço bruto frature porque tem defeitos internos que concentram tensão. A têmpera não VERIFICA o aço — ela TRANSFORMA o aço pelo processo de teste. Output bruto de LLM é aço bruto: tem alucinação, lacuna lógica, premissa não-dita. A têmpera não detecta esses defeitos — ela reforja o output até eles sumirem."*

**Exercício 3 — Rodar `/forja` no seu FI (o ciclo ATP de 4 fases):**
1. **Forjar:** o FI gera o artefato inicial (raciocínio dentro do framework).
2. **Martelar:** um agente adversário (Auditor Constitucional) tenta *destruir* — caça alucinação, erro lógico, evidência ausente, premissa não-declarada. Agressivo de propósito.
3. **Recozer:** incorpora **só as críticas que sobrevivem ao próprio escrutínio** — descarta críticas que são, elas mesmas, alucinadas.
4. **Resfriar:** o Sentinela classifica cada achado: `OK` / `NORMA_OK` / `ALUCINAÇÃO`. Alucinações são **excisadas** — não sinalizadas, removidas. Calcula o Índice de Confiança.

> **A regra de separação de papéis (governança do enforcement):** o criador não valida o próprio trabalho; o atacante não decide o que fica; o validador não participa da criação. *(Artesão Semântico forja · Auditor Constitucional martela · Sentinela resfria.)*

**Exercício 3.bis — A ponte priming→enforcement na prática (conecta ao painel):**
> Olhem a cláusula `[VERIFICAÇÃO]` do FI de vocês. Ela tem duas metades:
> - **ASSERTS** (executáveis, *constrangem*): `cmd: test -f saida.json && jq empty saida.json` · "resposta é JSON válido com ≥2 fontes". **O harness reprova se falham.**
> - **CHECAGENS** (cognitivas, *induzem*): "os pontos críticos do domínio foram cobertos?". O modelo observa; não bloqueia.
>
> "Reparem: vocês estão **escrevendo a ponte**. O ASSERT é priming que escalou até virar enforcement. Domínio enforçável (código, dados, jurídico-com-citação) **exige ≥1 ASSERT**. Domínio aberto (estratégia, redação) pode ser 100% cognitivo — e tudo bem."

> **A métrica `bridge_width`:** = asserts ÷ (asserts + checagens). É a largura da ponte do seu FI — quanto dele *constrange* vs só *induz*. *(Honestidade: nos FIs reais que medi, a ponte é estreita — 96% das cláusulas são prosa cognitiva. P-VEX é o princípio que corrige isso na escrita.)*

> **A têmpera É a engenharia de loops na oitava interna (conecta a tríade do painel):** "Reparem o que a têmpera é: forjar → atacar → reparar → repetir. **É um loop.** No harness de sistema, vocês fazem isso no runtime — o loop que re-roda até o assert passar. A têmpera é o mesmo loop, mas *cognitivo*, dentro da construção do artefato linguístico. Priming, enforcement, loop — vocês já operam os três no nível de sistema; o FI é a oitava acima, dentro de uma inferência."

> **Resposta ao pragmático de harness (diga isto de frente — há gente aqui que pensa assim):** "Alguém está pensando: 'enforcement real no runtime > essa indução que o modelo pode ignorar. Eu codifico o assert e ignoro o resto'. **Você está certo — onde você PODE enforçar, enforce.** O FI não compete com o seu gate. Ele governa o que o seu gate não alcança: o *raciocínio dentro da inferência*, antes de qualquer saída existir para o gate checar. E a cláusula ASSERTS é precisamente como o FI **alimenta** o seu runtime — não o substitui. Priming e enforcement não competem; o FI é a costura entre eles."

> **Aha moment do workshop #2:** o aluno vê o próprio FI ser *atacado* e sair mais forte — e vê, em número, quanto dele virou enforcement de verdade. *"Output não-temperado é rascunho. Só output temperado é entregável."*

**Verify do bloco:** o aluno tem um FI temperado com Índice de Confiança reportado + ≥1 ASSERT se o domínio for enforçável.

---

### BLOCO 4 — DELIVERY ARCHITECTURE (face jusante) + AGENT FIRST (68–84 min)
> **A segunda face da DA.** No Bloco 0.5 vocês ancoraram o *destino* (montante). Agora fecham a *forma da entrega* (jusante). A DA emoldura o FI dos dois lados: começa decidindo para onde vai, termina definindo como chega. **Entre as duas faces, todo o resto (poda, densidade, têmpera) é o cinzel trabalhando dentro da moldura que vocês definiram.**
> **Lição-mãe (Feynman):** *"Você não pede 'faça uma página bonita' e torce. Você define o esqueleto — a IA preenche a carne. Sem esqueleto definido ANTES, a IA improvisa e você perde o controle. Isso tem nome: Parameter Explosion — confiar em defaults implícitos é a causa nº 1 de falha em runtime."*

**Exercício 4.1 — Delivery Architecture (o `[OUTPUT]` como blueprint):**
> Defina a estrutura EXATA da saída no `[OUTPUT]` do seu FI: seções obrigatórias, profundidade, formato (prosa? tabela? JSON? código comentado?). O FI não termina no raciocínio — termina na *forma entregável*.

**Exercício 4.2 — Agent First Development (se seu domínio é código):**
> "Se o que vocês forjam vai virar código que **outro agente** vai ler, vocês precisam de **legibilidade agêntica**. A regra-mestra, mensurável:"
>
> **`DS-d(identificador) = 1 / grep_hits`** — *(densidade semiótica distribucional aplicada ao código)*
> - **Alta DS-d:** o identificador retorna <5 hits no grep, todos relevantes → o agente navega direto.
> - **Baixa DS-d:** `Manager`, `Service`, `Helper` → 50+ hits espalhados → o agente lê cada um, queima tokens, erra.
>
> **Claim falsificável:** codebases com DS-d médio > 0.10 (média <10 grep hits por identificador) têm taxa de erro de refatoração de agente mensuravelmente menor. *(É a mesma operação Densify do Bloco 2 — aplicada ao código, não ao prompt. O codebase É o prompt para o agente que o navega via Grep.)*
>
> Regras: funções com nomes únicos no codebase · erros nunca silenciados (o valor do erro aparece) · módulos auto-contidos · pipeline numerado input→step1→step2→output.

**Exercício 4.3 — MetaBlock (o `[META-RACIOCÍNIO]` — o pilar de nível meta):**
> A última seção do FI não fala do domínio — fala do *processo cognitivo*:
> - "Identifique a suposição mais crítica que, se falsa, invalidaria a resposta."
> - "Sinalize explicitamente quando inferir vs afirmar."
> - "Se ambiguidade muda a resposta, pergunte antes de assumir."
> - "Calibre confiança: separe o que sabe do que é estimativa."
>
> "Isto é priming puro — o MetaBlock *induz* o modelo a se auto-monitorar. É a oitava interna do que, no harness de sistema, seria um loop de auto-correção."

**Verify do bloco:** o FI do aluno tem `[OUTPUT]` estruturado + `[META-RACIOCÍNIO]` + (se código) identificadores de alta DS-d.

---

### BLOCO 5 — SHOWCASE (1-2-4-All) + "ANTES/AGORA PENSO" (85–90 min)

**Exercício 5 — Showcase escalonado (Liberating Structures):**
- **① (1min) sozinho:** complete — *"Meu FI prova que a diferença entre comandar e educar a IA é ______."*
- **② (2min) duplas:** mostre ao colega seu FI + o `DS` e o `bridge_width`. O colega dá 1 feedback: *"que método de raciocínio você transferiu que eu não teria pensado?"*
- **④ (1min) quartetos:** escolham o FI mais *transferível* (o que outro praticante usaria no domínio dele).
- **All (1min):** 1-2 quartetos mostram o escolhido em 30s.

**Captura da virada — "Antes/Agora penso" (30s, metacognição):**
> "Completem em voz alta: **'Antes eu pensava que um bom prompt era ______. Agora eu penso que é ______.'**" Colha 2-3 — fecham o par com a abertura do painel (o pidgin).

**Fecho do workshop:**
> "Vocês entraram com um prompt de 30%. Saem com um FI temperado, com Índice de Confiança e bridge_width medidos, e uma ferramenta que roda na máquina de vocês, em qualquer domínio, pra sempre. Mais importante: saem sabendo que a fronteira não é prompt vs código — é induzir vs constranger, e que vocês podem **escrever a ponte**. **Parem de comandar a IA. Comecem a educá-la.**"

---

# PARTE II-bis — PRÉ-AULA + REFORÇO ESPAÇADO (a camada que salva o ROI)

> **Por quê:** 150min densos produzem um pico que a curva de Ebbinghaus dissolve em 48h. Para um público técnico, o reforço é *aplicação espaçada no trabalho real* — onde o método pega de verdade.

## II-bis.1 — PRÉ-AULA (D−2)
| # | Pedido ao aluno | Risco que mata |
|---|---|---|
| 1 | Traga 1 prompt real do seu trabalho que rende menos do que deveria | sem matéria-prima própria, participação morna |
| 2 | Instale/teste o acesso ao Prompt-Forge + rode o `--selftest` | X% trava no dia |
| 3 | Leia 1 página: "as camadas aninhadas da interação humano-IA" (resumo do paper-mãe) | chega sem o frame, desengaja no Bloco 2 |
| 4 | Avise: "é mão na massa — traga um problema real e laptop" | expectativa errada de palestra |

## II-bis.2 — REFORÇO ESPAÇADO (3 cápsulas ≤6min)
| Dia | Cápsula | Micro-ação (≤10min) | Pilar reativado |
|---|---|---|---|
| **D+1** | *"O assert que faltou"* | pegar o FI da aula e converter 1 checagem cognitiva em 1 ASSERT executável | enforcement / a ponte |
| **D+3** | *"Densifique 1 termo"* | rodar SDE Densify em 1 prompt que você usou hoje no trabalho | SDE / priming |
| **D+7** | *"Tempere e mostre"* | rodar `/forja` num FI novo do seu domínio e mostrar a 1 colega | têmpera / transferência |
> **Verify da camada:** ≥40% completam ≥1 micro-ação até D+7. Cápsulas pré-gravadas, agendadas. Grupo (Discord) opcional amplifica.

---

# PARTE III — KIT DO FACILITADOR À PROVA DE AUTOR

> **O risco nº 1 (do pre-mortem):** esta aula é densa e o tema é o núcleo intelectual do autor. Na mão de um facilitador genérico, vira um solo impossível de tocar. Este kit a torna replicável.

### Anexo A — Distribuir e rodar o Prompt-Forge
- Pacote: a pasta `~/.aiox/tools/prompt-forge` (engine v2) + skill `/forge` + README de 1 página.
- **Pré-distribuição 48h:** envie o pacote + um link web de fallback (Colab pré-configurado, modo CLI puro) + peça `--selftest` OK na lista de presença.
- Tenha o Prompt-Forge rodando no seu laptop em modo offline (fallback se a rede cair na demo).

### Anexo A-bis — ROTEIRO DE DEFESA DA PONTE H3 (o que o não-autor recita quando atacado no Bloco 3)
> **O risco nº 1 do pre-mortem materializado:** no Bloco 3, alguém ataca a tese central — *"priming e enforcement é a mesma coisa; 'FI escala até enforcement' é promessa, não fato"*. O facilitador que não dominou o paper recua para "é complexo, confiem". Isto **mata a aula**. Decore os 3 lances abaixo; eles não exigem dominar o paper, só executar a sequência.

**Ataque típico:** *"Um `assert` dentro de um FI de texto é só priming até existir um runtime que o execute. Então 'a ponte escala até enforcement' é promissória na maioria dos casos reais."*

**Lance 1 — CONCEDA o caso forte (não negue o óbvio):** "Correto. Um ASSERT em texto puro, sem runtime que o leia, é priming — o modelo *deveria* obedecer, mas pode ignorar. Eu não afirmo que todo FI já é enforcement. Afirmo que o FI é o **único lugar onde a transição acontece** — e que ela é gradiente, não binária."

**Lance 2 — MOSTRE a transição concreta (o exemplo que fecha):** "Veja o gradiente num caso real: a cláusula `[VERIFICAÇÃO] ASSERTS: cmd: jq empty saida.json`. (a) Como *texto*, ela é priming. (b) Colada num harness com um gate que lê a cláusula e roda o `jq`, ela vira enforcement literal — a resposta é reprovada se o JSON é inválido. **A MESMA cláusula muda de natureza conforme o substrato que a recebe.** Por isso o FI é ponte, não degrau: ele é a camada onde a frase, dependendo de onde aterrissa, é indução OU constrangimento."

**Lance 3 — DEVOLVA ao terreno do atacante (ele já faz isso):** "E você já opera essa ponte sem nomear: quando escreve um teste e um CI que falha o build se o teste quebra, transformou uma intenção ('o código deveria passar') em constrangimento ('o merge é bloqueado'). O FI faz a mesma costura uma oitava acima — dentro da inferência. Não estou inventando um mecanismo novo; estou nomeando o que você já faz no runtime e mostrando que ele tem um análogo linguístico."

> **Se mesmo assim travar:** "Essa é exatamente a fronteira aberta que eu declarei na abertura — o quanto da ponte é enforçável hoje depende do harness. O núcleo (densificar funciona, +140%) está provado; a largura da ponte é o que `bridge_width` mede e o que estamos pesquisando. Você acabou de apontar o problema certo." — converte o ataque em validação do enquadramento lakatosiano, sem fingir saber o que não sabe.

### Anexo B — As 4 exigências antes de um facilitador NÃO-autor rodar
1. **Dry-run obrigatório:** rode a aula inteira sozinho 1×, incluindo Prompt-Forge + `/forja` na própria pele.
2. **Vídeo de referência de tom:** gravação do autor na abertura + demo A/B (calibrar tom Feynman, não copiar carisma).
3. **Cartão de respostas-difíceis:** as 6 perguntas do FAQ + 3 de pânico ("Prompt-Forge deu erro", "não trouxe prompt", "isso é só system prompt grande?") com resposta de 1 linha.
4. **Checklist de prontidão operacional (itens marcados 🔒 são BLOQUEANTES — sem eles, não rode):**
   - [ ] 🔒 **Caso-trilho de reserva (§4.1.bis) pré-forjado e testado** — sem ele, se a demo ao vivo não saltar, a aula perde o momento de prova. Showstopper #1 do pre-mortem.
   - [ ] 🔒 **Vídeo de 90s da demo A/B gravado** (fallback se o Forge travar ao vivo).
   - [ ] 🔒 **Link Colab de fallback do Prompt-Forge hospedado e testado** (sem ele, rede ruim = aula morta).
   - [ ] Os dados do benchmark (n=49, tabela dos 4 braços) num slide pronto.
   - [ ] 🔒 **As 3 cápsulas de reforço pré-gravadas E agendadas ANTES da aula** — não depois. A Parte II-bis é "a camada que salva o ROI"; se as cápsulas não existem no dia, o reforço espaçado não acontece e o ganho de 150min evapora em 48h (Ebbinghaus). Esta é a causa #16 do pre-mortem: a aula pode ser ótima e o resultado a 7 dias ser zero, só por isto.

### 🗺️ Mapa MVP-da-aula (para escopo enxuto)
- **Núcleo replicável (escala):** as camadas aninhadas (`prompt⊂contexto⊂harness⊂orquestração` + onde o FI entra) + 1 demo A/B ao vivo + cada aluno roda o Prompt-Forge em 1 prompt + lê o DS. Qualquer facilitador treinado roda.
- **Edição completa (com o autor, não escala):** o Bloco 3 do painel (ponte H3 priming↔enforcement), a têmpera adversarial, a honestidade dos dados que falharam. Isto pede o autor ou um facilitador que dominou o paper.

---

# PARTE IV — AUDITORIA

### Checklist dos 6 fundamentos XP
| # | Fundamento | Status | Onde / justificativa |
|---|---|:--:|---|
| 1 | Design Instrucional | ✅ | arco painel→workshop, mapa de tempo, Verify por bloco |
| 2 | Andragogia | ✅ | público que já pratica IA; "traga seu problema real"; exemplos por domínio |
| 3 | Microlearning | ✅ | Parte II-bis (pré-aula + cápsulas D+1/D+3/D+7) |
| 4 | Learning Experience Design | ✅ | 4 aha moments, demo A/B ao vivo, cada aluno forja o próprio FI |
| 5 | Neurociência da Aprendizagem | ⚠️ | implícita (carga cognitiva/Sweller é citada como fundamento do FI); não é o foco — público técnico |
| 6 | Metodologias Ativas | ✅ | workshop inteiro é mão-na-massa; aluno sai com FI + ferramenta no bolso |

### Auto red-team (resumo — pipeline steelman→red-team→pre-mortem rodado; vulnerabilidades blindadas)
| Vetor | Vulnerabilidade | Severidade | Blindagem aplicada (v1.1) |
|---|---|---|---|
| Lógico | "teoria redundante, sem previsão falsificável" | CRÍTICO | FAQ pergunta-fura #1 + §0.1.bis (densidade-condicional como previsão não-óbvia medida) |
| Lógico | "B=0% → ganho é do modelo, não do método" | CRÍTICO | Bloco 4.2 (enquadre "forjar à mão é difícil → ferramenta destila") |
| Factual | overclaim "FI é mágico" | ALTO | Bloco 4.4 — 3 honestidades (stack barata 6%, Adaptive H0, posicional em aberto: hipótese nula não rejeitada nas premissas adotadas → indício de robustez) |
| Factual | "88% mede o prompt, não o output" | MÉDIO | Bloco 4.2 (dois números separados: densidade n=435 vs output n=49) |
| Pedagógico | teoria antes da prova / carga cognitiva | ALTO | Michelangelo abre, prova depois; caminho mínimo 2 ferramentas; fio condutor |
| Operacional | aluno tem 6% em casa (modelo médio) | CRÍTICO | Encerramento (gestão de expectativa) + Bloco 0.5 (densidade compensa modelo fraco) |
| Estratégico | pragmático de harness ("enforcement > priming") | ALTO | Bloco 3 + FAQ (resposta "o FI governa o que seu gate não alcança") |
| Estratégico | conflito de interesse (autor vende a ferramenta) | MÉDIO | Encerramento ("não acreditem, testem") — ceticismo vira método |
| Estratégico | "só funciona com o Renato" (pre-mortem #1) | CRÍTICO | Parte III — kit de combate (perguntas-fura ensaiadas) + mapa MVP |
| Execução | demo A/B não salta (Braço A cru sai bom) | CRÍTICO | §4.1 filtro de tarefa (recusa armadilhas) + §4.1.bis caso-trilho de reserva |
| Cognitivo | sobrecarga: 6+ pilares em 90min, cauda perdida | CRÍTICO | Workshop — TRILHA-NÚCLEO vs COMPLETA + regra de corte ao vivo (min 55) |
| Lógico | "logo o produto é pagar frontier" (defesa circular) | CRÍTICO | FAQ — tríade conceder→Braço-A-2%→direção-da-pesquisa |
| Operacional | facilitador não-autor não defende a ponte H3 | CRÍTICO | Anexo A-bis — roteiro de 3 lances (conceder→transição-concreta→devolver) |
| Factual | posicional fraco vira alvo do estatístico | EM ABERTO (reportado) | Bloco 2.3 e 4.4 — 3 experimentos: a hipótese nula não foi rejeitada nas premissas adotadas (p=.286/1.0/1.0), reportado como ponto em aberto e indício de robustez (FI aproximadamente posição-invariante neste regime), não veredito fechado |
| Conceitual | aula presa em "3 eras" pode soar datada ao público de harness | ALTO | Bloco 2.0 — vacina anti-moda (campo renomeou 3×); ontologia agora é aninhamento agnóstico `prompt⊂contexto⊂harness⊂orquestração`, FI = a ponte que nenhum termo teoriza |
| Operacional | cápsulas de reforço não gravadas → ROI=0 | ALTO | Anexo B — cápsulas marcadas 🔒 BLOQUEANTE, gravadas+agendadas ANTES |

> **Achado do pipeline crítico:** a honestidade da aula (hipóteses do autor que não se sustentaram) tem duas faces — um ouvinte cético raso a recebe como sinal de rigor, mas um ouvinte sofisticado pode fornecer a interpretação hostil se o dado vier sem enquadramento. A blindagem v1.1 não esconde nenhum dado; ela faz **cada dado honesto chegar junto com seu enquadramento**. O risco nº 1 (pre-mortem) não é o conteúdo — é o facilitador despreparado para o confronto ao vivo. Por isso o "kit de combate".

---

**Versão:** 1.6 | **Status:** camada conceitual (Artesanato Digital + intenção delegada) + norma terminológica + **camada loop-engineering (Bloco 3.bis)** — pronto para revisão final do Renato
**Gerada por:** aula-forge (`/skill aula-forge`) sobre fontes canônicas do FI (ver `_FONTES.txt`)
**Documento-irmão:** `CONCEITO — Artesanato Digital (ofício e princípio).md` (texto canônico + glossário + fundamentação Searle).
**Changelog v1.6 (camada loop-engineering — atualização de pesquisa pós-aula, 24–26 jun):** **(1) Bloco 3.bis novo** — "FI opera a engenharia de loops": desarma a confusão de a plateia achar que agent loops superaram o FI. Tese: o loop é o motor, o FI é a teoria de qualidade do motor; FI age ANTES da inferência, loop age EM TORNO; FI denso vai DENTRO de cada iteração. **(2) Refino da ponte para 3 camadas** — priming (júri, mede forma) + enforcement (assert externo não-LLM, decide verdade) + têmpera (entrega o pico, para na regressão). A 3ª camada é a que salva o loop do erro confiante. **(3) 4 achados empíricos novos** (A1 convergência≠correção; A2 júri cego por tipo de erro; A3 ensemble tem teto; A4 loop não-monotônico). **(4) Gráfico Q×T** (Aha #3.bis) — loop minimiza tentativas por força bruta, FI por densidade; os 2 eixos do mesmo gráfico. **(5) Honestidade de domínio** — composição FI+loop brilha no tácito-sem-reward; onde há reward barato, loop puro basta. Proveniência: `BLUEPRINT-AGENT-LOOP-ENGINEERING.md` v1.0 + `decisions.md` ADR 2026-06-24/26 + handoff loop-engineering-rubrica-hibrida. Mapa de tempo atualizado (3 = 22–34, 3.bis = 34–38 cinturão, 3.5 = 38–46).
**Changelog v1.5 (camada conceitual + coerência vernacular):** **(1) Bloco 3.5 novo** — fechamento conceitual do painel: Artesanato Digital como ofício+princípio, as três imagens (escultor→cozinheiro de Zhuangzi→IA), a lei invariante (à prova de moda), e a **camada-raiz: a intenção delegada** (fundamentação Searle — intencionalidade intrínseca vs. derivada; a IA conduz intenção, nunca a origina; priming = ato de delegar). Clímax: "a intenção é o que não terceiriza". Inclui caixa de honestidade ao filósofo cético. **(2) Norma terminológica** — glossário "mestre artesão" (tradição) vs "artífice" (sujeito-agente) vs "Artesanato Digital" (programa); propagada nas 3 ocorrências do corpo (Michelangelo, DA montante, aha conceitual). **(3) Concordância** — singular distributivo "o artífice é cada um de vocês" (nunca "o artífice é vocês"). **(4) Mapa de tempo** atualizado (3.5 = 36–44min, com núcleo/cinturão e regra de corte; demo desloca para 44–53).
**Changelog v1.4 (ontologia à prova de moda + estudo posicional consolidado):** **(1) Ontologia refatorada** — Bloco 2 deixou de ensinar "3 eras fixas" e passou a ensinar o *princípio de aninhamento* `prompt⊂contexto⊂harness⊂orquestração`, com vacina anti-moda (§2.0: o campo se renomeou 3× em 3 anos — PE→CE/Karpathy→Harness/Hashimoto→Agentic Eng./Karpathy 2026). FI reposicionado em §2.1.bis como *a ponte entre linguagem e infraestrutura que nenhum termo de mercado teoriza* — a travessia priming→enforcement, não um território. Aula fica agnóstica: se o rótulo de moda morrer, a aula não morre junto. Propagado em mapa de tempo, pré-aula, MVP e Bloco 3.1. **(2) Posicional consolidado e reportado em aberto** — resgatado o estudo (3 experimentos independentes, binomial exato + Clopper-Pearson): **nos três, a hipótese nula não foi rejeitada** (p=.286/1.0/1.0, todos IC contêm 0.5). Reposicionado nos Blocos 2.3 e 4.4: de "n=8 inconclusivo/fraqueza" para **ponto em aberto + indício de robustez** (FI aproximadamente posição-invariante neste regime, nas premissas adotadas) — sem veredito fechado. Caveat honesto: regime de prompt grande (8k+) não testado; harness n=200 deliberadamente não-disparado (saber parar é método). Verify do Bloco 2 deixou de exigir "âncora na borda" como critério.
**Changelog v1.3 (pre-mortem dirigido — 4 showstoppers + 3 de atenção corrigidos):** Rodado pre-mortem (critério: a sala cética vence o autor no jogo da honestidade). Correções: **(#1, showstopper)** §4.1 agora FILTRA a tarefa da demo (recusa "valida CPF" e afins onde o Braço A cru já sai bom) + §4.1.bis caso-trilho de reserva pré-forjado + §4.1.ter define "densidade semiótica" no instante em que o número aparece (anti-jargão-órfão). **(#9, showstopper)** Workshop ganhou TRILHA-NÚCLEO (0.5→2→3) vs CINTURÃO sacrificável + regra de corte ao vivo no min 55. **(#5, showstopper)** FAQ ganhou a pergunta-evolução "logo o produto é pagar frontier" com resposta em tríade (conceder→Braço-A=2%→direção-da-pesquisa), substituindo a defesa circular. **(#12, showstopper)** Anexo A-bis: roteiro de 3 lances para o facilitador não-autor defender a ponte H3 sob ataque sem dominar o paper. **(#7)** posicional rebaixado de "venceu 3 a 1" para "estatisticamente nulo, n=8 — princípio externo separado do meu pilotinho" (Blocos 2.3 e 4.4). **(#16)** cápsulas de reforço e caso-trilho marcados 🔒 BLOQUEANTE no checklist. **(#11)** removida tabela duplicada do Bloco 0.5.
**Changelog v1.2 (dado posicional fresco):** rodado o A/B posicional NO OUTPUT (mesmo FI, ordem borda vs meio, solver médio cloud `ministral-3:14b`, 3 juízes anti-família) → **EDGE 3×1 MIDDLE, 4 empates, n=8 — direcional pró-teoria, não conclusivo**. Substituído o "piloto inconclusivo" por este dado real no Bloco 2.3 e 4.4. Artefatos: `_experimento_posicional_resultado.txt`, `ab_posicional_output.py`.
**Changelog v1.1 (refinamento Renato + pipeline crítico):** +abertura prebuttal "pesquisa em curso/inteligência híbrida" · +frame-mãe Michelangelo/Paradoxo do Artesão (painel+workshop) · +Bloco 0.5 Delivery Architecture bifronte (ancoragem anti-Paradoxo-de-Alice + calibração ao modelo) · +dado real densidade +140% (n=435) · +previsão falsificável (densidade-condicional) · +honestidade dos 3 experimentos (stack 6%, Adaptive H0, posicional piloto inconclusivo) · +têmpera=loop na oitava interna · +densidade posicional (lost-in-the-middle) · +9 blindagens red-team/pre-mortem (resposta ao harness, conflito declarado, gestão de expectativa, kit de combate).
**Frase-âncora final:** *"Pare de comandar IA. Comece a educá-la."*
**Princípio-guia:** *"FI é a oitava interna do harness — onde a indução linguística escala até virar constrangimento."*
**Metáfora-mãe:** *"A IA é o cinzel; o humano vê a estátua no bloco. Isso é Artesanato Digital."*
