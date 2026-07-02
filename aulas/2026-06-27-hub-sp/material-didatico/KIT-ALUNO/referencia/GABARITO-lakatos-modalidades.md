# Gabarito Lakatosiano — onde cada modalidade mora no seu FI

> **O que esta página resolve** (apontamento do peer-review 2026-06-27): o aluno entende a
> epistemologia lakatosiana (núcleo/cinturão/borda) E entende as 5 modalidades, mas **trava
> na hora de montar o prompt** — não sabe onde encaixar cada modalidade. Este gabarito é a
> ponte: transforma a teoria num **layout de FI**. A teoria vira design de interface.
>
> **Lastro:** estrutura lakatosiana do programa (núcleo duro / cinturão protetor / borda) +
> as 5 modalidades do FI. `[AF]` o mapeamento modalidade→zona é uma proposta didática derivada
> desse material — usar como andaime (Vygotsky), não como dogma. Ajuste ao seu domínio.

---

## A ideia em uma frase

**As 5 modalidades não têm o mesmo peso.** Umas são inegociáveis (se a IA violar, você joga a
resposta fora); outras protegem o núcleo mas podem ser ajustadas; outras são só experimento.
Lakatos dá o nome dessas 3 camadas. Este gabarito diz qual modalidade vai em qual camada — **e
por quê**, porque um gabarito que só afirma o lugar de cada peça não ensina a mover a peça
quando o seu domínio não for igual ao do exemplo.

---

## O gabarito (as 3 zonas × as 5 modalidades)

```
┌─────────────────────────────────────────────────────────────────────┐
│  NÚCLEO DURO  ·  inegociável  ·  violou → DESCARTA a resposta inteira │
│  ───────────────────────────────────────────────────────────────────│
│  • DECLARATIVA  → o que a IA PODE saber (ontologia, hierarquia de     │
│                   fontes). Fora disso = alucinação → descarte.        │
│  • ÉTICA        → o que a IA NUNCA faz (guardrails, compliance).      │
│                   Cruzou a cerca = descarte.                          │
│  ▸ tende a ENFORCEMENT (precisa de gate externo que reprova)          │
├─────────────────────────────────────────────────────────────────────┤
│  CINTURÃO PROTETOR  ·  protege o núcleo  ·  ajustável se a IA travar  │
│  ───────────────────────────────────────────────────────────────────│
│  • PROCEDIMENTAL → COMO raciocinar (passo a passo, método=caminho).   │
│  • AVALIATIVA    → como JULGAR (rubricas, critérios de qualidade).    │
│  ▸ mistura PRIMING (o raciocínio) + ENFORCEMENT (a rubrica checável)  │
├─────────────────────────────────────────────────────────────────────┤
│  BORDA  ·  hipótese em teste  ·  quebrou aqui → NÃO quebra o sistema  │
│  ───────────────────────────────────────────────────────────────────│
│  • COMPOSICIONAL → como COMBINAR as anteriores (gradações, mix).      │
│  ▸ tende a PRIMING (é onde você EXPERIMENTA em runtime)               │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Por que cada modalidade mora onde mora (a defesa do mapeamento)

Um gabarito que só aponta "Declarativa → núcleo" é um dogma. O que te deixa **mover** a peça no
seu domínio é o **critério** que colocou ela lá. O critério é sempre o mesmo, e é a pergunta-teste
do núcleo: *"se a IA violar isto, eu jogo a resposta inteira fora?"*

| Modalidade | Zona | Por que ali (a razão, não a afirmação) |
|---|---|---|
| **Declarativa** | Núcleo | Define **o universo de fatos/fontes admissíveis**. Se a IA cita fonte fora da lista, tudo que veio depois está contaminado na raiz — não dá pra "ajustar", só descartar. É a ontologia; ontologia furada = resposta inválida, não resposta fraca. |
| **Ética** | Núcleo | É a **cerca de compliance/segurança**. Violação não é erro de qualidade, é passivo (jurídico, regulatório, reputacional). Não existe "meio compliance". Binária por natureza → núcleo. |
| **Procedimental** | Cinturão | Define o **caminho do raciocínio** (passo a passo). Se a IA pular um passo, a resposta fica pior, não inválida — e você pode **afrouxar** a ordem se ela travar, sem tocar no núcleo. Protege o núcleo (força o método) mas é revisável. |
| **Avaliativa** | Cinturão (com pé no núcleo) | É a **rubrica de qualidade**. Fica no cinturão porque a maioria das rubricas é gradual ("quão bem cobriu?"). **Mas quando a rubrica é binária** ("toda conclusão TEM número + fonte, sim/não"), ela vira `assert` e **sobe para o enforcement do núcleo**. É a modalidade de fronteira. |
| **Composicional** | Borda | É onde você **combina** as anteriores de um jeito novo ("se faltar dado, misture setorial + histórico"). É hipótese em teste: se a combinação falhar, você descarta **o experimento**, não o FI. Por isso mora na borda — quebrar ali não quebra o sistema. |

> **O teste que decide a zona, sempre:** não é o *nome* da modalidade, é a **consequência da
> violação**. Descarta a resposta inteira → núcleo. Piora mas salva → cinturão. Só era um
> experimento → borda. **Se você mudar de domínio, é este teste que reclassifica as peças** —
> não a tabela acima. A tabela é o resultado do teste no caso-trilho, não uma lei universal.

---

## Como usar (regra operacional)

1. **Escreva primeiro o NÚCLEO.** Declarativa + Ética. Pergunta-teste de cada linha:
   *"se a IA violar isto, eu jogo a resposta fora?"* Se **sim** → é núcleo, e precisa de um
   **verificador externo** (senão é só priming — ver `como-classificar-priming-enforcement.md`).
2. **Depois o CINTURÃO.** Procedimental + Avaliativa. Aqui você pode afrouxar se a IA travar,
   sem comprometer o núcleo. A rubrica avaliativa, se for binária, sobe para enforcement.
3. **Por último a BORDA.** Composicional. É onde você testa combinações novas em runtime.
   Se falhar, o núcleo continua de pé — você só descarta o experimento, não o FI.

> **Por que isto casa com o eixo priming↔enforcement:** o núcleo é onde você MAIS precisa de
> catraca (enforcement externo); a borda é onde a placa (priming) basta. A coercividade não é
> a mesma em todo o FI — **ela cresce do centro para fora.** Núcleo = catraca. Borda = placa.
> Concretamente: uma linha do núcleo sem verificador externo é **catraca de papelão** (parece
> que barra, mas não barra — ver a matriz de 2 níveis em `como-classificar-priming-enforcement.md`).
> No núcleo, papelão é falha grave; na borda, papelão é aceitável (é só experimento).

---

## E se não encaixar limpo? (os casos-limite — leia, é aqui que o gabarito ganha músculo)

Nenhum mapeamento sobrevive intacto ao contato com um domínio real. Quatro situações em que a
peça **não cai limpa numa zona** — e o que fazer:

**1. Uma modalidade é núcleo E cinturão ao mesmo tempo.**
Acontece o tempo todo com a **Avaliativa**. Parte dela é binária ("cita fonte da lista: sim/não")
→ essa parte é núcleo/enforcement. Parte é gradual ("a análise está aprofundada?") → essa parte é
cinturão/priming. **Não force a modalidade inteira numa zona: quebre-a por linha.** A unidade de
classificação nunca é a modalidade — é a **cláusula**. Uma modalidade pode ter cláusulas em duas
zonas ao mesmo tempo, e isso é normal.

**2. Você acha que é núcleo mas não tem como verificar externamente.**
Ex.: "a IA NUNCA deve ser tendenciosa". É ética (parece núcleo), mas não existe `grep` para
"tendencioso". Sem verificador externo, isso é **priming disfarçado de núcleo** — uma catraca de
papelão no lugar mais perigoso do FI. Duas saídas honestas: (a) **operacionalizar** — trocar o
inverificável por um proxy checável ("não use os adjetivos X, Y, Z"; "cite os dois lados"); ou
(b) **rebaixar conscientemente** para cinturão e assumir que ali é priming, não catraca. O erro é
deixar no núcleo fingindo que barra.

**3. A regra do núcleo depende de julgamento do próprio modelo.**
Ex.: "só afirme o que estiver nas fontes" verificado por "o modelo confere se afirmou além das
fontes". **LLM julgando a si mesmo é priming fingindo enforcement** (a linha 4 da matriz em
`como-classificar-priming-enforcement.md`). Para ser núcleo de verdade, o verificador tem que ser
**outra coisa** (um parser que extrai citações e checa contra a lista; um segundo modelo com o
único papel de auditor). Autoavaliação nunca é catraca.

**4. Nada é núcleo no seu FI.**
Domínios criativos ("escreva 3 variações de headline") podem não ter nenhuma linha cuja violação
faça você descartar a resposta. **Isso é legítimo** — um FI pode ser quase todo cinturão + borda.
O gabarito não exige que você preencha o núcleo; exige que você **saiba se está vazio de propósito
ou por esquecimento**. Núcleo vazio num domínio de alto risco (crédito, saúde, jurídico) é o
esquecimento mais caro que existe.

> **Regra-mãe dos casos-limite:** quando travar, **não classifique a modalidade — classifique a
> linha**, e classifique-a pela *consequência da violação* + *quem verifica*. Toda dúvida de zona
> se resolve descendo da modalidade para a cláusula.

---

## Três exemplos contrastantes (domínios diferentes, mesmo gabarito)

O caso-trilho (risco de crédito) mostra o gabarito num domínio. Dois outros mostram que o **método
de classificar** é o que se transfere — não o conteúdo.

### Exemplo A — Analista de risco de crédito (o caso-trilho)

- **Núcleo/Declarativa:** "fontes válidas: rating interno + demonstrações auditadas. Nada além." → `assert`: a saída cita fonte da lista.
- **Núcleo/Ética:** "NUNCA recomende decisão de crédito final — só análise." → `gate`: reprova se contém verbo de recomendação.
- **Cinturão/Procedimental:** "1) rating 2) stress test 3) cobertura de juros."
- **Cinturão/Avaliativa:** "toda conclusão tem número + fonte." → rubrica binária (vira `assert`, sobe pro núcleo).
- **Borda/Composicional:** "se faltar dado, combine análise setorial + histórico." ← experimento.

### Exemplo B — Assistente de peça jurídica (contestação cível)

- **Núcleo/Declarativa:** "só cite jurisprudência que EU forneci no anexo. NUNCA invente número de processo, súmula ou tese." → `assert` **externo**: um parser extrai cada citação e confere contra a lista fornecida. (Alucinação de jurisprudência é o modo de falha nº1 aqui — e é fatal: petição com precedente inventado é sancionável.)
- **Núcleo/Ética:** "NUNCA afirme fato não constante dos autos como se fosse provado." → `gate`: reprova se um fato aparece sem âncora no documento-fonte.
- **Cinturão/Procedimental:** "1) preliminares 2) mérito 3) pedidos — nessa ordem processual."
- **Cinturão/Avaliativa:** "cada tese tem fundamento legal citado." → binária → sobe pro núcleo como `assert`.
- **Borda/Composicional:** "se a tese principal for fraca, combine com tese subsidiária + distinguishing do precedente contrário." ← experimento de estratégia.

> **O contraste que ensina:** aqui a **Declarativa carrega o peso** (a hierarquia de fontes é
> quase o FI inteiro), enquanto no crédito a Ética pesava tanto quanto. **A mesma modalidade tem
> peso diferente por domínio** — o gabarito diz a *zona*, o domínio diz o *tamanho*.

### Exemplo C — Triagem médica (assistente de anamnese, NÃO diagnóstico)

- **Núcleo/Ética:** "NUNCA dê diagnóstico definitivo nem prescreva. Só organize sintomas e sugira urgência de encaminhamento." → `gate` **externo**: reprova se a saída contém verbo prescritivo ou nome de diagnóstico afirmado como certeza. (Aqui a Ética é a modalidade dominante — a linha que, violada, é passivo médico-legal.)
- **Núcleo/Declarativa:** "baseie-se SÓ nos sintomas relatados. NUNCA presuma exame não feito." → `assert`: cada afirmação clínica rastreia a um sintoma relatado.
- **Cinturão/Procedimental:** "1) queixa principal 2) história 3) sinais de alarme 4) nível de urgência."
- **Cinturão/Avaliativa:** "todo sinal de alarme presente foi explicitamente citado." → binária → `assert`.
- **Borda/Composicional:** "se os sintomas forem ambíguos, combine dois protocolos de triagem e sinalize a divergência." ← experimento.

> **O contraste que ensina:** no médico, a **Ética domina e é quase toda binária** (verbos
> proibidos são `grep`-áveis) — ou seja, o núcleo aqui é fácil de virar catraca de verdade. No
> jurídico, o núcleo (não-alucinar citação) exige um parser mais esperto. **Domínios diferentes
> pedem verificadores de complexidade diferente para o MESMO tipo de núcleo.**

---

## Auto-teste (agora tente você)

Pegue o FI abaixo, de um domínio novo — **atendimento de suporte técnico de um SaaS**. Cinco linhas.
Para cada uma: **(a) qual modalidade? (b) qual zona? (c) tem verificador externo — ou é catraca de
papelão?**

```
[L1] "Você é o suporte N1 do produto X. NUNCA prometa reembolso — só o financeiro autoriza."
[L2] "Responda apenas com base na base de conhecimento anexada. Não invente funcionalidade."
[L3] "Fluxo: 1) confirme a versão do cliente 2) reproduza o passo 3) só então proponha solução."
[L4] "Toda resposta ao cliente deve conter o número do ticket."
[L5] "Se o caso for ambíguo, combine o script de billing com o de bug técnico e escale ao N2."
```

<details>
<summary><b>Gabarito do auto-teste (abra só depois de tentar)</b></summary>

- **L1** — **Ética · Núcleo.** Violação = passivo financeiro real → descarta. *Verificador:* `gate` externo — `grep` por "reembolso/refund" na saída reprova. **É catraca de verdade** (verbo é `grep`-ável).
- **L2** — **Declarativa · Núcleo.** Define o universo de fatos admissíveis; funcionalidade inventada contamina a raiz. *Verificador:* precisa de parser que confere afirmações de feature contra a KB. Se ficar só como frase no prompt, é **catraca de papelão** — escale anexando o checador.
- **L3** — **Procedimental · Cinturão.** É o caminho do raciocínio; pular um passo piora, não invalida. Ajustável se travar. *Priming* — nada externo reprova (e tudo bem, é cinturão).
- **L4** — **Avaliativa · sobe pro Núcleo.** Rubrica **binária** ("contém número do ticket: sim/não") → vira `assert`: `grep -qE '#[0-9]+' saida.md`. **É a linha que cruza a ponte** — priming disfarçado que você escala para enforcement anexando o `grep`.
- **L5** — **Composicional · Borda.** Combina dois scripts num caso novo; se falhar, descarta o experimento, não o FI. *Priming* — é onde você experimenta em runtime.

**Se você acertou L4 como "a linha que vira enforcement" e L2 como "núcleo que hoje é papelão",
pegou o gesto central:** a zona vem da *consequência da violação*; a catraca (vs papelão) vem de
*ter ou não verificador externo*. Errar L4 como "só cinturão" é o erro clássico — parece qualidade
gradual, mas é binária, então escala.
</details>

---

> **Honestidade epistêmica (postura Lakatos):** este gabarito é o **núcleo** de um programa
> didático, não uma verdade fechada. O mapeamento modalidade→zona é a hipótese central; os
> casos-limite acima são o **cinturão** que a protege sem torná-la dogma; e o seu domínio é a
> **borda** onde ela é testada. Se no seu caso uma peça não couber, não é o gabarito que falhou —
> é o convite para você aplicar o teste da consequência e reclassificar. Um gabarito bom não
> te dá o mapa pronto; te dá a bússola (`consequência da violação` + `quem verifica`) para
> desenhar o mapa do seu território.
