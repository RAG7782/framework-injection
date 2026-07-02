# A catraca sem código — enforcement para quem não é programador

> **O que esta página resolve** (apontamento do peer-review 2026-06-27): o `grep -q` é uma
> catraca perfeita para ensinar — mas o profissional não-dev (advogado, médico, analista) vê
> o código de terminal e **fecha o PDF**: "segurança é privilégio de programador". Falso.
> O `grep` é **um** ponto num espectro de catracas. Aqui estão as que não pedem terminal —
> com exemplo por profissão, um critério para **escolher** qual usar, e o limite honesto de
> cada uma (uma catraca que passou algo errado, para você sentir a fronteira antes do crítico).
>
> **Lastro:** critério-mestre do `como-classificar-priming-enforcement.md` (enforcement = existe
> mecanismo FORA do modelo que reprova a saída). O `grep` é só a encarnação mais didática desse
> critério. `[AF]` a lista de catracas sem-código, a matriz de escolha e o critério "quando confiar
> no duplo-agente" são derivados do mesmo critério-mestre — mesma regra, outras ferramentas — e
> marcados como tal.

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

**Por que cada ponto está onde está** (leia o espectro da esquerda para a direita — cada passo
move a verificação *para mais longe da cabeça do modelo*):

- **prosa solta** — "seja cuidadoso", "faça um bom parecer". Nada checável. Placa pura.
- **"deve conter X"** — já tem uma condição (a palavra X aparece?), mas quem julga ainda é o
  próprio modelo lendo a si mesmo. É a **catraca de papelão**: forma de regra, zero braço.
- **JSON schema no CRM** — aqui a verificação *sai* do modelo: um **parser** (software burro,
  determinístico) recusa o que não bate. Primeiro ponto que trava de verdade.
- **duplo-agente true/false** — a verificação está fora do gerador, mas ainda é **um LLM** que
  decide. Trava mais que papelão, menos que aço — porque o juiz é estocástico (varia).
- **structured output API** — o próprio provedor (OpenAI/Anthropic) **força** o formato na saída;
  o modelo não consegue fugir do schema. Determinístico de novo.
- **grep -q / teste / exit code** — o extremo: um comando roda, devolve 0 ou 1, e **reprova sem dó**.
  Nenhuma opinião, nenhum "quase". Catraca de aço.

> **A régua escondida no espectro:** quanto mais à direita, mais a decisão de aprovar/reprovar
> é tirada do modelo e entregue a algo que **não tem interesse em agradar**. O papelão está à
> esquerda porque o juiz é o próprio réu. O aço está à direita porque o juiz é um cano de ferro.

---

## 4 catracas que não pedem terminal

### 1. Structured Output / JSON Schema (a catraca é o *parser*)
Você exige que a IA devolva **exatamente** no formato de um schema (campos obrigatórios, tipos).
Se ela "devanear" e não preencher o formulário exato, **o software recusa automaticamente** —
não a IA. O parser é o muro de concreto.

- **Advogado:** "analise o contrato e devolva `{parte, objeto, valor, riscos[], clausula_leonina: bool}`."
  Faltou `riscos`? O sistema rejeita. A IA não se auto-aprovou — o schema reprovou.
- **Médico:** triagem devolve `{queixa, tempo_sintoma_h: number, red_flags[], conduta}`.
  A IA escreveu "há algumas horas" no campo `tempo_sintoma_h`? O parser exige **número** e barra —
  o campo vira input verificável de protocolo, não prosa vaga.
- **Analista financeiro:** parecer devolve `{ativo, rating, premissas[], preco_alvo: number, cenario_stress: bool}`.
  Veio `rating` mas `cenario_stress` ficou `null`? Não salva. A ausência do stress-test é barrada
  na porta, não descoberta na reunião.
- **Consultor:** diagnóstico devolve `{cliente, hipoteses[], evidencia_por_hipotese[], recomendacao, risco_execucao}`.
  Uma hipótese sem `evidencia`? Schema recusa — mata o slide bonito sem lastro.

> Ferramentas: OpenAI/Anthropic *structured output*, Pydantic, JSON Schema no próprio CRM/ERP.

### 2. Duplo-agente (a catraca é um *segundo agente que só diz sim/não*)
- **Agente A** = criativo (gera a resposta).
- **Agente B** = a catraca. Roda um checklist binário sobre a resposta de A.
- **Regra de ouro:** o Agente B **não tem permissão de gerar texto novo** — ele só emite
  `verdadeiro` ou `falso`. Ele não cria; ele **bloqueia**.

Por que funciona: B é externo à função geradora de A. Não é "réu e juiz na mesma cabeça" —
são duas cabeças, e a segunda não tem interesse em agradar a primeira.

- **Advogado:** A minuta a petição; B recebe só a pergunta binária *"toda tese citada tem
  fundamento legal explícito na peça? (S/N)"*. B acha uma tese sem artigo → reprova, devolve para A.
- **Médico:** A escreve a prescrição; B checa *"há interação medicamentosa entre os itens
  prescritos, conforme a lista fornecida? (S/N)"*. B não prescreve — só levanta a bandeira.
- **Analista financeiro:** A gera a recomendação; B checa *"a recomendação declara horizonte
  temporal E cenário de baixa? (S/N)"*. Faltou o downside → bloqueia.
- **Consultor:** A monta o roadmap; B checa *"cada iniciativa tem dono E prazo E métrica de
  sucesso? (S/N)"*. Iniciativa órfã → volta.

> *Cuidado:* B ainda é um LLM (estocástico). É uma catraca **mais forte que prosa**, mas mais
> fraca que um parser determinístico. Quando confiar nele, e quando não — ver a seção
> **"E o duplo-agente é confiável?"**, abaixo.

### 3. Formulário/campo obrigatório no sistema que você já usa
Seu CRM, planilha ou ERP já reprova campo vazio. Faça a saída da IA **passar por ele**. Se o
campo "fundamentação" está vazio, o sistema não deixa salvar. Enforcement de negócio, zero código.

- **Advogado:** o campo "fundamento legal" do sistema de peças é obrigatório → a saída da IA
  não é salva sem ele. O software do escritório vira a catraca.
- **Médico:** o prontuário eletrônico **não fecha o atendimento** sem CID preenchido → a nota
  gerada pela IA que "esqueceu" o CID trava na tela, não vaza para o registro.
- **Analista:** a planilha de comitê tem célula obrigatória "preço-alvo" com validação de tipo
  numérico → texto qualitativo não entra ali.
- **Consultor:** o template de proposta no CRM exige o campo "critério de aceite" preenchido →
  proposta sem critério não avança de estágio.

### 4. Regra de negócio como gate (lógica, não sintaxe)
"Valor da causa > R$ 100 mil → exige parecer sênior antes de sair." Isso é uma catraca de
**lógica de negócio**: um `if` que você já tem no fluxo, aplicado à saída da IA.

- **Advogado:** valor da causa > R$ 100 mil → trava até visto do sócio.
- **Médico:** paciente > 65 anos **e** dor torácica → protocolo obriga ECG antes de liberar alta;
  a conduta da IA que pula o ECG é barrada pela regra, não pela IA.
- **Analista:** exposição > 5% da carteira → exige aprovação do comitê de risco antes de executar.
- **Consultor:** contrato > R$ 500 mil ou prazo > 12 meses → exige revisão jurídica antes do envio.

---

## Qual catraca para qual situação? (a matriz de escolha) `[AF]`

Você não escolhe a catraca pelo que sabe programar — escolhe pela **natureza do que precisa barrar**.
Três perguntas resolvem quase sempre:

1. **O erro é de FORMA ou de CONTEÚDO?** (faltou um campo × o campo está errado)
2. **A checagem é MECÂNICA ou precisa de JULGAMENTO?** (existe/não-existe × "faz sentido?")
3. **Você TEM um sistema no fluxo** que já reprova campo vazio, ou está no vácuo?

| Sua situação | Catraca certa | Por quê |
|---|---|---|
| Preciso garantir que **todos os campos existem** e têm o tipo certo | **1. Schema/Parser** | verificação mecânica pura, determinística, à prova de devaneio |
| Já uso CRM/ERP/prontuário que **trava campo vazio** | **3. Campo obrigatório** | reaproveita muro que já existe — esforço zero, confiabilidade de software |
| A regra é **condicional de negócio** ("se X > limite, exige Y") | **4. Regra de negócio (gate)** | é um `if` do seu processo, não sintaxe — determinístico e auditável |
| Preciso checar algo que **exige leitura/interpretação** ("toda tese tem fundamento?") e não há teste mecânico | **2. Duplo-agente** | única opção quando o critério é semântico; aceite que é aço-fraco |
| A propriedade é **binária e literal** ("contém a palavra RATING") | **grep / teste** (o de terminal) | se você topar uma linha de comando, é a catraca mais barata e mais dura |

**Regra de desempate — sempre prefira a catraca mais à DIREITA do espectro que resolve o seu caso.**
Um schema (determinístico) ganha de um duplo-agente (estocástico) *sempre que o critério couber
num formato*. Só desça para o duplo-agente quando o que você precisa checar **não cabe** num
parser — quando exige de fato ler e entender. Não use duplo-agente para checar "o campo existe":
isso é canhão para matar mosca, e o canhão erra às vezes.

> **Combine catracas em camadas.** O mais forte na prática é empilhar: schema barra a forma
> (barato, determinístico) → duplo-agente barra o sentido (caro, estocástico) → campo obrigatório
> do CRM barra a entrega final. Cada camada pega o que a anterior deixou passar.

---

## E o duplo-agente é confiável? (quando confiar no juiz estocástico) `[AF]`

O Agente B é um LLM. Ele **varia**: rode a mesma checagem duas vezes e pode dar S numa e N noutra.
Isso não o inutiliza — mas define **onde ele serve e onde ele engana**.

**Confie no duplo-agente quando:**
- A checagem é **binária e bem-delimitada** ("existe a seção de riscos? S/N") — quanto mais a
  pergunta se aproxima de um "achei/não-achei", mais o LLM acerta.
- O custo de um **falso-positivo é baixo** (se ele deixar passar um errado de vez em quando, o
  dano é recuperável, não catastrófico).
- Você **fecha a pergunta**: B recebe *uma* pergunta S/N, não "avalie a qualidade". Pergunta
  aberta devolve prosa, e prosa não trava nada — vira papelão de novo.

**NÃO confie — exija catraca determinística (schema/regra/teste) quando:**
- O erro é **caro ou irreversível** (perda financeira material, dano ao paciente, nulidade
  processual). Estocástico não guarda cofre.
- A propriedade **cabe num teste mecânico** ("o campo `preco_alvo` é número?"). Se um parser
  resolve, usar LLM é trocar aço por lata por preguiça.
- Você precisa de **auditoria estável** ("provar que 100% das saídas passaram na checagem X").
  Um juiz que varia não dá garantia auditável.

> **O veto de eficácia-limitada** (mesmo princípio da `fi-enforce`): não peça ao duplo-agente
> algo que depende de juízo futuro aberto — *"avalie se a estratégia é razoável"*. Isso é
> cognitivo por natureza; forçar um S/N ali é **assert-teatro**: parece catraca, mas o "sim"
> não significa nada. Mantenha o duplo-agente nas perguntas **fechadas e verificáveis**, e deixe
> o julgamento aberto explicitamente para o humano.

**Regra de bolso do duplo-agente:** ele é um **detector de ausência**, não um selo de qualidade.
Ótimo para "faltou X?". Péssimo para "isto está bom?".

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

### Um exemplo de falha real (para você sentir a fronteira)

Um analista pediu à IA um parecer de crédito e colocou uma catraca de schema: o campo `rating`
era **obrigatório** e o campo `fontes[]` exigia **pelo menos 2 itens**. A saída passou: veio
`rating: "BBB"` e duas fontes na lista. Catraca verde, parecer salvo, enviado ao comitê.

O problema: **uma das duas "fontes" era um relatório que não existe** — a IA inventou o nome e
a data, e o schema, é claro, só contou *que havia dois itens na lista*, não *se os itens eram
reais*. A propriedade checada era "≥ 2 fontes", e ela foi cumprida ao pé da letra. O rating
`BBB`, por sua vez, era plausível na forma e furado no mérito — construído sobre a fonte fantasma.

**A catraca não falhou — ela fez exatamente o que prometeu.** Ela garantiu *verificabilidade*
("o formato tem duas fontes") e nunca prometeu *veracidade* ("as fontes existem e sustentam o
rating"). O erro foi humano: confundir "passou na catraca" com "está certo". A lição:

- A catraca **estreita** o que pode dar errado — ela não **elimina** o erro.
- Toda catraca tem uma **fronteira semântica**: até onde a propriedade é literal, ela trava;
  além disso (o item é *real*? o número é *verdadeiro*?), só o humano trava.
- Por isso a melhor catraca é a que checa a propriedade **mais próxima do dano que você teme**.
  Se o dano é "fonte inventada", a catraca certa não é "≥ 2 fontes" — é uma que **valida cada
  fonte contra uma base real** (regra de negócio / lookup externo). Escolher a propriedade certa
  é metade do trabalho.

---

## Auto-teste — você entendeu a catraca? (5 min)

Pegue uma saída de IA que você usa no seu trabalho e responda por escrito:

1. **Qual é o UM erro** que, se passar despercebido, mais te machuca? (dinheiro, prazo, nulidade,
   dano ao cliente/paciente) — descreva em uma frase.
2. Esse erro é de **FORMA** (faltou um campo, formato errado) ou de **CONTEÚDO** (o dado está
   errado)? Rode as 3 perguntas da matriz e **escolha a catraca**.
3. A propriedade que sua catraca checa é **literal e mecânica** ("existe o campo") ou depende de
   **julgamento** ("faz sentido")? Se depende de julgamento, você caiu no duplo-agente — sua
   pergunta para o Agente B **cabe num S/N fechado**? Reescreva-a até caber.
4. Aplique o **teste da falha real**: imagine a saída mais errada possível que **ainda assim
   passaria** na sua catraca. Ela existe? (Sempre existe.) Qual é? Isso te mostra a fronteira
   semântica — o pedaço que a catraca **não** cobre e que fica com você.
5. Sua catraca está **à direita possível** no espectro? Se você escolheu duplo-agente para algo
   que um schema resolveria, desça para o schema. Se escolheu prosa ("pedi pra ela caprichar"),
   você não tem catraca nenhuma — tem papelão. Anexe um mecanismo externo.

**Gabarito de raciocínio (não de resposta):** se em qualquer passo você respondeu "a própria IA
verifica" — pare. Isso é priming disfarçado, o réu julgando a si mesmo. Uma catraca de verdade
é sempre algo **fora do modelo** que devolve passa/não-passa sem pedir a opinião de quem gerou.

---

## Regra de bolso

> Não pergunte "sei programar?". Pergunte **"o que, na minha saída, se estiver errado, eu quero
> que seja BARRADO antes de chegar em mim?"** — ache o mecanismo externo mais simples que
> barra isso, escolha o ponto **mais à direita do espectro** que resolve o caso, e não confunda
> "passou na catraca" com "está certo". Às vezes é um `grep`. Muitas vezes é um campo obrigatório
> que você já tem. Sempre é algo que **não é a própria IA se aprovando**.
