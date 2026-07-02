# Auditoria na ordem do deck único — Framework Injection (3h)

> **Como ler:** este documento percorre a aula na ordem REAL em que ela vai acontecer (deck único, Parte 1 → Parte 2), não na ordem dos arquivos antigos. Cada bloco traz: função no arco · o que entra · o que muda · microaplicação (quando houver).
> **Companheiro:** o diagnóstico lâmina-a-lâmina detalhado (com `[Original]→[Refatorado]`) está em `AUDITORIA-DIDATICA-slides-fi.md`. Aqui é a SEQUÊNCIA.
> **SSOT factual = brief.** Pidgin = ~50% ("rende a metade"). Posicional = p=0,0987, IC[0,17–0,53], **em aberto** (não nulo).
> **Convenção:** `[novo]` lâmina-ponte a criar · `[fundir]` vem de duas lâminas hoje duplicadas · `[mover]` reordenação · `[mantém]` texto preservado · `[refino]` ajuste de texto.
> **Legenda de origem:** L# = lâmina do Painel atual · W# = lâmina do Workshop atual.

---

# PARTE 1 — O OFÍCIO · ~110-120 min · teórica COM mão na massa

## T1 · GANCHO (o aluno sente o problema em 2 min)
**Função no arco:** abrir no registro acessível. É a correção 🔴 mais importante — hoje o gancho está enterrado sob 13 lâminas.

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 1 | Capa "Framework Injection / Pare de comandar, comece a educar" | L1 | `[mantém]` |
| 2 | O pidgin digital — "analisa esse contrato" / telegráfico | L2 | `[mover]` para cá (era ~14ª) |
| 3 | "Isso te custa **cerca da metade** do modelo" | L2 | `[refino]` 70%→~50% (SSOT brief) |
| 4 | O que você sai sabendo (promessa, 3 bullets) | L3 | `[mantém]` |

**Transição → T2:** *"antes de mostrar como, preciso ser honesto sobre o que é isto que vou compartilhar."* (abre o contrato epistêmico — agora o aluno já quer saber).

## T2 · CONTRATO EPISTÊMICO (por que importa, e com que honestidade)
**Função:** estabelecer a postura Renato PI. Agora vem DEPOIS do gancho — o aluno já sente o problema, então a moldura de "como investigo" cai em terreno preparado.

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 5 | Isto é um programa de pesquisa, não um produto fechado | L1A | `[mantém]` — frase-tese Renato PI |
| 6 | Como ler um programa de pesquisa (Lakatos: núcleo/cinturão/borda) | L1B | `[mantém]`, `[mover]` para após o gancho |
| 7 | Onde estamos hoje (cravado ✓ / aberto 🔬 / testado-não-fechado 🜂) | L1C | `[refino]` "vence"→"supera/observado" |

## BLOCO A · O PROBLEMA ESTRUTURAL
**Função:** mostrar que o campo todo tropeça no mesmo vão. Crescendo começa a subir.

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 8 | A escada que virou cebola (prompt⊂contexto⊂harness⊂orquestração) | L4 | `[mantém]` — um dos melhores |
| 9 | O buraco que ninguém nomeia (dois mundos: induz/constrange) | L5 | `[mantém]` |
| 10 | As cinco modalidades de FI | L6 | `[mantém]` |

## BLOCO B · O EIXO ⭐ (primeiro grande uau)
**Função:** o coração conceitual. Pico de tensão #1.

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 11 | O eixo: priming → enforcement (metrô: sinalização→catraca) | L9 | `[mantém]` — não tocar, é a assinatura |

### ▸ CICLO 1 — microaplicação (≤3 min) `[novo]`
| # | Lâmina | Conteúdo |
|---|---|---|
| 12 | **"Induz ou obriga?"** | **Camada 1 (trilho):** projetar o FI de risco de crédito (caso-trilho). *"Em 60s: aponte 1 linha que INDUZ e 1 que OBRIGA."* **Camada 2 (transposição):** *"agora no seu prompt — o que nele obriga?"* |
| — | **Limite revelado** (na própria lâmina) | *"Quase nada do que você escreve hoje OBRIGA. Tudo é sugestão."* → abre a ponte como algo a construir. |

## BLOCO C · A PONTE (a prova antes da asserção)
**Função:** ancorar o nicho. `[mover]` crítico: a prova (L10) vem ANTES da asserção (L9bis).

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 13 | "Mas isso não é só mais um nome?" (OpenAI/Guardrails/ReAct/DSPy) | L10 | `[mover]` para ANTES da próxima — é a prova |
| 14 | A ponte é o coração do programa (o nicho, bidirecional) | L9bis | `[mantém]`, agora ancorada na prova anterior |
| 15 | Onde o FI mora (runtime vs travessia) | L8 | `[mantém]` ou fundir em 14 |
| 16 | A anatomia de um FI (8 seções) | L11 | `[mantém]` |
| 17 | A forma canônica integral (6 instrumentos × lado da ponte) | L11bis | `[mantém]` |

> **Nota:** L11ter (exegese do bridge_width) e L9ter+L9quater (engenharia de loops) **migram para a Parte 2 / aprofundamento** — são mecânica de forja, mais úteis na mão na massa. Tira 3 lâminas densas seguidas do fluxo teórico. Ver `[mover]` no doc detalhado.

## BLOCO D · FUNDAMENTOS (distribuídos, respirando — não em bloco)
**Função:** o lastro acadêmico. Com 3h, ficam INTEIROS no fluxo — só intercalados e com formas visuais variadas para quebrar o vale de fadiga.

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 18 | Fundamentos I — densidade semiótica (7 autores) | L1E | `[mantém]` |
| 19 | Peirce — o signo e o interpretante (signo pobre→estocástico) | L1E.bis2 | `[mantém]` — densidade pura |
| 20 | Fundamentos II — pedagogia e filosofia | L1E.bis | `[refino]` separar fundamentos de artigos |
| 21 | Fundamentos III — **o princípio do ofício** (taoísmo/wu wei) | L1E.ter | `[refino]` título: "raiz filosófica"→"princípio do ofício" |

### ▸ CICLO 2 — microaplicação (≤3 min) `[novo]`
| # | Lâmina | Conteúdo |
|---|---|---|
| 22 | **"Densifique 1 termo"** | **Camada 1:** *"pedido cru 'faça uma análise de risco' — troquem UM verbo genérico por um termo do método."* **Camada 2:** *"façam no seu domínio. Antes/depois em voz alta."* |
| — | **Limite revelado** | *"Vocês sentem que mudou — mas quanto? No olho não dá."* → abre a necessidade de MEDIR. |
| 23 | A demo que se mede (DS 1.86→4.47, +140%, n=435) | L20 | `[mantém]` + medidor DS ao vivo (perfil #2) |

## BLOCO E · O TÁCITO (o clímax filosófico)
**Função:** a virada para o humano. Pico de tensão #2.

### ▸ CICLO 3 — microaplicação (≤3 min) `[novo]`
| # | Lâmina | Conteúdo |
|---|---|---|
| 24 | **"Escreva a regra que você nem pensa"** | *"Em uma frase: a regra que você usa sem pensar no seu trabalho. Não sai inteira, sai?"* |
| — | **Limite revelado** | *"O que você sabe fazer é maior do que consegue dizer."* → abre o tácito/Polanyi. |
| 25 | O nome maior: Artesanato Digital (ofício+princípio+wu wei) | L18 | `[mantém]` ⭐ |
| 26 | A camada-raiz: a intenção delegada ("o artífice é cada um de vocês") | L19 | `[mantém]` ⭐ clímax emocional |
| 27 | **A dificuldade é a prova** (barreira-como-prova, Paradoxo do Artesão) | — | `[novo]` perfil #7 — eleva o FAQ#6 a conceito |
| 28 | A dimensão do uso — equidade (Wang&Zhang, Iacono) | L1E.quinquies | `[mover]` para cá (registro humano) |

## BLOCO F · A PROVA (real e atestado)
**Função:** fechar a credibilidade. Os uaus de honestidade.

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 29 | Dois números — não confunda (input+140% vs output 85-92%) | L21 | `[mantém]` ⭐ Renato PI puro |
| 30 | A estrutura domina o resultado (gráfico eficácia n=49) | L7 | `[mover]` para cá, junto da prova |
| 31 | A borda onde ainda trabalhamos (posicional EM ABERTO) | L22 | `[refino]` dado v2 (ver abaixo) ⭐ negative result |
| 32 | O corpus já publicado (Zenodo, DOIs) | L1E.sexies | `[mover]` para cá |
| 33 | Quem já leu — e respondeu (Ravfogel, Edelsbrunner) | L22bis | `[mantém]` ⭐ uau de credibilidade |

### ★ CLÍMAX C — A CHARNEIRA `[novo]`
| # | Lâmina | Conteúdo |
|---|---|---|
| 34 | **A fusão** | *"Vocês já forjaram 3 peças hoje: classificaram induz/obriga, densificaram um termo, tocaram no próprio tácito. Vejam essas 3 peças virando UM FI — ao vivo."* Roda a construção (L13-15) com o medidor DS subindo. **Esta lâmina fecha a Parte 1 E é o gesto que abre a Parte 2.** |

---

# PARTE 2 — A FORJA · ~60-70 min · emenda direto, SEM capa nova

**Abertura = o outro lado da charneira.** A lâmina 34 (fusão) vista do ângulo do aluno: *"agora é você quem forja — com o seu caso."* Sem W1-capa, sem W1A-reabertura (o contrato epistêmico já foi dado na Parte 1).

| # | Lâmina | Origem | Ação |
|---|---|---|---|
| 35 | A regra do jogo (transfira método, não prompt) | W2 | `[mantém]` |
| 36 | O pipeline de forja — 7 passos (2 ferramentas) | W3 | `[mantém]` |
| 37 | Setup + as duas ferramentas (fallback Colab) | W4 | `[mantém]` |
| 38 | Ancoragem — antes de forjar (gate anti-Alice) | W5 | `[mantém]` |
| 39 | Pilar 1 — Poda sintática (cru→podado) | W6 | `[mantém]` — já é microaplicação modelo |
| 40 | Pilar 2 — Densidade SDE (5 operações) | W7 | `[mantém]` |
| 41 | Rode o Prompt-Forge — ao vivo (gabarito 8 seções) | W8 | `[mantém]` — núcleo |
| 42 | Densidade posicional (3 bandas) | W9 | `[refino]` **dado v2 — ver bloco abaixo** |
| 43 | Têmpera — o ciclo /forja (Forjar→Martelar→Recozer→Resfriar) | W10 | `[mantém]` |
| 44 | A ponte na prática (CHECAGENS vs ASSERTS + bridge_width) | W11 + L11ter | `[fundir]` — recebe a fórmula que saiu do Painel; só aplicação, sem re-teoria |
| 45 | Pilar 4 — Delivery + Agent First (DS-d código) | W12 | `[mantém]` |
| 46 | Pilar 5 — MetaBlock (gabarito) | W13 | `[fundir]` enxuta — regra do fecho já dita na P1 |
| 47 | Showcase 1·2·4·todos ("Antes eu pensava… Agora penso…") | W14 | `[mantém]` ⭐ + aluno-como-corpus (perfil #6) |
| 48 | Leve no bolso — fecho + cápsulas D+1/D+3/D+7 | W15 | `[mantém]` — amarra com a capa |

> **Engenharia de loops (L9ter+L9quater):** entram aqui como **aprofundamento condicional** — o facilitador puxa só se houver praticantes de agent loop na sala (como o KIT já orienta). Não estão no fluxo obrigatório.

---

# A ATUALIZAÇÃO DA DENSIDADE POSICIONAL (não-destrutiva, SSOT=brief)

**Onde:** lâmina 31 (Parte 1, borda viva) e lâmina 42 (Parte 2, tabela das bandas).

**ASSERT — Valor Anterior vs Atualizado:**

| Campo | Valor anterior (slide hoje) | Valor atualizado (v2) | Fundamento (brief) |
|---|---|---|---|
| Banda 16k | "p=0,10 · IC contém ½" (tabela) / dado antigo | **p=0,0987 · IC95% [0,17–0,53]** | brief §3 L54/L58 — "preliminar, em aberto" |
| Leitura das 3 bandas | "em aberto" (cada uma solta) | **"as 3 bandas convergem para NÃO-REJEIÇÃO do nulo"** | brief §3 — "testes não permitem conclusão" |
| Rótulo da métrica | em aberto | **em aberto** (inalterado — núcleo da regra) | brief §3 — "mantido em aberto" |
| Ressalvas | presentes | **mantidas**: corpus pequeno · solver pequeno · frameworks gerados pelo próprio modelo | brief §3 L54/L58 |

**CHECAGEM — a atualização introduziu contradição?** Não. O dado v2 é *mais forte* que o anterior (3 bandas convergindo vs "comparação pendente") e *continua* não-rejeitando o nulo — portanto "em aberto" permanece verdadeiro. **Nada virou "nulo" ou "não funciona".**

**Texto sugerido para a lâmina (refino):**
- [Original — aside/tabela divergentes] → [Refatorado]:
  *"Densidade posicional — onde colocar a carga densa dentro do FI. Medimos em três bandas (4k/8k/16k). No 16k v2: p=0,0987, IC95% [0,17–0,53] — **as três bandas convergem para não-rejeição do nulo.** Não é nulidade do efeito: é uma fronteira que ainda não se fechou para nenhum lado. Premissas: corpus pequeno, solver pequeno, frameworks gerados pelo próprio modelo. Inspirada no Lost-in-the-Middle (Liu et al., 2023). Seguimos medindo."*
- **Justificativa:** regra 4 Renato PI (ausência de conclusão ≠ inexistência de efeito); SSOT brief; elimina o drift entre aside e tabela; *fortalece* a honestidade epistêmica (é o seu negative-result, perfil #1).

---

# RESUMO DA SEQUÊNCIA

- **Parte 1:** 34 lâminas (vs ~30 conceituais hoje + 4 ponte novas − algumas fundidas/movidas para P2).
- **Parte 2:** 14 lâminas (vs 15 hoje − fusões W1A/W11/W13 + recebe L11ter).
- **Total:** ~48 lâminas no deck único (vs 59 atuais) — **mais enxuto, mais contínuo, com 3 microaplicações + 1 charneira novas.**
- **Arco:** gancho cedo → contrato → problema → eixo+prática → ponte → fundamentos+prática → tácito+prática → prova → charneira → forja. Crescendo preservado; 3 vales de fadiga eliminados; 6 uaus (5 antigos + a charneira).
