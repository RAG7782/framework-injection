# Auditoria Didática — Slides Framework Injection (deck único: Parte 1 + Parte 2)

> **Status:** diagnóstico para revisão. Nada foi editado no HTML. Cada mudança estrutural está marcada para aprovação à parte.
> **Premissas atualizadas (sessão 2026-06-27):**
> - **Tempo total: 3 horas, fronteira móvel.** A divisão 60-90/60-90 era convenção; agora a Parte 1 (teórica COM microaplicações) pode usar ~110-120 min e a Parte 2 (mão na massa) ~60-70 min. **Consequência:** os fundamentos NÃO precisam ser comprimidos por falta de tempo — voltam ao fluxo principal, apenas redistribuídos para o ritmo certo.
> - **Deck único contínuo.** Painel e Workshop deixam de ser dois arquivos. Viram Parte 1 → Parte 2 num só HTML. Lâminas hoje duplicadas (W1A↔L1A/L1C · W11↔L9bis/L11ter · W13↔L11bis) **se fundem** — ditas uma vez, no momento certo. Total de lâminas cai, coerência sobe.
> - **Clímax C é charneira.** A fusão das 3 microaplicações num FI fecha a Parte 1 E abre a Parte 2 ("vocês já fizeram as peças → agora é você") — máxima continuidade, sem capa nova.
> **Critérios:** clareza · objetividade · densidade · simplicidade (nível-lâmina) · fluidez · crescendo · efeito uau ancorado (nível-sequência) · arquitetura andragógica B+C com microaplicações (nível-projeto). Estilo: Renato PI (padrão-ouro: `brief-diretoria-fi.html`).
> **Convenção:** `[INF]` = inferência da intenção do autor · `[AF]` = afirmação de melhoria didática · `[INF-PERFIL]` = derivado do seu padrão psicométrico · `[REC-TEC]` = recomendação técnica neutra.
> **Severidade:** 🔴 viola Renato PI / afirmação categórica · 🟡 densidade ou clareza comprometível · 🟢 ajuste fino · ✅ mantém.

---

# CAMADA 0 — ANÁLISE DE ARCO (a aula como curva)

## O mapa atual do Painel (44 lâminas)

O Painel tem hoje **uma abertura epistêmica longa** (lâminas 1A→1G, ~13 lâminas de programa-de-pesquisa/Lakatos/fundamentos/bibliografia/corpus) **antes** do gancho do pidgin (lâmina 2). Isso é a decisão de arco mais consequente do deck inteiro, e é onde mora o principal risco.

### A curva de tensão, como está

```
TENSÃO
COGNITIVA  │                                          ╭─ clímax intенção delegada (19)
   ALTA    │        ╭─ Lakatos       ╭─ ponte(9bis)  ╱
           │       ╱ │              ╱ │             ╱
   MÉDIA   │  ╭───╯  ╰──fundamentos─╯ ╰─eixo(9)────╯ ╰──borda viva──validação──fecho
           │ ╱        (1E→1G: 7 lâminas       
   BAIXA   │╱          densas seguidas)        
           └──────────────────────────────────────────────────────────────────→
            capa  programa  FUNDAMENTOS    gancho   método/anatomia   demo   fecho
                  pesquisa  (platô longo)  pidgin
```

**Os três problemas de arco que a leitura revelou:**

1. 🔴 **O gancho está enterrado.** A pergunta que prende a plateia mista — *"isso te custa 70% do modelo"* (lâmina 2, o pidgin) — só chega depois de ~13 lâminas de fundamentação acadêmica. Para o público técnico, a abertura epistêmica é ouro; para o não-técnico, são 13 lâminas antes de saber *por que deveria se importar*. **A aula abre no registro mais difícil e desce para o mais acessível** — o inverso do que a plateia mista pede. `[AF]`

2. 🟡 **Platô de fundamentos (1E→1G).** Sete lâminas de tabelas Autor→Conceito seguidas (densidade semiótica, pedagogia, Peirce, taoísmo, bibliografia continente, dimensão do uso, corpus). Cada uma é excelente isolada; juntas formam um **vale de fadiga** — mesma forma visual (tabela), mesmo nível de tensão, sem microvariação. O técnico admira; o leigo desliga no terceiro. `[AF]`

3. 🟢 **O crescendo final funciona.** De "onde o FI mora" (8) → eixo (9) → ponte (9bis) → anatomia (11) → demo (13-15) → intenção delegada (19) → borda viva (22) → validação externa (22bis) → fecho: **essa metade sobe bem.** A segunda metade do Painel é o deck no seu melhor. O problema é quase todo na entrada.

### Os pontos de virada (candidatos a "uau") — veredito sobre lastro

| Lâmina | Momento | Tem lastro lógico? | Veredito |
|---|---|---|---|
| 9 — eixo priming→enforcement | a sinalização vira catraca (metrô) | ✅ ancorado em etimologia + mecanismo softmax/gate | **Uau real.** É o coração conceitual. |
| 9bis — a ponte é o coração | "ninguém ocupa este nicho" | ✅ ancorado na tabela de quem-faz-o-quê (lâmina 10) | **Uau real**, mas chega *antes* da prova (lâmina 10 vem depois) — ordem subótima. |
| 13-15 — construção ao vivo | a DS sobe 1.3→4.4 | ✅ se a demo rodar; ancorado no medidor | **Uau cinético** — o mais forte para plateia mista. |
| 19 — intenção delegada | "o artífice é cada um de vocês" | ✅ ancorado em Searle | **Uau emocional/filosófico** — bem posicionado como clímax. |
| 22bis — quem já leu e respondeu | Ravfogel + Edelsbrunner endossaram | ✅ ancorado, com escopo honesto | **Uau de credibilidade** — e é puro Renato PI. Subutilizado: está quase no fim. |

**Conclusão de arco:** você tem **cinco** pontos de uau com lastro — material raríssimo. O problema não é falta de uau; é que (a) o primeiro deles demora ~17 lâminas a chegar, e (b) nenhum deles é uma *microaplicação do aluno* — são todos demonstrações suas. É exatamente o gap que a Camada 0.5 resolve.

---

# CAMADA 0.5 — ARQUITETURA ANDRAGÓGICA B+C

## O princípio que reorganiza tudo

Hoje o Painel é **exposição** e o Workshop é **prática** — separação limpa, mas o Painel inteiro passa sem o aluno *tocar* em nada por 60 min. A arquitetura B+C insere **3 microaplicações de ≤3 min no Painel** (espiral) e faz o Painel **culminar numa demo-projeto única** (o clímax C), sem destruir o crescendo — porque cada microaplicação *abre* o próximo conceito em vez de interrompê-lo.

## Os 3 ciclos, mapeados nas lâminas reais

> **Unidade:** Conceito denso → Microaplicação (≤3min, no caso-trilho comum + transposição) → **Limite revelado** (que é a porta do próximo conceito).

### CICLO 1 — onde entra: depois da lâmina 9 (eixo priming→enforcement)
- **Conceito:** priming vs. enforcement (a navalha "pode desobedecer?").
- **Microaplicação (NOVA lâmina-ponte):** *"Olhem este FI de risco de crédito [caso-trilho]. Em 60 segundos: aponte 1 linha que INDUZ e 1 que OBRIGA."* (camada 1: trilho comum, todos veem o mesmo). Depois: *"agora no seu próprio prompt mental — o que nele obriga? Provavelmente nada."* (camada 2: transposição).
- **Limite revelado:** *"quase tudo que vocês escrevem só induz."* → **abre a anatomia (11) e a ponte como algo a construir.**

### CICLO 2 — onde entra: junto da lâmina 20 (a demo que se mede / densidade)
- **Conceito:** densidade semiótica (o termo que carrega o campo).
- **Microaplicação:** *"Peguem o pedido cru 'faça uma análise de risco'. Troquem UM verbo genérico por um termo do método. Digam em voz alta o antes/depois."* (trilho) → *"façam no seu domínio."* (transposição).
- **Limite revelado:** *"vocês sentem que mudou — mas quanto? Não dá pra saber no olho."* → **abre a necessidade de medir / o medidor DS (sugestão de perfil #2).**

### CICLO 3 — onde entra: antes da lâmina 19 (intenção delegada)
- **Conceito:** conhecimento tácito / Paradoxo do Artesão (Polanyi).
- **Microaplicação:** *"Tentem escrever, em uma frase, a regra que vocês usam sem pensar no trabalho de vocês. Não sai inteira, sai?"*
- **Limite revelado:** *"o que vocês sabem fazer é maior do que o que conseguem dizer — e é por isso que precisa de um andaime externo."* → **abre a intenção delegada (19) e o FI como externalização do tácito.**

## O clímax C — a fusão (NOVA lâmina, antes do fecho)
As 3 microaplicações que o aluno fez (1 indução/obrigação · 1 densificação · 1 tentativa-de-verbalizar-o-tácito) **são as 3 peças de um FI**. A demo de construção ao vivo (13-15) deixa de ser "olhem eu construir" e vira **"vocês já construíram as 3 peças — agora eu mostro elas se fundindo num FI completo, ao vivo."** O Painel inteiro retroilumina: o aluno percebe que estava forjando o tempo todo.

> **Este é o efeito uau estrutural máximo** — o que amplia o arco *para trás* (sugestão de perfil #4, meta-demonstração). E casa com o Workshop, onde o aluno refaz sozinho com o caso dele.

**Decisão pendente para você:** as 3 microaplicações no Painel custam ~10-12 min. Num Painel de 60 min com 13 lâminas de fundamentação, **não cabe sem cortar**. Minha recomendação `[AF]` está na Camada 1 (proposta de compressão dos fundamentos). É o principal trade-off ritmo×densidade do projeto.

---

# CAMADA 1 — AUDITORIA LÂMINA A LÂMINA

## PAINEL

### L1 — CAPA ✅🟢
- **Diagnóstico:** "Pare de comandar a IA. Comece a educá-la." é forte e fiel. `assinatura` "um ofício, não um atalho" é Renato PI puro. Clareza e densidade altas.
- **Ajuste 🟢:** o subtítulo é levemente imperativo/venda ("Pare… Comece…"). Em Renato PI estrito seria exposição. Mas aqui `[INF]` é gancho legítimo de capa, não claim de resultado — **mantenho**, só sinalizo.
- **Veredito:** mantém.

### L1A — "Isto é um programa de pesquisa, não um produto fechado" ✅
- **Diagnóstico:** abertura epistêmica exemplar. "Trago as conclusões a que já cheguei — e, com a mesma honestidade, onde ainda não cheguei" é a frase-tese do Renato PI. Mantém intacta.
- **Função no arco:** estabelece o contrato. **Mas:** ver Camada 0 — esta lâmina inaugura o platô que adia o gancho. A lâmina é ótima; sua *posição* é o problema (tratado adiante).

### L1B — "Como ler um programa de pesquisa" (Lakatos) ✅🟡
- **Diagnóstico:** o diagrama núcleo/cinturão/borda é necessário — é o que torna honesto dizer "isto não se sustentou" sem "fracassou". Conceito denso, bem entregue.
- **Risco 🟡 `[INF]`:** Lakatos como **segunda** lâmina da aula é pesado para a plateia mista. O técnico ama; o leigo ainda não sabe por que precisa disso. **Recomendação de arco:** mover o aparato Lakatos para *depois* do gancho do pidgin — o aluno precisa sentir o problema antes de receber a moldura epistemológica de como o problema será investigado.
- **Texto:** mantém. Posição: reavaliar (ver proposta estrutural).

### L1C — "Onde estamos hoje" (cravado/aberto/não-fechado) ✅
- **Diagnóstico:** o contrato epistêmico em 3 caixas. Densidade alta, honestidade exemplar. "Nas nossas premissas, não se sustentou" é o léxico Renato PI canônico.
- **Refino 🟢 [Texto Original]→[Refatorado]:**
  - Original: *"o FI denso vence o comando cru num modelo forte — medido às cegas (85–92% vs 0–2%). E densifica o input (+140%)."*
  - Refatorado: *"o FI denso supera o comando cru num modelo forte — observado às cegas (85–92% vs 0–2%) — e densifica o input (+140%)."*
  - Justificativa: "vence" é levemente competitivo/venda; "supera… observado" mantém a densidade e adota o verbo de observação (regra 2). Ganho marginal mas consistente com o padrão-ouro.

### L1D — "O que é Framework Injection" (definição canônica) ✅
- **Diagnóstico:** a pedra angular. A definição está densa, precisa e honesta quanto a prior art (DSPy/ReAct). "Não se comanda a IA: educa-se" amarra com a capa. Mantém.
- **Nota de clareza 🟢:** a 3ª qualificação ("O que esta linha formaliza — a ponte") é a mais densa e a mais importante, mas vem como item de lista, perdendo peso. `[AF]` Considerar destacá-la visualmente (já há `.climax` no topo — talvez um segundo realce). Ajuste fino, não bloqueante.

### L1E — "Fundamentos I — densidade semiótica" 🟡
- **Diagnóstico:** tabela de 7 autores. Conteúdo impecável e verificado (DOI real). **Problema de arco, não de conteúdo:** primeira das 7 lâminas-tabela seguidas.
- **Recomendação 🟡 `[AF]`:** ver "Compressão do platô de fundamentos" abaixo. Isolada, a lâmina mantém.

### L1E.bis — "Fundamentos II — pedagogia, filosofia e artigos" 🟡
- **Diagnóstico:** mistura fundamentos (Vygotsky→Searle) com artigos de terceiros (Liu/Lost-in-the-Middle) numa lâmina só. A mistura prejudica a clareza — são duas naturezas distintas espremidas.
- **Refino 🟢:** separar visualmente "fundamentos pedagógicos" de "artigos pesquisados" (já há a divisão no texto, mas o peso visual é igual). Parte do pacote de compressão.

### L1E.bis2 — "Peirce — o signo e o interpretante" ✅🟡
- **Diagnóstico:** densíssima e excelente. "Signo pobre → resposta estocástica · signo rico → resposta quase-determinística" é uma das linhas mais fortes do deck inteiro — é DENSIDADE pura.
- **Risco 🟡:** é a 3ª tabela seguida e a mais abstrata. Para a plateia mista, Peirce-em-detalhe pode ser o ponto de maior evasão. `[INF]` Candidata a virar lâmina opcional/aprofundamento (o técnico quer; o leigo não precisa para o arco). **Recomendação:** manter no deck mas marcar como "lâmina de aprofundamento" que o facilitador pode pular sem quebrar o fio.

### L1E.ter — "Fundamentos III — raiz filosófica (taoísmo + ofício)" ✅
- **Diagnóstico:** o wu wei com fonte (Tao Te Ching explícito). "A matéria muda; o princípio não" é a tese da invariância em uma linha. Mantém — é eixo identitário.
- **Nota Renato PI:** a skill avisa: *taoísmo é transversal, não raiz; o eixo é Artesanato/maestria.* O título "raiz filosófica" para o slide do taoísmo pode confundir. 🟢 **[Original]→[Refatorado]:** "Fundamentos III — a raiz filosófica" → **"Fundamentos III — o princípio do ofício"** (alinha com a estrutura canônica: o eixo é o Artesanato; o taoísmo costura, não enraíza).

### L1E.quater — "Bibliografia continente do programa" 🟡
- **Diagnóstico:** Vaswani/RNN/Behrouz — a literatura de arquitetura que sustenta a invariância. Conteúdo correto, mas é a 5ª tabela. Para a plateia mista, "bibliografia continente" é o ponto onde o arco mais esfria.
- **Recomendação 🟡 `[AF]`:** forte candidata a **fundir** com a borda de fundamentos ou virar backup do facilitador. O argumento ("a lei não depende do Transformer") pode ser dito em 1 frase na lâmina da invariância, sem a tabela inteira no fluxo principal.

### L1E.quinquies — "A dimensão do uso (ética/equidade)" ✅🟡
- **Diagnóstico:** Wang & Zhang + Iacono. Verificado (G6, nota cuidadosa sobre J vs U). Conteúdo valioso e é o único momento "humano/social" da fundamentação.
- **Risco de arco 🟡:** está no meio do platô técnico, onde menos ressoa. `[INF]` Esta camada (equidade, "o ofício como ponte") teria muito mais força **perto do fecho/intenção delegada** — onde o registro já é humano — do que perdida na bibliografia. **Recomendação:** considerar mover para junto do bloco Artesanato/intenção (18-19).

### L1E.sexies — "O corpus já publicado" (Zenodo) ✅
- **Diagnóstico:** 8 papers com DOI real. Materializa "é pesquisa registrada, não improviso". Renato PI puro (proveniência). Mantém.
- **Arco:** encerra o platô. **Recomendação:** se o platô for comprimido, esta é uma das que sobrevivem (prova de lastro), mas pode vir mais tarde, perto da validação externa (22bis) — os dois juntos formam o bloco "isto é real e atestado".

### L1F — "O FI vive dentro do Artesanato Digital" ✅
- **Diagnóstico:** reposiciona o FI como instrumento de um programa maior. Necessária. Mantém. Boa transição do epistêmico para o conceitual.

### L1G — "O telos: inteligência híbrida" ✅
- **Diagnóstico:** o objetivo último (simbiose, Margulis, Licklider). Você marcou na memória que é "o ponto que mais quer presente". Mantém — mas ver arco: hoje fecha a abertura longa. Funciona como ponte para o gancho.

### L2 — "O pidgin digital" (gancho) ✅🔴(posição)
- **Diagnóstico:** **este é o verdadeiro gancho da aula** e está na lâmina ~14. "Isso te custa cerca de 70% do modelo" é a frase que prende. Texto: excelente, mantém.
- 🔴 **Problema de arco (o mais importante do deck):** o gancho deveria estar **muito mais cedo**. Ver proposta estrutural "Abertura em dois tempos".
- **Refino 🟢 `[INF]`:** "cerca de 70%" — verificar o lastro desse número. O brief fala "metade" (~50%, "rende a metade"). 70% vs 50% é inconsistência interna entre slides e brief. **Alinhar** (regra 6: número com fonte). Qual é o correto?

### L3 — "O que você sai sabendo" (promessa) ✅
- **Diagnóstico:** contrato com a plateia, 3 bullets. Claro e enxuto. Mantém.
- **Refino 🟢:** "e o nome do ofício que faz isso" é ótimo (curiosidade). Mantém.

### L4 — "A escada que virou cebola" ✅
- **Diagnóstico:** diagrama prompt⊂contexto⊂harness⊂orquestração. Excelente — "camadas aninhadas, não uma escada. Nada foi aposentado" é clareza+densidade exemplar. Um dos melhores slides. Mantém.

### L5 — "O buraco que ninguém nomeia" ✅
- **Diagnóstico:** os dois mundos (linguagem induz / infra constrange). Prepara o FI sem nomear. "Ninguém costura os dois" — gancho perfeito. Mantém.

### L6 — "As cinco modalidades" ✅
- **Diagnóstico:** tabela das 5 modalidades. Clara, necessária, bem-feita. Mantém.
- **Arco 🟢:** é tabela densa logo após duas lâminas-conceito leves. Ritmo ok aqui (a tensão pede a sistematização). Mantém posição.

### L7 — "A estrutura domina o resultado" (gráfico eficácia) ✅
- **Diagnóstico:** 85–92% vs 0–2%, n=49, juízes cegos. A prova do output. Forte. Mantém.
- **Nota:** "vence 85–92%" — mesmo refino do verbo (supera/é preferido). O brief usa "é preferido em 85,7–91,8%". 🟢 Alinhar léxico ao brief (padrão-ouro): **"preferido"**, não "vence".

### L8 — "Onde o FI mora" ✅
- **Diagnóstico:** runtime vs ponte. Curto, denso, prepara o eixo. Mantém.

### L9 — "O eixo: priming → enforcement" ✅ ⭐
- **Diagnóstico:** **a lâmina-assinatura.** O metrô (sinalização→catraca), o critério "pode desobedecer?". Uau real ancorado. Não toco. É o coração.
- **Função no arco:** primeiro grande uau. **Ponto de inserção do CICLO 1** (microaplicação) logo após.

### L9bis — "A ponte é o coração do programa" ✅🟡
- **Diagnóstico:** o nicho que ninguém ocupa, bidirecional. Densíssima e central. Conteúdo mantém.
- **Risco de arco 🟡:** afirma "é o nicho que ninguém ocupa" **antes** da lâmina 10 que *prova* isso (a tabela OpenAI/Guardrails/ReAct/DSPy). A asserção chega antes da evidência. `[AF]` **Recomendação:** inverter — 10 (a prova de que ninguém nomeia) antes de 9bis (a asserção do nicho). Deixa o uau ancorado em vez de antecipado.

### L9ter — "O FI opera a engenharia de loops" ✅🟡
- **Diagnóstico:** loop=motor, FI=teoria de qualidade. Você mesmo marcou "cinturão sacrificável". Densíssima — talvez a lâmina mais densa do deck.
- **Risco 🟡:** para plateia mista, este é um pico de carga cognitiva que pode não pagar. `[INF]` É defensiva (responde "isso não foi superado pelo agent loop?"). **Recomendação:** manter como **lâmina condicional** — o facilitador entra nela só se houver praticantes de agent loop na sala (o KIT já trata assim). Marcar visualmente como "aprofundamento".

### L9quater — "Os dois eixos do mesmo gráfico" (Q×T) ✅
- **Diagnóstico:** loop sobe Q gastando tentativas; FI sobe Q gastando densidade. A imagem É o argumento. Se cortar o bloco loop, esta sozinha carrega. Mantém — mas é par da 9ter (condicional junto).

### L10 — "Mas isso não é só mais um nome?" ✅
- **Diagnóstico:** tabela fazem/não-fazem (OpenAI, Guardrails, ReAct, DSPy). É a **prova** do nicho. Excelente, honesta (reconhece o que cada um faz). Mantém texto.
- **Arco:** mover para **antes** de 9bis (ver acima) — a prova ancora a asserção do nicho.

### L11 — "A anatomia de um FI" (8 seções) ✅
- **Diagnóstico:** as 8 seções + MetaBlock + coda, com âncoras marcadas. Núcleo operacional. Mantém. Clara.

### L11bis — "A forma canônica integral" (6 instrumentos) ✅🟡
- **Diagnóstico:** 6 instrumentos × lado da ponte. "A VERIFICAÇÃO bicéfala é a travessia: CHECAGENS induzem · ASSERTS constrangem" — linha-chave. Densa.
- **Risco 🟡:** vem logo após a 11 (anatomia) — duas lâminas de estrutura interna seguidas, ambas densas. Possível sobrecarga. `[AF]` Avaliar fundir os pontos essenciais ou espaçar com a microaplicação do Ciclo 1 entre elas.

### L11ter — "Por que a ponte se mede assim" (bridge_width) ✅🟡
- **Diagnóstico:** exegese da fórmula `asserts/(asserts+checagens)`. Excelente para o técnico — "0=puro priming, 1=tudo atravessou". Honesta (não inflar, assert-teatro reprova).
- **Risco 🟡 `[INF]`:** é a **terceira** lâmina densa de mecânica interna seguida (11→11bis→11ter). Para a plateia mista é o segundo platô do deck. **Recomendação:** 11ter é forte candidata a "aprofundamento opcional" — a fórmula importa para quem vai forjar (Workshop), menos para quem assiste ao Painel. Mover boa parte para o Workshop (onde W11 já trata bridge_width).

### L12 — "O mesmo FI, em dois registros" ✅
- **Diagnóstico:** FI-máquina vs FI-humano. Conceito importante (dual-legibilidade). Clara. Mantém.

### L13-15 — "Construindo um FI — ao vivo" (3 lâminas auto-animadas) ✅ ⭐
- **Diagnóstico:** a demo de construção com o medidor DS subindo (1.3→3.0→4.4). **Uau cinético** — o mais forte para plateia mista. Mantém.
- **Arquitetura B+C:** **esta é a sede do clímax C.** Reframe: em vez de "olhem eu construir", torna-se "vocês já fizeram as 3 peças nas microaplicações — vejam-nas se fundindo". Requer 1 lâmina-ponte antes (a fusão). Ver Camada 0.5.
- **Sugestão de perfil #2 (medidor ao vivo):** o `ds-gauge` já existe no CSS — explorar como instrumento que o aluno aponta para o próprio prompt.

### L16 — "Mesmo o pedido mais preguiçoso" (par Declarativo) ✅
- **Diagnóstico:** cru→FI, DS 1.0→4.0, n=435. Bom exemplo. Mantém.
- **Arco 🟡:** L16 e L17 são dois pares cru→FI seguidos. Para o arco, talvez **um** baste no Painel (o outro vai para o Workshop ou backup). Avaliar.

### L17 — "Um pedido profissional, multifacetado" (par Composicional) ✅🟡
- **Diagnóstico:** o caso status-line, DS 2.5→4.8. Bom, mas é o segundo par seguido. `[AF]` Candidato a corte/mover se o tempo apertar — redundante em função com L16.

### L18 — "O nome maior: Artesanato Digital" ✅ ⭐
- **Diagnóstico:** ofício+princípio+costura (wu wei), Michelangelo. Eixo identitário. Lindo e fiel. Mantém. Uau filosófico.

### L19 — "A camada-raiz: a intenção delegada" ✅ ⭐
- **Diagnóstico:** "a IA executa; não pretende"; "a intenção é o que não se terceiriza; o artífice é cada um de vocês". **Clímax emocional.** Searle como lastro. Mantém — é o pico.
- **Arquitetura B+C:** **ponto de chegada do CICLO 3** (tácito). A microaplicação do tácito desemboca aqui.

### L20 — "A demo que se mede" (densidade input) ✅
- **Diagnóstico:** gráfico DS 1.86→4.47, +140%, n=435. A prova do input. Mantém.
- **Arquitetura B+C:** **sede do CICLO 2** (microaplicação de densificação).

### L21 — "Dois números — não confunda" ✅ ⭐
- **Diagnóstico:** densidade(input)+140% vs vitória(output)85-92%, amostras distintas. **Esta lâmina é Renato PI puro** — antecipa a objeção e separa o que se mede. Brilhante. Mantém.

### L22 — "A borda onde ainda trabalhamos" ✅ ⭐
- **Diagnóstico:** densidade posicional em aberto, ajuste-runtime não-sustentado. **A lâmina de honestidade epistêmica** — exatamente a sugestão de perfil #1 (negative result). Já existe! Mantém e valoriza.
- **Sugestão de perfil #1:** esta lâmina É o "negative result". Considerar dar-lhe mais peso visual — é o seu maior diferencial.

### L22bis — "Quem já leu — e respondeu" ✅ ⭐🟡
- **Diagnóstico:** Ravfogel + Edelsbrunner, com escopo honesto (validação de STEER/IMI, não do FI direto). **Uau de credibilidade.** Mantém o texto — a honestidade de escopo é o que o torna forte.
- **Risco de arco 🟡:** está penúltima. `[INF-PERFIL]` Para o seu perfil (credibilidade por honestidade), este ativo poderia respirar melhor — talvez emparelhado com o corpus (1E.sexies) formando um bloco "isto é real e atestado" antes do fecho.

### L23 — "Fecho" ✅
- **Diagnóstico:** volta ao mapa Lakatos (núcleo/cinturão/borda), "dispor o método e deixar fluir", "é isto que pesquiso, é aqui que ainda não sei". **Fecho Renato PI perfeito** — sem call-to-action de venda (regra 7). Mantém. "Amanhã você forja o seu" amarra com o Workshop.

### L24 — "?" ✅
- **Diagnóstico:** lâmina-pergunta. Minimalista, eficaz. Mantém.

---

## WORKSHOP (15 lâminas)

### W1 — CAPA "Forje e Tempere o Seu FI" ✅
- Mantém. "Mão na massa" sinaliza o registro. Bom contraste com o Painel.

### W1A — "Antes da mão na massa" ✅
- **Diagnóstico:** reinstala a humildade epistêmica (núcleo provado / borda aberta) em 1 lâmina. Renato PI fiel. Mantém.

### W2 — "A regra do jogo" ✅
- **Diagnóstico:** "não escreva um prompt melhor; transfira um método". A tese em uma linha. Mantém.

### W3 — "O pipeline de forja — 7 passos" ✅
- **Diagnóstico:** diagrama dos 7 passos + 2 ferramentas. "Você está aqui" reaparece. Anti-Sweller (2 ferramentas, não 10). Mantém.

### W4 — "Setup + as duas ferramentas" ✅
- **Diagnóstico:** operacional, com fallback Colab. Mantém. Importante para não travar.

### W5 — "Ancoragem — antes de forjar" ✅
- **Diagnóstico:** gate anti-Paradoxo de Alice + tabela executor→prioridade. Densa e prática. Mantém.

### W6 — "Pilar 1 — Poda sintática" ✅
- **Diagnóstico:** exemplo cru→podado lado a lado. "Pode o ruído, nunca o sinal." Clara. Mantém. **Esta é a 1ª microaplicação real do Workshop** — bom modelo do que o Painel deveria ter.

### W7 — "Pilar 2 — Densidade (SDE)" ✅
- **Diagnóstico:** 5 operações (densify/rarefy/rotate/subtract/blend). "Densidade é DIAL, não axioma." Mantém.

### W8 — "Rode o Prompt-Forge — ao vivo" ✅
- **Diagnóstico:** o gabarito de 8 seções + comando. Backup Colab. Mantém. Núcleo do Workshop.

### W9 — "Densidade posicional" ✅🟢
- **Diagnóstico:** a borda em aberto, com a tabela das 3 bandas (4k/8k/16k). Honesto (em aberto, não nulo).
- **Refino 🟢:** a nota do `aside` diz que o 16k v2 fechou (p=0,0987) — mas a tabela visível ainda mostra dados antigos. **Verificar e alinhar** o número exibido com o dado mais recente (regra 6). Possível drift entre aside e tabela.

### W10 — "Têmpera — o ciclo /forja" ✅
- **Diagnóstico:** ciclo Forjar→Martelar→Recozer→Resfriar, separação de papéis (Artesão/Auditor/Sentinela). Densa e original. Mantém.

### W11 — "A ponte: priming→enforcement, na prática" ✅
- **Diagnóstico:** CHECAGENS vs ASSERTS com exemplos de código + bridge_width. Mantém. É onde a fórmula do Painel 11ter pode migrar e ganhar contexto prático.

### W12 — "Pilar 4 — Delivery + Agent First" ✅
- **Diagnóstico:** [OUTPUT] exato + DS-d para código. "Cinturão — só para quem forja código." Honesto sobre escopo. Mantém.

### W13 — "Pilar 5 — MetaBlock" ✅
- **Diagnóstico:** as 4 diretrizes metacognitivas + regra do fecho (coda/exceção Ético). Mantém. Consistente com o Painel 11bis.

### W14 — "Showcase — 1·2·4·todos" ✅ ⭐
- **Diagnóstico:** Liberating Structures + "Antes eu pensava… Agora penso…". **A virada metacognitiva capturada** — fechamento andragógico perfeito (o aluno verbaliza a transformação). Mantém. **Sugestão de perfil #6 (aluno-como-corpus):** o "antes/agora" pode ser coletado como dado.

### W15 — "Leve no bolso" (fecho + cápsulas) ✅
- **Diagnóstico:** as cápsulas D+1/D+3/D+7 + "pare de comandar, comece a educar" (amarra com a capa do Painel). Mantém. Bom fecho de arco duplo (Painel↔Workshop).

---

# CAMADA 2 — AS 7 RECOMENDAÇÕES DE PERFIL (onde ancorar)

| # | Recomendação | Já existe? | Onde ancorar no arco |
|---|---|---|---|
| 1 | **Negative result** | ✅ L22 (borda viva) | Já está. Dar mais peso visual — é o diferencial. |
| 2 | **Medidor DS ao vivo** | parcial (ds-gauge no CSS) | L13-15 e L20 + microaplicação Ciclo 2. Tornar instrumento que o aluno aponta. |
| 3 | **Falsificação convidada** | parcial (6 perguntas no KIT) | Pós-fecho ou Q&A (L24). Versão controlada (você apresenta o steelman). Risco de palco — opcional. |
| 4 | **Meta-demonstração** | não explícito | **Vira o clímax C** (fusão das microaplicações em L13-15). O maior uau estrutural. |
| 5 | **Provenance visível** | parcial (`.fonte` já existe) | Transversal — já há gramática visual de fonte. Adicionar selo 🔬 consistente para "em aberto". |
| 6 | **Aluno-como-corpus** | parcial (W14, cápsulas) | W14 + cápsulas. "Vocês geram os dados da próxima versão." |
| 7 | **Barreira-como-prova** | implícito (FAQ #6) | Elevar a uma lâmina conceitual perto de L18-19: "a dificuldade é a prova" (Paradoxo do Artesão). |

---

# PROPOSTAS ESTRUTURAIS (requerem aprovação à parte)

## EP1 — Abertura em dois tempos 🔴→✅ `[AF]` (a mais importante)
**Problema:** o gancho (pidgin, L2) está enterrado sob ~13 lâminas de fundamentação.
**Proposta:** dividir a abertura.
- **Tempo 1 (gancho, 3-4 lâminas):** Capa → Pidgin (L2) → "isso te custa X% do modelo" → promessa (L3). O aluno sente o problema em 2 min.
- **Tempo 2 (contrato epistêmico, condensado):** "isto é programa de pesquisa" (L1A) + Lakatos (L1B) + "onde estamos" (L1C) — agora o aluno já sabe *por que* importa.
- **Fundamentos:** comprimidos (ver EP2) e distribuídos, não em bloco.
**Ganho:** abre no registro acessível, sobe para o denso — curva certa para plateia mista. Preserva todo o conteúdo, muda a ordem.

## EP2 — Redistribuição do platô de fundamentos 🟡→✅ `[AF]` (REVISADO: com 3h, não é mais corte)
**Problema:** 7 lâminas-tabela seguidas (1E→1G) = vale de fadiga — *independente do tempo*. O problema é de RITMO (mesma forma visual repetida), não de duração.
**Proposta (revisada):** os fundamentos **permanecem no fluxo principal** (o tempo extra de 3h os acomoda). O que muda é a **distribuição**: quebrar a sequência de 7 tabelas iguais intercalando-as com as microaplicações e variando a forma visual. Ex.: densidade semiótica perto do Ciclo 2 (densificação); taoísmo/ofício perto do bloco Artesanato (L18); a dimensão do uso/equidade perto da intenção delegada (L19). Peirce-detalhe e bibliografia-continente seguem no deck — não puláveis por tempo, mas posicionadas onde a tensão as comporta.
**Ganho:** elimina o vale de fadiga **sem sacrificar nenhum fundamento**. Resolve a tensão rigor×ritmo que o tempo de 3h tornou falsa — você fica com os dois.
**Decisão `[INF]`:** você confirmou (sessão 2026-06-27) que os fundamentos voltam ao fluxo. EP2 deixou de ser "comprimir para caber" e virou "reordenar para o ritmo". ✅ resolvido.

## EP5 — Unificação dos decks num fluxo contínuo 🟢→✅ `[AF]` (NOVO — confirmado)
**Decisão:** Painel + Workshop num único HTML, Parte 1 → Parte 2, sem capa nova entre eles.
**Fusões (lâminas hoje duplicadas → ditas uma vez):**
- W1A (humildade epistêmica) ↔ L1A + L1C → a Parte 2 não reabre o contrato epistêmico; herda o da Parte 1. W1A vira 1 frase de transição ("o núcleo que provamos lá atrás é sobre o que você forja agora").
- W11 (ponte priming→enforcement na prática) ↔ L9bis + L11ter → a teoria da ponte fica na Parte 1; W11 vira só a **aplicação prática** (os exemplos de código CHECAGEM/ASSERT), sem re-explicar o conceito.
- W13 (MetaBlock) ↔ L11bis → a regra do fecho/coda é dita uma vez (Parte 1); W13 vira o **gabarito operacional** do MetaBlock para o aluno preencher.
**Charneira (clímax C):** a lâmina-fusão fecha a Parte 1 (o FI nasce das 3 peças do aluno) e *é* o gesto que abre a Parte 2 ("agora você refaz com o seu caso"). Uma só lâmina-dobradiça.
**Ganho:** o fio nunca se quebra; sem redundância; o projeto-fio ("seu FI") fica contínuo do primeiro conceito ao showcase final. Reduz o total de lâminas.

## EP3 — Inserir os 3 ciclos de microaplicação 🟢→✅ `[AF]`
3 lâminas-ponte novas (Ciclo 1 pós-L9, Ciclo 2 em L20, Ciclo 3 pré-L19) + 1 lâmina-fusão (clímax C pré-L13-15). Custo: ~10-12 min. Depende de EP1+EP2 abrirem espaço.

## EP4 — Reordenações pontuais 🟢 `[AF]`
- L10 (prova do nicho) **antes** de L9bis (asserção do nicho).
- L1E.quinquies (dimensão do uso/equidade) **junto** de L18-19 (registro humano).
- L22bis (validação externa) + L1E.sexies (corpus) formando bloco "real e atestado" antes do fecho.

---

# ESPINHA DORSAL DO DECK ÚNICO (3h) — estrutura-alvo

```
PARTE 1 — O OFÍCIO  ·  ~110-120 min  ·  teórica COM mão na massa
─────────────────────────────────────────────────────────────────
  T1 GANCHO (3-4 lâm)     capa → pidgin → "custa X%" → promessa
  T2 CONTRATO (3 lâm)     programa de pesquisa → Lakatos → onde estamos
  A  O PROBLEMA           cebola aninhada → dois mundos → 5 modalidades
  B  O EIXO ⭐            priming→enforcement (L9)
       ▸ CICLO 1          microaplicação: induz/obriga no caso-trilho → transposição
       └─ limite: "quase nada que você escreve OBRIGA"
  C  A PONTE              prova do nicho (L10) → a ponte (L9bis) → anatomia 8 seções
  D  FUNDAMENTOS          densidade semiótica · Peirce · taoísmo/ofício
       (distribuídos, formas visuais variadas, respirando — não em bloco)
       ▸ CICLO 2          microaplicação: densifique 1 termo → transposição
       └─ limite: "mudou — mas quanto? não dá pra ver no olho" → medidor DS
  E  O TÁCITO
       ▸ CICLO 3          microaplicação: escreva a regra que você usa sem pensar
       └─ limite: "o que você sabe é maior do que consegue dizer"
       → intenção delegada (L19) ⭐ → barreira-como-prova
  F  A PROVA              dois números (L21) → borda viva (L22) → quem atestou (L22bis)
  ★ CLÍMAX C (charneira)  "vocês já forjaram as 3 peças — vejam o FI nascer"
                          ↓ a mesma lâmina abre a Parte 2

PARTE 2 — A FORJA  ·  ~60-70 min  ·  mão na massa  ·  emenda direto, sem capa
─────────────────────────────────────────────────────────────────
  "agora é você"          (= clímax C visto do outro lado)
  pipeline 7 passos → poda → SDE → Prompt-Forge ao vivo → posicional
  → têmpera (/forja) → bridge_width na prática (W11 enxuta)
  → delivery/agent-first → MetaBlock gabarito (W13 enxuta)
  → showcase 1-2-4-all → fecho + cápsulas D+1/D+3/D+7
  (W1A já fundida na transição; sem reabertura do contrato epistêmico)
```

**Contagem estimada:** o deck único fica com **menos** lâminas que os 44+15=59 atuais — as ~3 fusões (W1A, W11, W13) compensam as ~4 lâminas-ponte novas (3 ciclos + charneira). Saldo aproximado: neutro a -2 lâminas, com coerência muito maior.

---

# SÍNTESE EXECUTIVA

**O que está forte (não mexer):** toda a metade conceitual do Painel (L9 em diante), a honestidade epistêmica (L1A, L1C, L21, L22, L22bis, fecho), o Workshop inteiro (arquitetura andragógica já madura). O estilo Renato PI **já está aplicado** na maior parte — este deck foi construído com a skill. As regressões ao tom de venda são pontuais (verbos "vence", subtítulo de capa).

**O que move o ponteiro (com as premissas de 2026-06-27):**
1. **EP5 — deck único contínuo** (Parte 1 → Parte 2, fusões). Confirmado. Dá a continuidade de arco que nenhuma outra mudança dá sozinha.
2. **EP1 — abertura em dois tempos** (gancho cedo). Maior ganho de arco para plateia mista.
3. **EP3 + clímax C charneira** — as microaplicações que transformam a Parte 1 de exposição em projeto, e a fusão que costura as duas partes.
4. **EP2 — redistribuição dos fundamentos** — agora SEM corte (o tempo de 3h resolveu). Vira reordenação por ritmo. Tensão rigor×ritmo dissolvida.

**A decisão difícil DESAPARECEU.** Com 3h e fronteira móvel, você não precisa escolher entre rigor exaustivo e ritmo — tem os dois. Era a única tensão real do projeto; o tempo extra a desfez.

**O que NÃO é problema:** densidade conceitual. Ela está alta e bem ancorada. O trabalho aqui quase nunca é *adicionar* densidade — é *reordenar* para que ela chegue na hora certa, *intercalar* a prática para fixá-la, e *fundir* o que estava dito duas vezes.

**Inconsistências factuais — RESOLVIDAS (SSOT = brief, decisão 2026-06-27):**
- **Pidgin:** "cerca de 70% do modelo" (slide L2) → **alinhar ao brief: "a metade / ~50%"** (brief §"sua IA rende a metade do que poderia"). Valor anterior: 70%. Valor atualizado: ~50%. Fundamento: brief, seção 1 + síntese.
- **Densidade posicional (W9):** atualizar para o dado v2 mais recente — **16k: p=0,0987, IC95% [0,17–0,53]** — exibido como **não-rejeição do nulo nas 3 bandas → segue EM ABERTO** (jamais "nulo"). Ressalvas do brief mantidas (amostra pequena, solver pequeno, frameworks gerados pelo próprio modelo). Fundamento: brief §3 (linhas 54, 58) — "em aberto / preliminar / inconclusivo, mantido em aberto". Regra 4 Renato PI: ausência de conclusão ≠ inexistência de efeito.
