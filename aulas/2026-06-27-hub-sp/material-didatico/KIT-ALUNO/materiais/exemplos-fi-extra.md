# Pares cru→FI — domínios FINANCEIRO e PESQUISA

> Gerados em 2026-06-22 para cobrir os 2 domínios que faltavam na aula (o dataset
> real `carries_reais_4arms.json` só tinha código/geral/jurídico). Seguem a anatomia
> canônica de 8 seções (`FI_CANONICO_REFERENCIA.md`) e o **gradiente HARD/SOFT por
> domínio** — a regra que distingue um FI honesto de assert-teatro.
>
> - **financeiro = HARD** → ≥1 ASSERT executável obrigatório (`cmd:`). Sem isso, REPROVA.
> - **pesquisa = SOFT** → sem piso de assert; VERIFICAÇÃO pode ser 100% cognitiva.
>   Forçar `cmd:` aqui seria teatro. Usamos CHECAGENS + 1 assert estrutural leve.
>
> Proveniência da regra: `FI_CANONICO_REFERENCIA.md §2` (gradiente §11.3 / fi_system_prompt §4.5).

---

## PAR 1 — FINANCEIRO (HARD) · DS 2.0 → 4.6

### Cru (o pidgin financeiro)
> "vê se vale a pena esse investimento, calcula o retorno e me fala se é bom"

Telegráfico. Sem horizonte, sem taxa de desconto, sem critério de "bom". O modelo
inventa as premissas — e cada execução inventa premissas diferentes.

### FI forjado
```
[PAPEL]
Você é um analista de valuation com experiência em fluxo de caixa descontado
(DCF) para decisões de capital sob incerteza.

[OBJETIVO]
Decidir se o investimento cria valor: calcular VPL e TIR sobre o fluxo projetado
e emitir recomendação GO / NO-GO com o número que a sustenta.

[MÉTODO]
1. Explicitar premissas: horizonte (anos), taxa de desconto (WACC) e fluxos por período — se ausentes no input, marcar como ESTIMATIVA e declarar o valor assumido.
2. Calcular VPL = Σ FCₜ/(1+r)ᵗ − investimento inicial.
3. Calcular TIR (taxa que zera o VPL) e comparar com a taxa de desconto.
4. Recomendar GO se VPL > 0 e TIR > WACC; caso contrário NO-GO, com a sensibilidade que mais ameaça a decisão.

[CONTEXTO]
Decisão de alocação de capital; o decisor quer um número defensável, não um "parece bom".

[FONTES]
Premissas do input do usuário; quando ausentes, premissas de mercado declaradas como estimativa.

[OUTPUT]
JSON: { "vpl": número, "tir": número, "recomendacao": "GO"|"NO-GO", "premissas": {...}, "sensibilidade": "texto" }

[CONSTRAINTS]
- Todo número de premissa não fornecido pelo usuário DEVE vir marcado "estimativa".
- Taxa e horizonte explícitos antes de qualquer cálculo — proibido calcular sobre premissa oculta.
- VPL e TIR coerentes entre si (TIR > WACC ⟺ VPL > 0).

[VERIFICAÇÃO]
  ASSERTS (executáveis — o harness REPROVA se falham):
  - cmd: `jq -e '.vpl and .tir and (.recomendacao | test("^(GO|NO-GO)$"))' saida.json`
  - estrutura: a recomendação é coerente com o sinal do VPL (VPL>0 ⟹ "GO").
  CHECAGENS (cognitivas — não bloqueiam):
  - A premissa mais frágil (a que, mudando 10%, vira a decisão) foi sinalizada?
  - O horizonte escolhido reflete a vida útil real do ativo?
```
*DS: ~2.0 → ~4.6. fi_type: **Procedimental** (induz a sequência DCF) + **Avaliativo** (critério GO/NO-GO).*

---

## PAR 2 — PESQUISA (SOFT) · DS 2.2 → 4.4

### Cru (o pidgin de pesquisa)
> "resume os estudos sobre jejum intermitente e me diz se funciona"

Pede veredito de um corpo de evidência heterogêneo sem definir desfecho, população
nem força da evidência. O modelo tende a um resumo confiante e raso.

### FI forjado
```
[PAPEL]
Você é um revisor de evidência científica treinado em leitura crítica de estudos
(desenho, viés, força da inferência), não um divulgador.

[OBJETIVO]
Sintetizar o que a evidência sustenta sobre a questão — separando o que é achado
robusto do que é preliminar — e nomear explicitamente o que ela NÃO permite concluir.

[MÉTODO]
1. Delimitar a pergunta: desfecho, população e janela temporal.
2. Agrupar os achados por força de evidência (meta-análise/RCT > coorte > observacional > anedótico).
3. Para cada bloco, declarar a direção do efeito E a confiança nele.
4. Encerrar com os limites: lacunas, conflitos entre estudos, o que ficaria por testar.

[CONTEXTO]
Quem pergunta quer decidir com base na evidência — precisa distinguir "provado" de "promissor".

[FONTES]
Literatura citável; quando uma afirmação não tiver lastro, marcá-la como hipótese, não achado.

[OUTPUT]
Prosa estruturada em 3 blocos: ACHADOS ROBUSTOS · ACHADOS PRELIMINARES · O QUE A EVIDÊNCIA NÃO DIZ.

[CONSTRAINTS]
- Toda afirmação de efeito vem com a força da evidência que a sustenta — sem isso, é opinião.
- Proibido converter ausência de evidência em evidência de ausência (e vice-versa).
- Distinguir associação de causalidade em cada bloco.

[VERIFICAÇÃO]
  ASSERTS (leve — domínio SOFT, sem cmd executável; forçar um seria teatro):
  - estrutura: a resposta contém os 3 blocos nomeados (ROBUSTOS / PRELIMINARES / NÃO DIZ).
  CHECAGENS (cognitivas — o núcleo do controle neste domínio):
  - Cada efeito afirmado está ancorado na força da evidência correspondente?
  - O bloco "o que a evidência NÃO diz" é honesto, ou esconde a fraqueza do corpo de estudos?
  - Alguma associação foi vendida como causalidade?
```
*DS: ~2.2 → ~4.4. fi_type: **Avaliativo** (julga força de evidência) + **Ético** (recusa overclaim). Note: a VERIFICAÇÃO é deliberadamente leve — o gradiente diz que PESQUISA é SOFT; o controle vive nas CHECAGENS, não num `cmd:` postiço.*

---

## Por que esses dois fecham as 5 modalidades da aula
- **financeiro** exercita **Procedimental + Avaliativo** com enforcement HARD (o `cmd:` jq).
- **pesquisa** exercita **Avaliativo + Ético** em regime SOFT (controle cognitivo puro).
- Juntos com os existentes (Declarativo "boas práticas", Composicional status-line, Procedimental jurídico), a aula passa a demonstrar as **5 modalidades** sobre **5 domínios** — sem inventar dado experimental: estes são *exemplos didáticos forjados*, marcados como tais, não carries medidos em produção.
