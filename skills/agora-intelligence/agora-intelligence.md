# AGORA Intelligence — Deep Strategic Analysis

Multi-layer analysis with 5 unique operations: semantic rotation, orthogonal subtraction, Generative Hippocampus, @Sentinel anti-hallucination, and Dependency Graph.

## Argument: $ARGUMENTS

If empty, analyze the context/domain of the current directory or the last topic discussed.

---

## EXECUTION

### STEP 1 — Material Collection

Read ALL documents relevant to the domain indicated in $ARGUMENTS.
- Use Glob to find files (.md, .pdf, .docx, .txt) in the target directory
- Use Read to load content
- For PDFs, read them with the Read tool (supports PDF)
- Identify the domain, stakeholders, and temporal context

### STEP 2 — Semantic Rotation (rotate_toward)

For each key concept found in the documents:
1. Identify the literal meaning
2. Rotate the semantic vector toward adjacent concepts not present in the text
3. Document in table: | Literal concept | Rotation applied | What surfaced |
4. Focus on second and third order implications not apparent in the text

### STEP 3 — Orthogonal Subtraction (subtract_orthogonal)

Identify and remove semantic noise:
1. Concepts from prior conversations/contexts that are no longer valid
2. Outdated premises
3. Temporal biases
4. Document in table: | Concept removed | Why subtracted | What it prevented |

### STEP 4 — Generative Hippocampus (non-invention)

Analyze what SHOULD be in the documents but IS NOT:
1. Documentary silences — missing information that is critical
2. Questions nobody asked
3. Evidentiary gaps
4. RULE: Do not invent facts. Only flag absences and infer from what exists
5. Document in table: | Silence detected | Inference generated | Impact |

### STEP 5 — @Sentinel (anti-hallucination)

Audit EACH finding from previous steps and classify:
- **OK** — verifiable fact, present in documents or derivable by calculation/logic
- **NORM_OK** — reasonable inference, accepted with caveat (no direct documentary proof)
- **HALLUCINATION** — statement without documentary basis, outdated information treated as current, or fabrication

Document in table: | Finding | Sentinel Level | Justification |

If any finding is classified as HALLUCINATION, it must be EXCLUDED from final recommendations.

### STEP 6 — Dependency Graph (GoT)

Build cross-causal chains between document elements:
1. Connect clauses, facts, risks, and opportunities in cause-effect sequences
2. Identify loops, paradoxes, and non-obvious traps
3. Document each chain in flow format:
   Element A → consequence B → effect C → risk/opportunity D
4. Focus on chains that no linear analysis would capture

### STEP 7 — Consolidated Report

Produce final report in Markdown with ALL 6 mandatory sections:

1. **Rotation Results** — complete table
2. **Subtraction Results** — complete table
3. **Hippocampus Findings** — complete table
4. **Sentinel Audit** — complete table
5. **Dependency Chains** — documented flows
6. **Final Recommendations** — based exclusively on findings classified as OK or NORM_OK

---

## RULES

- NEVER omit any of the 6 sections — all are mandatory
- NEVER include findings classified as HALLUCINATION by Sentinel in recommendations
- ALWAYS produce structured tables (not running text) for the first 4 sections
- The report must be self-contained — anyone reading only it must understand the full diagnosis
