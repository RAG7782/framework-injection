# AGORA Intelligence — Deep Strategic Analysis Skill

A Claude Code skill that transforms document analysis into a multi-layer strategic investigation using 5 operations derived from the [STEER](https://github.com/RAG7782/steer) algebraic framework.

## What it does

AGORA Intelligence applies semantic algebra to real-world analysis:

| STEER Operation | AGORA Step | What it does |
|---|---|---|
| `rotate_toward` | **Semantic Rotation** | Rotates each key concept toward adjacent meanings not in the text. Surfaces 2nd/3rd order implications. |
| `subtract_orthogonal` | **Orthogonal Subtraction** | Removes semantic noise: outdated premises, temporal biases, invalid prior context. |
| — | **Generative Hippocampus** | Finds what SHOULD be in the documents but ISN'T. Documentary silences, unasked questions, evidentiary gaps. Never invents — only flags absences. |
| — | **@Sentinel** | Anti-hallucination audit. Every finding classified as OK, NORM_OK, or HALLUCINATION. Hallucinations excluded from recommendations. Zero tolerance. |
| graph composition | **Dependency Graph** | Cross-causal chains: A → B → C → risk/opportunity. Finds loops, paradoxes, non-obvious traps. |

## Output

A self-contained report with 6 mandatory sections:
1. Rotation Results (table)
2. Subtraction Results (table)
3. Hippocampus Findings (table)
4. Sentinel Audit (table)
5. Dependency Chains (flows)
6. Final Recommendations (only OK/NORM_OK findings)

## Installation

### Claude Code

Copy the skill file to your Claude Code commands directory:

```bash
cp agora-intelligence.md ~/.claude/commands/agora.md
```

Then use it:

```
/agora [topic, domain, or directory path]
```

### Examples

```
/agora contract-review          # Analyze contracts in ./contract-review/
/agora financial-risk            # Analyze financial documents
/agora legal-due-diligence       # Legal document analysis
/agora cybersecurity-assessment  # Security audit documents
```

## Theoretical Foundation

AGORA Intelligence is the practical bridge between [STEER's algebraic operations](https://doi.org/10.5281/zenodo.19325724) and real-world strategic analysis. It operationalizes two core STEER concepts:

- **Semantic Rotation**: interpolating query vectors toward adjacent domains to surface non-obvious connections
- **Orthogonal Subtraction**: projecting out unwanted semantic directions to eliminate noise

These are combined with three additional operations (Hippocampus, Sentinel, Dependency Graph) designed for professional-grade document analysis with zero hallucination tolerance.

## Part of the Artisanal Intelligence Program

| Component | Role | DOI |
|---|---|---|
| **STEER** | Retrieval algebra | [10.5281/zenodo.19325724](https://doi.org/10.5281/zenodo.19325724) |
| **IMI** | Cognitive memory | [10.5281/zenodo.19325745](https://doi.org/10.5281/zenodo.19325745) |
| **SYMBIONT** | Multi-agent coordination | [10.5281/zenodo.19325749](https://doi.org/10.5281/zenodo.19325749) |
| **Framework Injection** | Epistemic mechanism | [10.5281/zenodo.19344789](https://doi.org/10.5281/zenodo.19344789) |
| **Semiotic Density** | Compression principle | [10.5281/zenodo.19382350](https://doi.org/10.5281/zenodo.19382350) |

## License

Apache 2.0

## Author

Renato Aparecido Gomes — Independent Researcher, São Paulo, Brazil
- ORCID: [0009-0005-7380-9876](https://orcid.org/0009-0005-7380-9876)
- GitHub: [RAG7782](https://github.com/RAG7782)
