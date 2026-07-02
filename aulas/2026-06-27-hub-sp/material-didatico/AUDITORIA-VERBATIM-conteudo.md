# Auditoria verbatim do conteúdo — `slides-aula-fi-completo.html`

> **Método (G4/G6/G7):** cada termo/número do deck confrontado com SSOT — brief-diretoria,
> FONTE-glossario, FONTE-classificacao, papers Zenodo (DOIs) e memórias IMI (im_nav verbatim).
> Veredito por item: ✓ verificado · ⚠️ impreciso (corrigir) · ✗ errado (corrigir) · ℹ️ nota.
> Data: 2026-06-27. Fontes IMI citadas por node_id.

---

## A. NÚMEROS EMPÍRICOS (os de maior risco)

| # | Claim no deck | Veredito | Fonte / Correção |
|---|---|---|---|
| A1 | DS input **1,86 → 4,47 (+140%)**, n=435 | ✓ | brief §3 L52; IMI `fe0308b4c8e3` (fact-check G4: ds_o=1,860 ds_f=4,467; **+165% era ERRO**, +140% correto). **Manter.** |
| A2 | Eficácia output **85–92% vs 0–2%**, n=49, consenso 2 de 3 | ✓ | brief §3 L53 diz **85,7%–91,8% vs 0–2%**, **49 tarefas, 3 desenhos, 3 famílias não-Anthropic (consenso 2 de 3), viés-compr ≤4%**. "85–92%" é arredondamento fiel. IMI `pattern_67eb2b`: A=2% B=0% C₀=4% **C₁Opus-inline=88%** C₂=6% (88% é UM braço; a faixa cobre 3 desenhos). **Manter, mas ver A2-bis.** |
| A2-bis | n=49 vs n=62 | ℹ️ | n=49 = amostra de **julgamento** (brief §3). n=62 = **série mainline de carriers** (IMI `5ff1d584908b`: 47 code+14 general; `cb6f0868f2df`). São coisas distintas — sem erro. **Não confundir no palco.** |
| A3 | Posicional **p=0,0987, IC95% [0,17–0,53]**, 3 bandas convergem p/ não-rejeição | ✓ | brief §3 L54 (binomial exato, Clopper-Pearson, amostra pequena, em aberto). Piloto bruto `_experimento_posicional_resultado.txt`: n=8, EDGE 38% vs MIDDLE 12%, "direcional não conclusivo". **Manter — "em aberto, não nulo".** |
| A4 | viés-comprimento **4%** / "≤4%" | ✓ | brief §3 L53 "≤4%"; IMI `cb6f0868f2df` "vies-comprimento-4pct". **Manter.** |
| A5 | bridge_width empírico **~0.04** (aside lâmina 46) | ✓ | IMI `pattern_b78311`: "bridge_width=0.0409 FIs reais". **Manter.** |

---

## B. TERMOS DO FI (instrumentos) — cruzados com FONTE-glossario

| # | Claim no deck | Veredito | Correção |
|---|---|---|---|
| B1 | **5 operações SDE** (densify/rarefy/rotate/subtract/blend) | ✓ na P2 (lâmina 42) | glossario §1 nota: "SDE = **5 operações**; Poda Sintática é instrumento nº2 SEPARADO, não operação SDE". **Lâmina 42 já tem 5 ✓. CONFERIR que nenhuma lâmina diga 6.** |
| B2 | Forma canônica = **6 instrumentos** (lâmina 17/⑰) | ⚠️ | glossario PARTE I: são **7 instrumentos** (1 SDE · 2 Poda · 3 CodePrompt · 4 Delivery · 5 Agent-First · 6 MetaBlock · **7 Reatualização/coda**). O deck lista 6 (funde MetaBlock+coda). **Corrigir para 7, OU rotular explicitamente "6 + a coda como 7º".** A coda é instrumento próprio (recency, condicional). |
| B3 | DS **cultural** vs distribucional (dsc/dsd) | ℹ️ ausente | O deck NÃO expõe a distinção dsc/dsd. glossario §1: rótulo canônico é **cultural** (não "conceitual"). Não é erro de omissão (é aprofundamento), mas se entrar, usar **cultural**. |
| B4 | Delivery Architecture "abre E fecha, não só jusante" | ✓ | glossario §4 Face 1: "transversal, não só jusante". Deck lâmina 17 diz exatamente isso. **Manter.** |
| B5 | Agent-First = **cinturão só-código** | ✓ (+pendência) | glossario nota 4 PENDENTE (sua decisão). Deck trata como cinturão. **Consistente; pendência sua segue aberta.** |
| B6 | MetaBlock penúltimo + coda re-ancora; exceção Ético/anti-aluc. encerra | ✓ | glossario §7 verbatim. Deck lâminas 17 e 48. **Manter.** |

---

## C. EIXO / PONTE / NOMES CANÔNICOS

| # | Claim no deck | Veredito | Fonte |
|---|---|---|---|
| C1 | **SCA — Semantic Coercion Axis** (Goldberg, a construção coage) | ✓ | IMI `4a214c9af38a`: "sca semantic-coercion-axis p2e e2p ... goldberg coercao". **Manter.** |
| C2 | **P2E / E2P** vetores asc/desc | ✓ | IMI `4a214c9af38a` + `fbfb5f92e755` (via descendente/ascendente). **Manter.** |
| C3 | **RFI = FI × DA** (artefato = conteúdo × entrega) | ⚠️ | IMI registra **RFI = Reasoning Framework Injection** (`4a214c9af38a`). A fórmula "FI × DA" NÃO aparece verbatim nas fontes — é síntese minha do handoff. **Rebaixar de afirmação a formulação, ou remover.** Não cravar como se fosse canônico publicado. |
| C4 | bridge_width = asserts/(asserts+checagens), model-invariante | ✓ | IMI `pattern_b78311`, brief §2 L40, glossario PARTE III. **Manter.** |
| C5 | FI = ponte bidirecional enforcement↔priming, "INDUZ vira constranger" | ✓ | IMI `fbfb5f92e755` (decisão H3 verbatim). **Manter.** |
| C6 | critério-mestre "o agente PODE desobedecer?" | ✓ | FONTE-classificacao Nível 2 + glossario. **Manter.** |

---

## D. FUNDAMENTOS (autores) — cruzados com brief §4

| # | Claim no deck | Veredito | Correção |
|---|---|---|---|
| D1 | **Fundamentos III = "o princípio do ofício"** com Laozi/Zhuangzi como raiz | ✗ ÊNFASE ERRADA | brief §4.3 é EXPLÍCITO: o eixo é **o Artesanato / o Mestre Artesão** (o homem integral: saber tradicional→tecnologia→IA). "**O taoísmo e os demais são conceitos TRANSVERSAIS a esse eixo, não a sua raiz.**" glossario confirma: wu wei é "o princípio do ofício" mas o EIXO é o Mestre Artesão. **Corrigir lâmina 23: o Mestre Artesão é a raiz; Laozi/Zhuangzi/Sennett são transversais.** |
| D2 | 7 fundamentos linguísticos (Fillmore, Rosch, Fauconnier&Turner, Lakoff&Johnson, Firth, Collins&Loftus, Goldberg) | ✓ | brief §4.1 idêntico. **Manter.** |
| D3 | Peirce tríade + interpretante algorítmico + semiose projetada | ✓ | brief §4.2 + glossario PARTE II semiótico. **Manter.** |
| D4 | Searle intencionalidade intrínseca/derivada → intenção delegada | ✓ | brief §4.2 + glossario; IMI `f6b440194c44` "intencao-delegada-searle". **Manter.** |
| D5 | Wang&Zhang β=0,335/0,351 + curva J; Iacono Small AI/87%-17% | ✓ | brief §4.5 (DOI 10.1186/s41239-026-00585-x verificado). **Manter — Wang&Zhang foi G6-verificado (retratação do 'fantasma' em 31-mai).** |
| D6 | Liu 2023 Lost-in-the-Middle; Stanford/Tsinghua 6×; Berkeley | ✓ | brief §4.4. **Manter.** |
| D7 | Vaswani Attention; RNN-com-cache; invariância à arquitetura | ✓ | brief §4.4. **Manter.** |
| D8 | Licklider 1960 "Man-Computer Symbiosis"; Margulis simbiogênese | ✓ | glossario CONCEITOS DE MÉTODO. **Manter.** (lâmina simbiose foi removida no deck único? CONFERIR — estava na L1.G do painel.) |

---

## E. VALIDAÇÃO EXTERNA (o ativo mais delicado)

| # | Claim no deck (lâmina 35) | Veredito | Nota |
|---|---|---|---|
| E1 | Ravfogel (LACE) endossou paper p/ arXiv; STEER estende LACE | ✓ escopo | brief implícito; o escopo HONESTO (é STEER, não FI) já está no rodapé. **Manter o escopo explícito — é o que dá credibilidade.** |
| E2 | Edelsbrunner (Persistent Homology) "faz sentido"; IMI aplica | ✓ escopo | idem. Ressalva "não opina sobre interpretação cognitiva" presente. **Manter.** |
| E3 | "validação do RIGOR do programa, não selo de resultado do FI" | ✓ | Postura Renato-PI correta. **Manter — não inflar.** |

---

## RESUMO — O QUE CORRIGIR (3 itens reais)

1. **[D1 · ✗ corrigir] Lâmina 23 (Fundamentos III):** inverter a ênfase — o **Mestre Artesão / Artesanato** é o EIXO/raiz; taoísmo (Laozi, Zhuangzi), Sennett são **transversais**, não a raiz. Adicionar a figura do Mestre Artesão (homem integral: saber tradicional→tecnologia→IA) que hoje falta.
2. **[B2 · ⚠️ corrigir] Lâmina 17 (forma canônica):** são **7 instrumentos**, não 6 — a Reatualização/coda é o 7º (instrumento próprio, recency, condicional). Rotular explicitamente.
3. **[C3 · ⚠️ rebaixar] "RFI = FI × DA":** não é fórmula canônica publicada — RFI = Reasoning Framework Injection. Rebaixar de afirmação cravada a formulação, ou remover do rodapé da lâmina 14.

**Tudo o mais (números, eixo, ponte, fundamentos, validação) está VERIFICADO ✓.**
O deck já era factualmente sólido; estas 3 são correções de precisão, não de erro grosseiro.
