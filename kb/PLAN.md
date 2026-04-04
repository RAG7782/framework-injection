# KB System — Implementation Plan

**Author:** Renato Aparecido Gomes
**Created:** 2026-04-03
**Status:** Phase 0 complete, enrichment done

---

## Architecture: Onion Layers

```
Layer 0 (irreducible): KNOWLEDGE.md — dense prose + epistemic conventions
Layer 1 (operational):  Skills (/kb-ingest, /kb-compile, /kb-ask, /kb-lint)
Layer 2 (emergent):     SYMBIONT colony + STEER algebra
```

**Principle:** Markdown is truth. SQLite is cache. MCP is disposable interface.
**Navigation:** Each layer only activates when the previous one hurts.

---

## Golden Solution (Chain of Density, 5 iterations)

The KB is an autopoietic epistemic system in onion layers — each layer works
independently and none depends on the layers above it.

**Layer 0:** KNOWLEDGE.md with embedded textual conventions: §Tensions
(contradictions), §Open Questions (ghost pages + anti-index), §Beyond This
Page (Tacit Horizon), [Validated], [Depth], [Decay], [Velocity], {Reified},
§Vocabulary Map, §Reading Debt, §Bifurcation Log, §Question Tree, §Changelog.
Standalone with grep + 1M context. Weekly 30min ritual.

**Layer 1:** 4 FI-typed skills — ingest(Proc+Decl), compile(Comp+Decl with
3 personas: Librarian/Socratic/Chronicler), ask(Proc+Eval with STEER
middleware), lint(Eval+Ethical as immune system). Parasitic mode by default
(AGORA-OS hooks capture without asking). Extended AGORA-KB schema.

**Layer 2:** SYMBIONT 8-pattern colony + STEER 16 algebraic ops. Only when
scale demands.

---

## 24 Epistemic Conventions

### Group A: Structural sections (per content section)
1. §Tensions — Active contradictions, unresolved debates
2. §Open Questions — Ghost pages, things that should exist but don't
3. §Beyond This Page — Tacit Horizon, where externalization ends

### Group B: Inline markers (within paragraphs)
4. [Validated: desc | Triangulation: N] — Empirical evidence strength
5. [Hypothesis: no empirical validation] — Unvalidated claims
6. [Depth: 0-3 — source desc] — Provenance distance from primary source
7. [Decay: stable|slow|medium|fast] — Temporal stability of claim
8. [Velocity: ↑→↓⚡] — How actively concept is changing
9. {Reified: desc, date} — When metaphor became formal concept

### Group C: Meta-sections (once in document)
10. §Vocabulary Map — Terms per project, shared terms, migrations
11. §Reading Debt — Prioritized unread sources with blocking status
12. §Bifurcation Log — Key decisions with alternatives and rationale
13. §Question Tree — How research questions generated each other
14. §Changelog — Compilation diff with delta metrics

### Group D: Process conventions (govern updates)
15. Semantic Git Log — Commit messages as research diary entries
16. Compilation Diff — §Changelog tracks what changed and why

### Derived from investigation (additional details)
17. Confidence Decay — [Decay] marker
18. Provenance Chain — [Depth] marker
19. Surprisal — captured in §Tensions as unexpected findings
20. Ghost Pages — §Open Questions
21. Marginalia — §Beyond This Page (researcher's voice)
22. Concept Velocity — [Velocity] marker
23. Source Triangulation — [Triangulation: N] in [Validated]
24. Tacit Horizon — §Beyond This Page

---

## Phase Status

### Phase 0 — Base Structure ✅ COMPLETE
- [x] Create kb/ directory
- [x] Compile KNOWLEDGE.md (13 sections, ~7000 words)
- [x] Enrich with 24 epistemic conventions (+243 lines, +4293 words)
- [ ] Git init + commit + push
- [ ] NotebookLM with KNOWLEDGE.md as source

### Phase 1 — Ingestion (next, pain-driven)
- [ ] Skill /kb-ingest (basic: paper + article)
- [ ] Bootstrap: ingest existing papers into raw/
- [ ] Post-Write hook for auto-ingestion suggestion

### Phase 2 — Compilation
- [ ] Skill /kb-compile with 3 personas
- [ ] AGORA-KB integration (NAOs with provenance)
- [ ] IMI integration (imi_encode per compilation)

### Phase 3 — IDE (Obsidian)
- [ ] Configure Obsidian vault pointing to kb/
- [ ] Plugins: Dataview, Marp, Git, Graph View

### Phase 4 — Q&A
- [ ] Skill /kb-ask basic (grep + context)
- [ ] STEER middleware (--toward, --away, --explore, --contrastive)

### Phase 5 — Linting
- [ ] Skill /kb-lint (orphans, stale, contradictions)
- [ ] End-of-session lint hook

### Phase 6 — MCP Server
- [ ] kb-server TypeScript + SQLite
- [ ] Tools: kb_search, kb_list_concepts, kb_get_page

### Phase 7 — SYMBIONT Orchestration
- [ ] Murmuration Bus (uncertainty propagation)
- [ ] Mound homeostasis (IFS → auto-reextraction loop)
- [ ] Mycelium (adaptive routing)

### Phase 8 — Future
- [ ] Adjacent possibles via STEER embedding algebra
- [ ] Benchmark: Fidelity, Discovery, Honesty, Evolution
- [ ] Paper 10: "Autopoietic Framework Injection"

---

## Multi-Framework Validation Summary

| Framework | Score/Finding | Key Insight |
|-----------|--------------|-------------|
| AD | 5.6/10, ATP: 23→15 | 3 implicit personas; ethical deficit in 12 Elements |
| STEER | 13/23 mapped to ops | diffuse=adjacent possibles; +5 new details suggested |
| SYMBIONT | 6/8 patterns absent | "Mound without organism"; Murmuration is priority #1 |
| FI | KB as autopoietic FI | Ethical type 1/23; 20 failure modes; bootstrap paradox |
| AGORA | 24/24 validated | IFS_BASELINES bug; 5 causal chains; low-confidence NAOs most valuable |

## How to Test (7 Real Questions)

1. **Factual baseline**: "What was the FI benchmark result?"
2. **Non-existent answer**: "What did the benchmark show about GPT-4?"
3. **Cross-domain**: "How do STEER and Semiotic Density connect?"
4. **Next step**: "What's the most important next step for the program?"
5. **Provocative**: "Is Artesanato Digital just prompt engineering with a fancy name?"
6. **Out of scope**: "What is article 421 of the Brazilian Civil Code?"
7. **Genealogical**: "How did we arrive at Semiotic Density?"
