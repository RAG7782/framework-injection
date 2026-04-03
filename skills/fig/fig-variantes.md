# FIG Variantes — Gerador de Versões de Framework Injection

Transforma uma Framework Injection temperada em versões calibradas para contextos, públicos e formatos diferentes. Cria uma biblioteca de variações a partir de um núcleo validado.

## Argumento: $ARGUMENTS

Se chamado pelo `/fig`, recebe a FI temperada. Se standalone: "Cole a Framework Injection que deseja adaptar em variantes."

---

## EXECUÇÃO

### PASSO 1 — Análise do núcleo invariante

Identifique o que NÃO PODE mudar entre variantes:
- Princípios inegociáveis
- Definições críticas
- Cercas e exclusões
- Critérios de qualidade fundamentais

Identifique o que PODE ser adaptado:
- Nível de profundidade
- Vocabulário (técnico vs. acessível)
- Formato de delivery
- Tom (professoral, executivo, litigioso, didático)
- Extensão
- Grau de formalidade

---

### PASSO 2 — Geração de variantes

Gere as variantes solicitadas (ou, se não especificado, gere as 5 padrão):

**Variante 1 — Técnica (para especialistas)**
- Vocabulário denso, sem explicações básicas
- Delivery conciso, alta precisão
- Presume domínio do campo

**Variante 2 — Didática (para ensino/curso)**
- Vocabulário acessível com termos técnicos explicados
- Exemplos em cada conceito
- Delivery progressivo (simples → complexo)

**Variante 3 — Executiva (para decisores)**
- Foco em implicações práticas e recomendações
- Delivery: resumo executivo + detalhamento sob demanda
- Tom direto, sem academicismo

**Variante 4 — Litigiosa (para peças jurídicas/confronto)**
- Tom assertivo com fundamentação
- Delivery: tese → fundamentação → aplicação → refutação
- Inclui antecipação adversária

**Variante 5 — Agente permanente (para system prompt)**
- Otimizada para tokens (compacta)
- Autocontida (sem dependências externas)
- Inclui autoauditoria embutida

---

### PASSO 3 — Validação cruzada

Para cada variante, verifique:
- [ ] O núcleo invariante foi preservado?
- [ ] A adaptação não introduziu ambiguidade nova?
- [ ] A variante funciona standalone (sem precisar das outras)?
- [ ] O delivery está coerente com o público-alvo?

---

## FORMATO DE SAÍDA

Para cada variante:
1. **Nome e público-alvo**
2. **Framework Injection completa** (texto pronto)
3. **O que mudou vs. a versão base** (diff semântico)
4. **Checklist de validação** (preenchido)

Ao final:
5. **Tabela comparativa** das variantes (dimensões que mudam)
