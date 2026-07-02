# INDEX — Framework Injection / Artesanato Digital

> **Mapa-mestre de tudo sobre Framework Injection (FI) na máquina.**
> Este repo (`~/experimentos/research/framework-injection/`) é o **canônico** da pesquisa.
> Alguns artefatos vivem fora dele (ferramenta operacional, aplicações, memória do Hermes) —
> este índice diz **onde está cada coisa** para nada ficar disperso.
>
> Gerado em 2026-07-02 por varredura de disco + `00-programa.md` do Hermes. Manter atualizado.

---

## 0. Definição canônica (a tese em 1 parágrafo)

**Framework Injection (FI):** mecanismo epistêmico de **transferência unidirecional de métodos
completos de raciocínio** específicos de domínio, do expert humano para o modelo/agente de IA,
codificados em **linguagem natural**, injetados **antes da inferência** como **substrato cognitivo
persistente**. Inclusão estrita: **PE ⊂ CE ⊂ FI** (Prompt Eng.=comandar/receita · Context Eng.=informar/cozinha · FI=educar/ensino). *Não se comanda a IA: educa-se.*

Eixo operacional central: **priming ↔ enforcement** (induz/estocástico ↔ obriga/determinístico —
"a placa pede, a catraca obriga"). Verificador externo (`grep -q`, exit code) = prova, não confiança.

> Postura de comunicação: **Renato PI** (humildade metodológica; conclusivo ✓ vs. em aberto 🔬 sempre
> separados; toda afirmação numérica com fonte real). Skill: `~/.aiox/skills/core/renato-pi/SKILL.md`.

---

## 1. Mapa dos 6 eixos (onde está cada coisa)

| Eixo | O que é | Localização canônica | Status |
|---|---|---|---|
| **A. Pesquisa/Papers** | papers fundacionais .tex/.pdf | **este repo** (raiz) + `research/papers/paper*` | canônico aqui |
| **B. Programa/Conceito** | a forma de pensar + estado do programa | `~/.hermes/…/artesanato-digital-fi/00-programa.md` | canônico (Hermes) |
| **C. Aula** | palestra, slides, transcrição, kit-aluno | `aulas/2026-06-27-hub-sp/` (neste repo) | canônico aqui |
| **D. Skills didáticas** | 4 skills da forja (aula) | `~/.aiox/skills/aula/` + cópia em `aulas/…/KIT-ALUNO/skills/` | canônico em `.aiox` |
| **E. Aplicações FI** | 71 FIs por área jurídica | `~/experimentos/applied/framework-injections/` | canônico (fonte-mestra) |
| **F. Ferramenta (PromptForge)** | motor que gera FI | `~/.aiox/tools/prompt-forge/` (produção) | ver §6 |

---

## 2. Eixo A — Papers (pesquisa)

### Neste repo (raiz) — fontes .tex + PDF compilado
- `paper.tex` — **Framework Injection: Teaching AI How to Think, Not What to Do** (comparative analysis)
- `artesanato-digital.tex` — **Digital Craftsmanship: A Semiotic Framework…**
- `founding-paper.tex` / `founding-paper-pt.tex` — paper fundador (EN/PT)
- `semiotic-density-paper.tex` — Densidade Semiótica
- `l2-computational-formalization.tex` · `d1-paper-draft.tex` · `paper-pt.tex` · `versao-portugues.md`
- `ontological-analysis.md` · `semiotic-density-analysis.md` · `sde-functional-embeddings-semantic-compute.md`
- `kb/KNOWLEDGE.md` (base de conhecimento do AIP) · `kb/PLAN.md`

### Build dirs isolados (em `research/papers/`) — compilam o mesmo texto
- `paper6-artesanato-digital/paper-v2.tex` — Digital Craftsmanship **v2** (camada "Delegated Intentionality") · ATIVO (working copy do texto v2)
- `paper7-framework-injection/` — build standalone do paper FI · ARQUIVO-MORTO (recompilar do repo)
- `framework-injection-repo/` — **clone divergente** do mesmo GitHub (`RAG7782/framework-injection`), linha da v2 · ⚠️ reconciliar com `git log`/merge antes de descartar

### Corpus publicado (Zenodo) — linha FI direta (DOIs)
Framework Injection `19479916` · Founding `19344789` · Semiotic Density `19645955` ·
SDE Encoding `19887868` · Delivery Architecture `19939303` · Adaptive FI `20040726` ·
AFD `20355340` · CMP `20355372` · Digital Craftsmanship `19479926`.
Calendário completo: `~/experimentos/research/papers/CALENDARIO-ZENODO-2026.md`.

---

## 3. Eixo B — Programa de pesquisa (conceito canônico)

**`~/.hermes/segundo-cerebro/projetos/artesanato-digital-fi/00-programa.md`** — o documento-mãe
do programa: forma de pensar (Renato PI), definição canônica, 5 modalidades, 8 seções, enquadramento
lakatosiano (núcleo/cinturão/borda), fundamentação bibliográfica em camadas, e **estado das evidências**:
- **+140%** densidade do input (1,86→4,47, n=435 reais) — ✓ direcionado
- **85–92%** preferência às cegas pelo output FI vs. 0–2% comando cru (n=49, 3 famílias) — ✓ direcionado
- Posicional / Adaptive-FI / banda de comprimento — 🔬 em aberto (não "nulo")

Fundamentos teóricos DS v2: `~/experimentos/research/aip-v2-goldberg/` (git, canônico:
`FOUNDATIONS-v2.md`, `CxG-FI-BRIDGE.md`, `DSc-DSd-DISTINCTION.md`, `CROSS-PREDICTIONS.md`).
⚠️ Existe cópia antiga menor em `~/experimentos/aip-v2-goldberg/` (topo) — arquivo-morto.

---

## 4. Eixo C — Aula (neste repo)

**`aulas/2026-06-27-hub-sp/`** — aula HUB SP (≈4h46). Ver `aulas/2026-06-27-hub-sp/README.md`.
- `transcricao-completa.md` (fonte canônica) · `destilacao.md` · `resumo-executivo.md`
- `FONTE-video-youtube.md` (vídeo `zlCCYKeWo58`, trecho de 2h30)
- `derivados/` — 2 podcasts NotebookLM (debate priming↔enforcement · peer-review crítico)
- `material-didatico/` — slides (HTML+PDF), roteiro AULA.md, conceitos, glossário, briefs, casos,
  `KIT-ALUNO/` (skills + promptforge.py + materiais), `assets/img/`
- `audio-original/` — 2 `.m4a` (no disco, gitignored)

---

## 5. Eixos D — Skills

### Skills didáticas (aula) — canônico em `~/.aiox/skills/aula/`
Fluxo da forja: **forja → mede → enforce → tempera**
- `fi-forja` — gera o FI canônico (8 seções + 7 instrumentos) a partir de pedido cru
- `ds-meter` — mede densidade semiótica (1.0–5.0) + justifica; modo comparação antes/depois
- `fi-enforce` — acha priming vs enforcement (teste de 3 perguntas) e cria os asserts externos
- `fi-tempera` — ataca o FI para fortalecê-lo (forjar→martelar→recozer→resfriar; autor vs auditor)

> Cópia entregue ao aluno: `aulas/2026-06-27-hub-sp/material-didatico/KIT-ALUNO/skills/`.

### Skills operacionais (neste repo, `skills/`)
`agora-intelligence` · `fig` · `juridicas` · `lapidacao` · `prompt-forge` (wrapper slash-command)

---

## 6. Eixo E — Aplicações FI

**`~/experimentos/applied/framework-injections/`** — **fonte-mestra**, 71 FIs por área
(sem git). Categorias: escritório-especialista por ramo jurídico · suite OXÉ (19 agentes) ·
verticais "-ia" · ESG/cripto/carbono · ferramentas · meta/qualidade. Cada FI: `fi-v1.md`,
`fi-v3-temperada-atp.md`, `governanca.md`.

**Deploy:** `~/oxe/integrations/framework-injections/` — subconjunto (22) só com a versão
temperada final. ⚠️ `~/experimentos/tools/oxe/integrations/framework-injections/` está **vazio** (placeholder).

---

## 7. Eixo F — PromptForge (a ferramenta) — 3 estágios de maturidade

| Cópia | O que é | Status |
|---|---|---|
| `~/.aiox/tools/prompt-forge/` | engine modular em **produção** (daemon, verify-gate, A/B posicional) | **canônico operacional** (mais recente, 30/jun) |
| `~/experimentos/promptforge/` | CLI single-file (`promptforge.py`, 670L) — **repo git de lançamento** | canônico de referência (git, 08/jun) |
| `skills/prompt-forge/SKILL.md` (neste repo) | wrapper slash-command do pipeline | derivado |

Não são duplicatas byte-a-byte — são estágios (launch → produção → skill).

---

## 8. Consolidação — FEITO em 2026-07-02

Duplicatas mortas arquivadas em **`~/experimentos/research/_arquivo-morto-fi/`** (reversível, ver README de lá):
- ✅ **`framework-injection-repo`** (clone divergente) → arquivado. A v2 já vive em `paper6/` (mais recente); só o histórico git dos 3 commits era exclusivo, preservado no `.git` movido.
- ✅ **`~/experimentos/aip-v2-goldberg/`** (topo, snapshot antigo) → arquivado. Canônico é o de `research/`.
- ✅ **`paper7-framework-injection/`** (build-dir, `.tex` idêntico ao canônico) → arquivado.
- ✅ **`experimentos/tools/oxe/…/framework-injections`** (placeholder 0 bytes) → removido.

Não-duplicatas (mantidas):
- Duplicação de PromptForge em 3 lugares é **intencional** (estágios launch→produção→skill) — documentada em §7, não mesclar.
