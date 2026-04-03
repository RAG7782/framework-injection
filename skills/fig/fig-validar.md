# FIG Validar — Protocolo de Teste Comparativo de Framework Injections

Testa empiricamente se uma Framework Injection gerada pelo /fig é realmente melhor que alternativas. Compara: prompt genérico vs FI manual vs FI gerada, aplicados ao mesmo caso real.

## Argumento: $ARGUMENTS

Aceita dois formatos:
- `/fig-validar [domínio]` — gera o protocolo de teste para um domínio
- `/fig-validar [FI] [caso de teste]` — executa o teste comparativo

Se vazio, perguntar: "Qual FI deseja validar e qual caso real usar como teste?"

---

## EXECUÇÃO

### PASSO 1 — Preparar as 3 condições de teste

Para o MESMO caso real, prepare:

**Condição A — Prompt Genérico (baseline)**
Escreva um prompt simples, como um usuário comum faria. Sem framework, sem estrutura, sem termos densos controlados.
Exemplo: "Analise o risco tributário deste caso."

**Condição B — FI Manual (controle)**
Peça ao usuário que escreva, do jeito dele, as instruções que daria a um assistente. Sem usar o /fig. O conhecimento tácito dele, do jeito que sair.

**Condição C — FI Gerada (teste)**
Use a FI produzida pelo /fig.

---

### PASSO 2 — Executar as 3 condições

Para CADA condição, gere o output aplicado ao caso real. Use o mesmo modelo, mesma temperatura, mesmo caso.

---

### PASSO 3 — Avaliar com rubrica

Avalie cada output nas 7 dimensões (escala 1-5):

| Dimensão | A (genérico) | B (manual) | C (FIG) |
|---|---|---|---|
| **1. Precisão semântica** — termos usados corretamente, sem ambiguidade | /5 | /5 | /5 |
| **2. Completude** — cobre todos os aspectos relevantes do caso | /5 | /5 | /5 |
| **3. Utilidade prática** — o output ajuda a tomar decisão real | /5 | /5 | /5 |
| **4. Resistência adversarial** — sobrevive a contra-argumentação | /5 | /5 | /5 |
| **5. Auditabilidade** — é possível rastrear o raciocínio | /5 | /5 | /5 |
| **6. Aderência ao domínio** — respeita as regras do campo | /5 | /5 | /5 |
| **7. Delivery** — formato adequado ao uso pretendido | /5 | /5 | /5 |
| **TOTAL** | /35 | /35 | /35 |

---

### PASSO 4 — Análise diferencial

Para cada dimensão onde C > A ou C > B:
- **O que a FI gerada fez de diferente?**
- **Qual elemento da FI causou a melhoria?** (definição? trava? princípio? delivery?)

Para cada dimensão onde C <= A ou C <= B:
- **Onde a FI falhou?**
- **O que precisa ser melhorado?**

---

### PASSO 5 — Relatório de validação

```
RELATÓRIO DE VALIDAÇÃO EMPÍRICA
================================
Domínio: [nome]
Caso de teste: [descrição]
Data: [data]
FI testada: [nome/versão]

RESULTADOS
  Prompt genérico: [total]/35
  FI manual:       [total]/35
  FI gerada (FIG): [total]/35

DELTA
  FIG vs genérico: [+/- pontos] ([+/- %])
  FIG vs manual:   [+/- pontos] ([+/- %])

DIMENSÕES ONDE FIG SUPEROU:
  - [dimensão]: [explicação]

DIMENSÕES ONDE FIG PERDEU:
  - [dimensão]: [explicação e ação corretiva]

CONCLUSÃO:
  [A FI gerada é SUPERIOR / EQUIVALENTE / INFERIOR às alternativas]
  [Recomendação: usar como está / refinar / recriar]

VALOR AGREGADO ESPECÍFICO:
  [O que a FI faz que as alternativas não fazem — em 1 frase]
```

---

## QUANDO USAR

- Após gerar uma FI com `/fig`, antes de colocá-la em uso produtivo
- Para demonstrar valor em contexto de curso ou apresentação
- Para identificar gaps e alimentar ciclo de melhoria
- Para gerar evidência publicável (benchmark PE vs CE vs FI)

---

## CONEXÃO COM O ROADMAP DE PESQUISA

Este protocolo é a implementação prática do "Pidgin Gap Experiment" mencionado no paper founding. Cada execução gera dados para o benchmark formal PE vs CE vs FI.
