# Aula HUB SP — Artesanato Digital / Framework Injection

**Data:** 2026-06-27 · **Local:** HUB SP · **Palestrante:** Dr. Renato Aparecido Gomes
**Duração:** ≈4h46 (transcrição completa) · vídeo capturou ≈2h30
**Tema:** Framework Injection · eixo priming↔enforcement · densidade semiótica

> Aula-mãe do programa de pesquisa **Artesanato Digital**. Tese central: *parar de comandar
> a IA e passar a educá-la*. Pertence ao repo canônico do Framework Injection.

---

## Conteúdo desta pasta

| Arquivo | O que é | Fonte |
|---|---|---|
| `transcricao-completa.md` | **Transcrição integral da aula (≈4h46)** — fonte-texto canônica | HUB_SP orig. |
| `destilacao.md` | Mapa conceitual hierárquico + resumo estruturado + citações-ouro | HUB_SP orig. |
| `resumo-executivo.md` | 1 página: tese, modelo mental de 3 camadas, 5 movimentos práticos | HUB_SP orig. |
| `FONTE-video-youtube.md` | Link do vídeo (`zlCCYKeWo58`) + por que não retranscrevemos | proveniência |
| `material-didatico/` | **Material da aula**: slides, AULA.md, briefs, glossário, KIT-ALUNO (skills + promptforge), assets | `Aula FI` orig. |
| `audio-original/` | Os 2 `.m4a` originais dos podcasts derivados | Downloads |
| `derivados/` | Transcrições dos 2 podcasts (ver abaixo) | Whisper `small`, 2026-07-02 |

## Derivados — 2 podcasts (estilo NotebookLM) sobre o material

**NÃO são partes da aula** — são conteúdo *derivado* gerado a partir do material do Artesanato
Digital. Guardados aqui por serem material-de-aula reutilizável (divulgação, revisão da tese).

1. **`derivados/podcast-placa-catraca.transcricao.txt`**
   *"A placa pede mas a catraca obriga"* — debate **dialético** entre dois interlocutores sobre
   o eixo **priming ↔ enforcement**. Um sustenta que o LLM é irredutivelmente estocástico (tudo
   é priming); o outro que FI + validadores externos (`grep -q`, exit code) constroem a "catraca".
   Cobre: réu-e-juiz, densidade semiótica (selfie da girafa), poda≠resumo, coda densa,
   lost-in-the-middle, curva-J, 2001/HAL. ≈16 min.

2. **`derivados/podcast-domine-ia.transcricao.txt`**
   *"Domine a IA com o artesanato digital"* — sessão de **peer-review crítico** do material.
   Aponta 4 fraquezas + melhorias acionáveis:
   1. Reposicionar o pitch → foco B2B crítico (direito, medicina, finanças);
   2. Transformar o Lakatos (núcleo/cinturão/borda) em **gabarito visual** para as 5 modalidades;
   3. Abstrair a "catraca" **além do `grep`/bash** → structured output (JSON schema no CRM),
      arquitetura de **duplo-agente** (agente-B só emite verdadeiro/falso, não cria texto);
   4. Criar um **"teste de densificação"**: enviar o termo denso isolado ao modelo e ver se ele
      "acende a galáxia" (densidade distributiva real) vs. só densidade cultural humana.
   ≈15 min. → *contém sugestões concretas de melhoria para o paper/aula.*

---

## `material-didatico/` — o que foi criado e usado na aula

Material de ensino da aula (Academia Lendária / HUB SP). Estrutura:

**Slides & deck** (HTML canônico + PDF renderizado via `_gerar_pdf.mjs`):
- `slides-aula-fi-completo.html` — deck único, ordem da aula
- `slides-painel-fi-dark.{html,pdf}` — painel (parte teórica)
- `slides-workshop-fi-dark.{html,pdf}` — workshop (parte prática)

**Roteiro & conceitos:**
- `AULA — Framework Injection (Painel + Workshop).md` — roteiro-mestre da aula
- `CONCEITO — Artesanato Digital…md` · `CONCEITO — Priming e Enforcement (método Feynman).md`
- `FONTE-glossario.md` · `FONTE-classificacao-priming-enforcement.md` · `LAMINA-grep-ponte-enforcement.md`
- `caso-trilho-risco-credito.md` · `pares-fi-financeiro-pesquisa.md` — casos/exemplos
- `AUDITORIA-*.md` — auditorias didáticas/verbatim do conteúdo

**Diretoria & facilitação:**
- `BRIEF-DIRETORIA — Framework Injection.{md,html,pdf}` · `KIT-FACILITADOR.md` · `PLANO-3-SKILLS-aluno.md`

**`KIT-ALUNO/`** — o que o aluno leva para casa (ver `KIT-ALUNO/COMECE-AQUI.md`):
- `skills/` — **4 skills** da forja: `fi-forja` (gera FI) · `ds-meter` (mede densidade) ·
  `fi-enforce` (cria os asserts) · `fi-tempera` (ataca p/ fortalecer). *Fluxo: forja→mede→enforce→tempera.*
- `backend-opcional/` — `promptforge.py` + `requirements.txt` + `colab-fallback.ipynb`
- `materiais/` — cápsulas de reforço, cartão do aluno, exemplos de fluxo
- `referencia/` — glossário FI + conceitos

**`kit-entrega/`** — `colab-fallback.ipynb`, `README-prompt-forge.md`, `roteiro-video-90s.md`
**`assets/img/`** — 4 imagens da aula (forja-tempera, intenção-delegada, mármore-artesanato, ponte-eixo)

> Limpeza (2026-07-02): removidos 30 `.bak`, versões `ABANDONADO`/`NAO-USAR`, `.DS_Store` e o
> `KIT-ALUNO.zip` redundante (a pasta já está descompactada). Histórico de edição → git.

---

## Proveniência

- Originais da aula: `~/Downloads/2026.06.27_HUB_SP-Dr.RenatoGomes /` (transcrição + destilação + resumo).
- Material didático: `~/Downloads/Academia Lendaria - Hub SP/Aula FI/` (slides, kit-aluno, skills, briefs).
- Áudios derivados: `~/Downloads/*.m4a`; transcritos com OpenAI Whisper `small` (pt) em 2026-07-02.
- Organizado em 2026-07-02 (sessão Claude Code). Originais preservados em Downloads.
