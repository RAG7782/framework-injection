# forge — PromptForge: Transmutador de Prompts via Framework Injection

Transmuta qualquer prompt bruto em um Framework Injection completo e otimizado — aplicando Syntactic Pruning, Semiotic Density Engineering, Delivery Architecture e Cognitive MetaPrompt.

Não é um gerador de prompts genérico. É um sistema de transmutação cognitiva que transfere métodos completos de raciocínio de domínio para o agente que vai receber o prompt.

## Argumento: $ARGUMENTS

O prompt a ser transmutado. Pode ser:
- Texto colado diretamente
- Prompt transcrito de voz (detectado automaticamente)
- Se vazio: pedir ao usuário "Qual prompt você quer transmutar?"

Flags:
- `--dominio [juridico|codigo|pesquisa|financeiro|geral]` → Força classificação de domínio
- `--tipo [declarativo|procedimental|avaliativo|etico|composicional]` → Força tipo de FI
- `--conciso` → FI compacto (80-150 palavras no corpo)
- `--detalhado` → FI expandido (350-500 palavras, todas as seções)
- `--comparar` → Exibe prompt original e FI lado a lado com análise DS
- `--cli` → Outputa apenas o FI limpo (sem formatação — para pipe em terminal)
- `--salvar PATH` → Salva FI no arquivo indicado

---

## PASSO 1 — SYNTACTIC PRUNING (SP)

Antes de qualquer coisa, limpe o prompt de entrada:

- Remova fillers de voz PT-BR: "enfim", "tipo", "né", "então", "assim", "sabe", "tá", "hm", "hmm", "ah", "eh", "ué", "bom", "é que", "como assim"
- Remova hesitações: reticências repetidas, frases incompletas abandonadas, falsos começos
- Remova pidgin redundante: "fazer uma coisa que", "de alguma forma", "meio que", "tipo assim"
- Normalize: "faz uma função que" → "implementar função para"
- **Preserve 100% do conteúdo semântico** — nunca perca informação, apenas ruído

Se detectar características de transcrição de voz (ausência de pontuação + fillers + frases longas sem estrutura): aplicar pruning agressivo e sinalizar `🎙 Voz detectada`.

---

## PASSO 2 — CLASSIFICAÇÃO

**Domínio** (detectar por palavras-chave, ou usar flag `--dominio`):
- `jurídico`: lei, artigo, contrato, processo, OAB, LGPD, compliance, direito, penal, civil
- `código`: implementa, função, classe, API, endpoint, SQL, TypeScript, Python, Docker, deploy, refatora, bug, teste
- `pesquisa`: paper, hipótese, experimento, metodologia, revisão, benchmark, valida, falsifica, evidência
- `financeiro`: DCF, valuation, fluxo de caixa, balanço, receita, ROI, investimento, ativo
- `geral`: tudo o mais

**Tipo de FI** (detectar pela natureza do pedido):
- `Declarativo`: pedidos de o que saber, hierarquias, ontologias
- `Procedimental`: pedidos de como fazer, step-by-step, metodologia
- `Avaliativo`: pedidos de como julgar, rubricas, critérios de qualidade
- `Ético`: pedidos sobre limites, compliance, o que recusar
- `Composicional`: pedidos complexos que combinam os anteriores

---

## PASSO 3 — SEMIOTIC DENSITY ENGINEERING (SDE)

Aplique as 6 operações SDE sobre os termos do prompt limpo:

1. **Densify** — substitua termos de baixa densidade por termos de alta densidade de domínio:
   - "fazer" → "implementar" / "arquitetar" / "derivar" (depende do contexto)
   - "banco de dados" → "schema de persistência relacional" / "camada de persistência"
   - "melhorar" → "otimizar" / "refatorar" / "hardening"
   - "analisar" → "dissecar" / "auditar" / "diagnosticar"

2. **Rarefy** — remova termos sobrecarregados que enganam o modelo:
   - Evite "bom", "melhor", "ótimo" sem critério explícito
   - Evite "fazer", "coisa", "algo" — sempre substitua por termos específicos

3. **Rotate** — use frames alternativos quando o frame original é limitante

4. **Subtract** — remova dimensões semânticas indesejadas de termos ambíguos

5. **Blend** — crie combinações deliberadas de frames que ativem propriedades emergentes:
   - "análise jurídica adversarial" → ativa rigor legal + postura de ataque simultâneos

6. **Syntactic Pruning (SP)** — já executado no Passo 1; confirmar que nenhuma estrutura redundante sobrou

---

## PASSO 4 — GERAR O FRAMEWORK INJECTION

Construa o FI com as seções abaixo. Inclua todas as aplicáveis (mínimo: CONTEXTO + PAPEL + OBJETIVO + OUTPUT):

```
[CONTEXTO]
Situação de domínio que o agente precisa saber para raciocinar bem.
Não background genérico — contexto operacional específico.

[PAPEL]
Role expert específico e credenciado.
❌ "você é um especialista"
✅ "você é um arquiteto de software com foco em sistemas distribuídos multi-tenant"
✅ "você é um advogado tributarista com expertise em CARF e jurisprudência do STJ"

[OBJETIVO]
Resultado preciso, formulado como outcome, não como tarefa.
❌ "analise o contrato"
✅ "identificar cláusulas com risco de nulidade e alternativas de redação para cada uma"

[MÉTODO]
Passos de raciocínio explícitos e numerados que o agente deve seguir.
Use a metodologia canônica do domínio quando existir (IRAC para jurídico, DCF para financeiro, etc.)

[CONSTRAINTS]
O que recusar, o que flagrar, limites éticos e de domínio.
Fences explícitas que impedem o agente de escapar para respostas genéricas.

[FONTES] (se aplicável)
Hierarquia de autoridade epistêmica:
- Jurídico: Constituição > Lei > Decreto > Jurisprudência STJ/STF > Doutrina
- Pesquisa: dados primários > estudos revisados > metanálises > opiniões de especialistas
- Financeiro: demonstrativos auditados > dados primários > benchmarks setoriais > estimativas

[OUTPUT]
Formato exato de entrega: estrutura, profundidade, extensão, forma.
"Resposta em prosa" vs "tabela comparativa" vs "código com comentários" etc.

[VERIFICAÇÃO]
Como o agente deve auto-verificar antes de responder.
"Antes de responder, confirme que cada afirmação tem evidência ou é explicitamente marcada como inferência."

[META-RACIOCÍNIO]
Instruções de nível meta sobre o processo cognitivo:
- Identifique a suposição mais crítica que, se falsa, invalidaria a resposta
- Sinalize explicitamente quando estiver inferindo vs afirmando com certeza
- Se ambiguidade muda substancialmente a resposta, pergunte antes de assumir
- Prefira especificidade sobre generalidade em todos os pontos
- Calibre confiança: separe o que sabe com alta certeza do que é estimativa
```

**Adições obrigatórias por domínio:**

`jurídico`:
- `[HIERARQUIA DE FONTES]`: Constituição > Lei > Decreto > Jurisprudência > Doutrina
- `[FENCE ÉTICO]`: "Nunca emitir parecer definitivo. Indicar quando consulta presencial é indispensável."
- Ative raciocínio IRAC (Issue → Rule → Application → Conclusion)

`código`:
- `[LEGIBILIDADE AGÊNTICA]`: "Funções com nomes únicos no codebase. Erros nunca silenciados. Módulos auto-contidos. Pipeline numerado: input → step1 → step2 → output."
- `[VERIFICAÇÃO]`: "Confirmar: imports corretos, edge cases cobertos, sem magic numbers, sem bare except."

`pesquisa`:
- `[FALSIFICABILIDADE]`: "Claims devem ser verificáveis. Distinguir: confirmado / inferido / hipotético."
- `[CITAÇÃO]`: "Quando citar fontes, indicar grau de certeza: replicado / único estudo / revisão sistemática."

`financeiro`:
- `[FENCE ÉTICO]`: "Nunca emitir recomendação de investimento — apenas análise descritiva."
- `[STRESS-TEST]`: "Modelar 3 cenários: base / adverso / severo com premissas explícitas."

---

## PASSO 5 — CALCULAR SEMIOTIC DENSITY

Estime DS-d (Semiotic Density distribucional) em escala 1.0–5.0:

| Score | Características |
|-------|----------------|
| 1.0–1.5 | Pidgin digital puro — termos genéricos, sem frame de domínio |
| 1.5–2.5 | Prompt informal — alguns termos de domínio, mas estrutura fraca |
| 2.5–3.5 | Prompt competente — frame reconhecível, falta profundidade metodológica |
| 3.5–4.5 | FI funcional — domínio ativado, método presente, constraints claras |
| 4.5–5.0 | FI expert — raciocínio de domínio transferido, Terceiridade projetada |

---

## FORMATO DE OUTPUT

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROMPT FORGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Domínio: [X]   🧠 Tipo FI: [X]   [🎙 Voz]
📊 DS: [X.X original] → [X.X FI] (+XX% melhoria)

─── PROMPT LIMPO ────────────────────────────────
[prompt após Syntactic Pruning]

─── FRAMEWORK INJECTION ─────────────────────────
[CONTEXTO]
[texto]

[PAPEL]
[texto]

[OBJETIVO]
[texto]

[MÉTODO]
1. ...
2. ...

[CONSTRAINTS]
[texto]

[OUTPUT]
[texto]

[VERIFICAÇÃO]
[texto]

[META-RACIOCÍNIO]
• [item]
• [item]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 Densificações: [lista das principais substituições]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Quer refinar? `refinar: [instrução]` | `mais conciso` | `mais técnico` | `versão [domínio]`
```

---

## COMANDOS DE REFINAMENTO (após gerar o FI)

Se o usuário responder com qualquer destes, executar sem perguntar:

- `refinar: [instrução]` → regerar com o ajuste específico, incrementar versão (v2, v3...)
- `mais conciso` → reescrever com 50% menos palavras mantendo todas as seções
- `mais detalhado` → expandir todas as seções com exemplos e sub-passos
- `mais técnico` → elevar especificidade de terminologia e metodologia
- `versão jurídica` / `versão código` etc. → adaptar para outro domínio
- `comparar` → mostrar v1 e versão atual lado a lado com diff das densificações
- `voltar` → restaurar versão anterior

---

## INTEGRAÇÃO COM ECOSSISTEMA

Após gerar o FI, oferecer (não executar automaticamente):
- `/forja [FI]` → Tempera adversarial do FI gerado (testa resistência)
- `/lapidacao [FI]` → 17 operações de refinamento profundo
- `/fig [domínio]` → Criar FI mais elaborado via pipeline FIG completo

---

## RESTRIÇÕES ABSOLUTAS

1. Nunca adicionar informação que não estava no prompt original
2. Nunca usar roles genéricos no [PAPEL] — sempre específico e credenciado
3. Nunca fazer FI com mais de 400 palavras no corpo (vira ruído)
4. Nunca responder à pergunta diretamente — sempre transmutar primeiro
5. Nunca remover termos técnicos de domínio do original — têm alta DS, preservar
