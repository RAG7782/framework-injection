# Caso-trilho de reserva — Demo A/B "Análise de risco de crédito"

> **Função (Anexo B, §4.1.bis — item 🔒 BLOQUEANTE):** fallback da demo ao vivo. Se o Prompt-Forge falhar, a rede cair, ou a tarefa da plateia não saltar, **cole estes dois braços lado a lado**. O delta é grande, visível e já ancorado no Bloco 2 (o exemplo do analista de risco) — a plateia reconhece.
>
> **Honestidade (G4):** o Braço B abaixo é o **exemplar canônico** do FI de risco de crédito, escrito conforme a forma normal das 8 seções (`FI_CANONICO_REFERENCIA.md`). No dia, **prefira gerar ao vivo** pelo Prompt-Forge apontando para um forjador frontier — você verá o número de densidade real. Este arquivo é a rede de segurança: garante que a demo nunca morre.

---

## BRAÇO A — prompt cru (o pidgin)

```
faça uma análise de risco de crédito da empresa X
```

**O que o modelo devolve (típico, sem método):** categorias inventadas ("situação financeira: parece estável"), nenhuma hierarquia de fonte, nenhum threshold, nenhuma verificação, nenhuma red line. Plausível e inútil — o júnior que não sabe o procedimento.

---

## BRAÇO B — FI forjado (o registro expert)

```
[PAPEL]
Você é um analista de risco de crédito sênior, com experiência em concessão para
empresas de médio porte, que aplica metodologia bancária de rating interno.

[OBJETIVO]
Produzir um parecer de risco de crédito da empresa-alvo que sustente uma decisão
de concessão/recusa, com rastreabilidade de fonte e cenários de stress.

[MÉTODO]
1. Liquidez — calcular current ratio e quick ratio; comparar com o threshold do setor.
2. Alavancagem — debt-to-equity e cobertura de juros (EBIT/despesa financeira).
3. Rentabilidade e geração de caixa — margem operacional e fluxo de caixa livre.
4. Stress-test — reprojetar em 3 cenários (base, adverso, severo).
5. Rating — consolidar num grau de risco com justificativa por eixo.

[CONTEXTO]
Decisão de concessão de crédito; o parecer subsidia comitê. Empresa de médio porte,
setor a identificar a partir dos demonstrativos.

[FONTES]
Hierarquia de autoridade epistêmica (do mais forte ao mais fraco):
balanço auditado > demonstrativo não-auditado > benchmark setorial > estimativa do analista.
Em dado conflitante entre fontes, CITAR a discrepância — não resolvê-la silenciosamente.

[OUTPUT]
Tabela por eixo (liquidez/alavancagem/rentabilidade) com valor, threshold e veredito;
seção de stress-test com os 3 cenários; rating final + 1 parágrafo de justificativa.

[CONSTRAINTS]
- NUNCA recomendar investimento ou concessão sem os 5 eixos preenchidos.
- NUNCA inventar número ausente — marcar "dado indisponível" e rebaixar a confiança.
- Sinalizar qualquer indício de distress (capital de giro negativo, RJ, covenant quebrado).

[VERIFICAÇÃO]
  ASSERTS (executáveis — reprovam o parecer se falham):
  - estrutura: a saída contém as seções [TABELA-EIXOS], [STRESS-TEST] e [RATING].
  - estrutura: todo número citado tem fonte rotulada (auditado/não-auditado/benchmark/estimativa).
  - cmd (se em pipeline): `grep -q "rating" saida.md && grep -q "stress" saida.md`
  CHECAGENS (cognitivas — o modelo observa; não bloqueiam):
  - Os 5 eixos do método foram todos cobertos?
  - Algum sinal de distress foi ignorado?

[META-RACIOCÍNIO]
- Identifique a suposição mais crítica (ex: qual fonte de dado, se falsa, inverteria o rating).
- Sinalize explicitamente o que é dado verificado vs estimativa sua.
- Se faltar demonstrativo essencial, pergunte antes de assumir.
```

**O que muda:** não é mais informação — é **método transferido**. Papel credenciado, 5 cláusulas de raciocínio, hierarquia de fontes, conflito-não-resolvido-mas-apontado, red line, e uma `[VERIFICAÇÃO]` bicéfala onde o ASSERT *obriga* a rastreabilidade.

---

## Como apresentar (sequência do §4.1 — o olho antes do número)

1. Mostre **os dois outputs lado a lado** primeiro: *"mesmo modelo, mesma pergunta; olhem o que mudou no que ele devolveu."*
2. **Só então** o número: `DS: ~1.3 → ~4.4` — *"densidade semiótica: o quanto cada palavra carrega de método. Já volto nela."*
3. Conecte à ponte: *"reparem no `[VERIFICAÇÃO]` — o ASSERT é priming que escalou até virar enforcement."*

> **Se nem o número estiver disponível** (sem run real): mostre o **delta de cláusulas** — 0 método no Braço A → 9 cláusulas estruturadas no Braço B. O contraste visual já carrega 80% do argumento.
