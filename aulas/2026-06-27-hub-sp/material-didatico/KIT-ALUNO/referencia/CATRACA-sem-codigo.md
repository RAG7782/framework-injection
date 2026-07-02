# A catraca sem código — enforcement para quem não é programador

> **O que esta página resolve** (apontamento do peer-review 2026-06-27): o `grep -q` é uma
> catraca perfeita para ensinar — mas o profissional não-dev (advogado, médico, analista) vê
> o código de terminal e **fecha o PDF**: "segurança é privilégio de programador". Falso.
> O `grep` é **um** ponto num espectro de catracas. Aqui estão as que não pedem terminal.
>
> **Lastro:** critério-mestre do `como-classificar-priming-enforcement.md` (enforcement = existe
> mecanismo FORA do modelo que reprova a saída). O `grep` é só a encarnação mais didática desse
> critério. `[AF]` a lista de catracas sem-código é derivada do mesmo critério — mesma regra,
> outras ferramentas.

---

## A regra continua a mesma

O que faz uma catraca **não é ser código** — é ser um **mecanismo externo ao modelo que reprova
a saída se a condição falhar**. O `grep -q` só é famoso porque é o exemplo mais nu. Troque o
`grep` por qualquer coisa que devolva **passa / não-passa** sem pedir a opinião do modelo, e você
tem enforcement. A coercividade é um **espectro**, não um botão liga-desliga.

```
PLACA ─────────────────────────────────────────────────────► CATRACA
(priming)                                              (enforcement)
 prosa      "deve      JSON      duplo-      structured    grep -q
 solta      conter X"  schema    agente      output API    / teste
            ▲          no CRM    true/false                exit code
            │
       PRIMING DISFARÇADO (parece regra, mas nada externo reprova)
```

---

## 4 catracas que não pedem terminal

### 1. Structured Output / JSON Schema (a catraca é o *parser*)
Você exige que a IA devolva **exatamente** no formato de um schema (campos obrigatórios, tipos).
Se ela "devanear" e não preencher o formulário exato, **o software recusa automaticamente** —
não a IA. O parser é o muro de concreto.
> *Advogado:* "analise o contrato e devolva `{parte, objeto, valor, riscos[], clausula_leonina: bool}`."
> Faltou `riscos`? O sistema rejeita. A IA não se auto-aprovou — o schema reprovou.
> Ferramentas: OpenAI/Anthropic *structured output*, Pydantic, JSON Schema no próprio CRM/ERP.

### 2. Duplo-agente (a catraca é um *segundo agente que só diz sim/não*)
- **Agente A** = criativo (gera a resposta).
- **Agente B** = a catraca. Roda um checklist binário sobre a resposta de A.
- **Regra de ouro:** o Agente B **não tem permissão de gerar texto novo** — ele só emite
  `verdadeiro` ou `falso`. Ele não cria; ele **bloqueia**.
> Por que funciona: B é externo à função geradora de A. Não é "réu e juiz na mesma cabeça" —
> são duas cabeças, e a segunda não tem interesse em agradar a primeira.
> *Cuidado:* B ainda é um LLM (estocástico). É uma catraca **mais forte que prosa**, mas mais
> fraca que um parser determinístico. Ver "o que a catraca NÃO garante", abaixo.

### 3. Formulário/campo obrigatório no sistema que você já usa
Seu CRM, planilha ou ERP já reprova campo vazio. Faça a saída da IA **passar por ele**. Se o
campo "fundamentação" está vazio, o sistema não deixa salvar. Enforcement de negócio, zero código.

### 4. Regra de negócio como gate (lógica, não sintaxe)
"Valor da causa > R$ 100 mil → exige parecer sênior antes de sair." Isso é uma catraca de
**lógica de negócio**: um `if` que você já tem no fluxo, aplicado à saída da IA.

---

## O que a catraca NÃO garante (a honestidade que blinda contra o crítico)

> **Catraca prova VERIFICABILIDADE, não VERACIDADE.**
> Um `grep -q "rating"` passa num rating **alucinado** — desde que a palavra "rating" apareça.
> O schema aceita um JSON **bem-formado com conteúdo errado**. A catraca garante que uma
> **propriedade checável** foi cumprida; ela **não** garante que a resposta é verdadeira.
>
> Por isso: escolha bem O QUE a catraca checa (uma propriedade que, se falha, você quer barrar),
> e saiba que propriedades semânticas profundas (é *correto*? é *bom*?) continuam exigindo
> julgamento humano. A catraca **localiza e barra o erro checável** — ela não pensa por você.

---

## Regra de bolso

> Não pergunte "sei programar?". Pergunte **"o que, na minha saída, se estiver errado, eu quero
> que seja BARRADO antes de chegar em mim?"** — e ache o mecanismo externo mais simples que
> barra isso. Às vezes é um `grep`. Muitas vezes é um campo obrigatório que você já tem.
