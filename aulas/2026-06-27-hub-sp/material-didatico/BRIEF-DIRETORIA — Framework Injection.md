---
documento: Nota Técnica de Viabilidade
destinatário: Diretoria — Academia Lendária
assunto: "Framework Injection — estado atual de um programa de pesquisa (Artesanato Digital)"
autor: Renato Aparecido Gomes
classificação: confidencial — uso interno da diretoria
data: junho 2026
extensão: 3 páginas
---

# Framework Injection — Nota Técnica de Viabilidade

### A exposição do estado atual de um programa de pesquisa sobre a interação humano–IA generativa

> **Em uma linha, para a diretoria:** esta é a apresentação do estado atual de um programa de pesquisa em curso — sobre como interagimos com as inteligências artificiais generativas. Reúne fundamentação acadêmica organizada em camadas, uma descrição operacional do método (anatomia, modalidades, ferramenta) e as observações já reunidas, distinguindo com cuidado o que já se sustenta do que segue em aberto. Esta nota apresenta os fundamentos e a estrutura — sem expor o mecanismo proprietário que constitui o conteúdo compartilhado ao vivo.

---

## 1. O problema que se observa

Boa parte do conteúdo de "IA aplicada" trata de **comandar** modelos — prompts, atalhos, listas de super-comandos. Esse material tende a envelhecer rápido, e o público avançado já o domina.

A questão que se pretende abordar é outra: **observa-se que a qualidade do que uma IA produz parece depender menos da qualidade do comando e mais da qualidade do método de raciocínio transferido a ela.** O campo de construção com IA renomeou sua disciplina central três vezes em três anos (engenharia de *prompt* → de *contexto* → de *harness*; já se fala em "engenharia agêntica"). Cada renomeação reconhece que a estrutura *ao redor* do modelo influencia o resultado — mas nenhuma descreve **a ponte entre a linguagem que instrui e a infraestrutura que executa**. É esse vão que esta pesquisa procura observar e nomear.

**Para a Academia:** uma oportunidade de acompanhar de perto uma frente de investigação ainda em aberto, em vez de correr atrás do consenso já consolidado.

---

## 2. O método

O Framework Injection é uma estrutura de transferência de conhecimento do ser humano para a máquina, descrita por uma gramática própria. Dois eixos a compõem:

**As 5 modalidades de Framework Injection** — cada FI transfere uma destas coisas:
- **Declarativo** — *o que saber* (hierarquias de fonte, ontologias)
- **Procedimental** — *como raciocinar* (metodologia passo-a-passo)
- **Avaliativo** — *como julgar* (rubricas, critérios)
- **Ético** — *o que recusar* (cercas de compliance)
- **Composicional** — *como combinar* os anteriores

**A anatomia de 8 seções** — `[PAPEL] [OBJETIVO] [MÉTODO] [CONTEXTO] [FONTES] [OUTPUT] [CONSTRAINTS] [VERIFICAÇÃO]`, mais MetaBlock e coda. A estrutura é dinâmica e adaptável — molda-se à necessidade do que se pede. O eixo que a norteia é a travessia **Priming → Enforcement**: a linguagem que *induz* escalando até a obrigatoriedade que *constrange*. A verificação deriva desse eixo — separa **ASSERTS** (que constrangem: um sistema externo reprova) de **CHECAGENS** (que induzem: o modelo observa) — e permite estimar a maturidade de um framework: `bridge_width = asserts / (asserts + checagens)`.

A proposta é que se possa **classificar e construir** o próprio framework — uma habilidade de transferência agnóstica a modelos e às transformações tecnológicas no tempo. O encontro inclui uma **demonstração ao vivo de construção** e uma **sessão mão na massa** com a ferramenta (Prompt-Forge) e o ciclo de têmpera, para aplicar e atestar o método na prática.

---

## 3. O que se observou até aqui

As observações vêm de medições produzidas em ambiente real de trabalho. **Dois números medem coisas diferentes; um terceiro segue em aberto** — a distinção é deliberada e importa:

| # | O que foi medido | O que se observou | Amostra e método |
|---|---|---|---|
| **1** | **Densidade** do que o usuário *escreve* (o input do método) | densidade semiótica média sobe de **1,86 para 4,47 (+140%)** — direcionado | **435 transmutações reais** de produção, múltiplos domínios |
| **2** | **Qualidade** do que a IA *devolve* (o output), avaliada às cegas | o método estruturado é preferido em **85,7%–91,8%** dos casos vs. **0–2%** do comando cru — direcionado | **49 tarefas**, três desenhos independentes, juízes cegos de **3 famílias de modelos não-Anthropic** (consenso 2 de 3), viés de comprimento controlado (vitória-por-comprimento ≤4%) |
| **3** | **Robustez posicional** do método | **em aberto** — os testes preliminares não permitem, ainda, conclusão | testes preliminares (binomial exato, Clopper–Pearson) em amostra pequena e com frameworks gerados pelo próprio modelo; reportados como tais |

**Parte das hipóteses foi testada e ainda não é conclusiva.** Não se trata de refutação — são frentes que seguem em análise, e expor seus limites é parte do método:
- **Adaptive-FI** (ajustar a "força" do método em tempo de execução): nas premissas adotadas, os testes não sustentaram o ganho esperado — segue em estudo.
- **Posicional**: resultado preliminar e inconclusivo (amostra pequena, uma única vertente abordada) — mantido em aberto.
- **H3-média**: a infraestrutura automatizada barata, hoje, *não substitui* um agente forte na forja — limite localizado e honesto.

Estes pontos não foram conclusivos porque o corpus é pequeno e porque se abordou, por ora, apenas uma das vertentes possíveis; há outras a adotar. Diante de um público técnico que sabe falsificar afirmações, distinguir com cuidado o que se sustenta do que segue em aberto é parte da postura de pesquisa.

> **Nota de propriedade intelectual:** os números acima são o *resultado*. A sintaxe completa do framework, o pipeline que o gera e o vocabulário operacional constituem o ativo autoral compartilhado ao vivo. Esta nota apresenta as observações e a estrutura do método; o mecanismo detalhado é reservado ao conteúdo do encontro.

---

## 4. Fundamentação acadêmica

A investigação se apoia em um **programa de pesquisa** com fundamentação organizada em camadas distintas — fundamentos diretos, bibliografia complementar e corpus publicado próprio.

### 4.1 Fundamentos I — a densidade semiótica (linguística cognitiva)
Sete fundamentos ajudam a compreender *por que* densificar a instrução parece funcionar:
- **Fillmore** (1982, Frame Semantics — o termo-chave ativa um frame)
- **Rosch** (1975, Prototype Theory — termos prototípicos nas âncoras)
- **Fauconnier & Turner** (2002, Conceptual Blending — compor FIs gera estrutura emergente)
- **Lakoff & Johnson** (1980, Conceptual Metaphor — transfere método entre domínios)
- **Firth** (1957, Distributional Semantics — a DS-distribucional, mensurável)
- **Collins & Loftus** (1975, Spreading Activation — a carga densa se propaga na rede)
- **Goldberg** (1995, 2006, Construction Grammar — a construção *coage* a interpretação; o FI é uma construção)

Antecedentes em análise: **Langacker** (gramática cognitiva), **Barthes** (conotação), **Goodman** (densidade simbólica).

### 4.2 Fundamentos II — pedagogia e filosofia
- **Vygotsky** (Zona de Desenvolvimento Proximal — o FI como *scaffolding*)
- **Sweller** (carga cognitiva — o FI reduz a carga extrínseca)
- **Wittgenstein** (jogos de linguagem — ensina *qual jogo* jogar)
- **Polanyi** (conhecimento tácito — base do *Paradoxo do Artesão*)
- **Peirce** (semiótica — projeta a Terceiridade/interpretante) · **Greenberg** (universais linguísticos)
- **Searle** (*Intentionality*, 1983 — intencionalidade intrínseca vs. derivada → conceito autoral de **intenção delegada**)

### 4.3 Fundamentos III — os fundamentos do programa (a maestria do artífice)
O eixo é o **Artesanato** — a figura do Mestre Artesão, o homem integral que une o saber tradicional à tecnologia avançada e, agora, à IA generativa. Daí: **Artesanato Digital**. O taoísmo e os demais são conceitos *transversais* a esse eixo, não a sua raiz. A passividade ativa: *o que deixa de ser para que tudo seja.*
- **Maestria — o Mestre Artesão**: o homem integral, saber tradicional ⟶ tecnologia ⟶ IA generativa *(eixo)*
- **Sennett — *The Craftsman***: a maestria que se cultiva, não se copia (com Polanyi, a linha do ofício/tácito)
- **Laozi — *Tao Te Ching* (道德經)**: o *wu wei* (無為), a ação sem forçar — "dispor o vazio para a forma emergir" *(transversal)*
- **Zhuangzi**: o Cozinheiro Ding — a lâmina que acha os vazios *(transversal)*

### 4.4 Bibliografia complementar (literatura de arquitetura)
Não são fundamentos diretos do FI; sustentam a tese de **invariância à arquitetura** do programa: **Vaswani et al.** (2017, *Attention Is All You Need*), **RNNs com caching / state-space**, **Liu et al.** (2023, *Lost in the Middle*), estudos **Stanford/Tsinghua** (harness → até 6×) e **UC Berkeley**; genealogia: **Karpathy** (contexto), **Hashimoto** (harness).

### 4.5 A dimensão do uso (ética e equidade)
Fontes das palestras OAB Santo Amaro / advocacia negra: **Wang & Zhang** (2026, *Pedagogical partnerships with generative AI in higher education*, IJETHE, n=912, DOI `10.1186/s41239-026-00585-x` — a curva do uso: não-usar / usar-errado / usar-certo) e **Iacono** (2026, *Hybrid Horizons* — o mapa colonial da IA, a *IA pequena* / Small AI, o salto de etapa na África e Ásia).

### 4.6 Corpus publicado (Zenodo)
A linha de Framework Injection e Artesanato Digital está registrada publicamente — **27 papers publicados** no total. Da linha direta (amostra com DOIs reais):
| Artigo (EN) · tradução | DOI |
|---|---|
| Framework Injection · *Injeção de Framework* | `10.5281/zenodo.19479916` |
| Founding Paper · *Artigo Fundador* | `10.5281/zenodo.19344789` |
| Semiotic Density · *Densidade Semiótica* | `10.5281/zenodo.19645955` |
| SDE Encoding · *Codificação por Densidade Semiótica* | `10.5281/zenodo.19887868` |
| Delivery Architecture · *Arquitetura de Entrega* | `10.5281/zenodo.19939303` |
| Adaptive FI · *FI Adaptativo* | `10.5281/zenodo.20040726` |

Corpus completo (incl. Agent-First Development, The Artisan's Paradox, IMI, AGORA, STEER, NMP, MIAA, Somatic Markers e outros) disponível à diretoria sob solicitação.

---

## 5. Como isto pode ser compartilhado

Duas frentes complementares:
- **(I) Painel teórico (60–90 min)** — exposição dos conceitos e do estado atual da pesquisa; com kit de facilitação que permite reapresentar o material além do autor.
- **(II) Mão na massa (60–90 min)** — aplicação das ideias compartilhadas, para atestar a metodologia na prática, com a ferramenta (Prompt-Forge) e fallback Colab para quem não tem ambiente técnico.
- **Camada de reforço posterior** (cápsulas D+1/D+3/D+7) contra a curva de esquecimento.
- **Auditoria de qualidade já aplicada** (revisão adversarial e teste de pontos de falha).

Eventualmente, serão disponibilizados alguns dos **instrumentos** — ferramentas e skills que criei e hoje utilizo no meu próprio trabalho.

**Limite declarado:** os leitores cegos do benchmark são modelos de famílias independentes — isso fecha o viés "Claude avaliando Claude", mas não substitui validação cross-arquitetura ampla nem revisor humano de domínio. A portabilidade cross-modelo e a dose ótima de densidade seguem como fronteira de investigação em aberto, e são apresentadas como tais.

---

## Em síntese

Esta é a exposição de um **programa de pesquisa em curso** sobre a forma como interagimos com a IA generativa. Reúne **o que se observou até aqui** (dois desenhos experimentais distintos, com método reproduzível), **fundamentação acadêmica organizada em camadas** (linguística cognitiva, pedagogia/filosofia, a raiz no Artesanato — com o taoísmo como transversal — mais bibliografia complementar e um corpus de 27 papers publicados) e uma **descrição operacional do método** (painel, sessão mão na massa, ferramenta, kit). Distingue-se, com cuidado, o que já se sustenta — ou se direciona a uma conclusão — do que ainda permanece em aberto, em investigação. Os limites são expostos, não escondidos.

É este o estado atual destas investigações. As páginas anteriores são o seu retrato no tempo presente. O autor disponibiliza-se para uma demonstração fechada de 15 minutos à diretoria, sem expor o mecanismo proprietário.

---
*Nota preparada para leitura executiva. As observações são auditáveis internamente; o mecanismo metodológico é reservado ao conteúdo do encontro.*
