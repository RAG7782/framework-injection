# Protocolo de Lapidacao Iterativa

Refinamento espiral de qualquer output de IA por passes sucessivos de descoberta, consolidacao e polimento. Cada passe revela facetas que o anterior nao alcancou — como o lapidario que transforma pedra bruta em gema por cortes progressivos.

Premissa: Toda resposta de IA, mesmo as excelentes, contem facetas nao-reveladas. Lapidacao ≠ correcao. Lapidacao = aprofundamento estruturado.

Quando aplicar: por julgamento do praticante. Nem toda resposta precisa ser lapidada — respostas faticas simples, calculos diretos ou tarefas triviais nao se beneficiam. Lapidacao e para outputs onde ha profundidade a revelar. Em contextos de urgencia, usar `--passes 1`.

Parte do ecossistema Artesanato Digital.

## Argumento: $ARGUMENTS

O argumento e o conteudo a ser lapidado. Pode ser:
- Texto colado diretamente
- Referencia a uma resposta anterior na conversa
- Se vazio: lapidar a ULTIMA resposta gerada na conversa atual

Flags:
- `--auto` → Modo Automatico: roda os 3 passes sem parar (PADRAO se nenhuma flag)
- `--interativo` → Modo Interativo: executa operacao por operacao, mostra resultado, aguarda confirmacao
- `--progressivo` → Modo Progressivo: roda Pass 1 completo, mostra resultado, usuario decide se continua
- `--passes N` → Limita a N passes (1, 2 ou 3)
- `--full` → Ativa TODAS as operacoes condicionais (implementabilidade, falsificabilidade, precedentes historicos)

---

## ROTEAMENTO

Leia as flags no argumento e determine o modo:

| Flag | Modo | Comportamento |
|---|---|---|
| (nenhuma) ou `--auto` | Automatico | 3 passes completos, output final consolidado |
| `--interativo` | Interativo | Cada operacao isolada, pausa entre elas |
| `--progressivo` | Progressivo | Pass completo → pausa → decisao → proximo pass |

Declare o modo escolhido antes de iniciar: "Modo: [X]. Lapidando..."

### Deteccao de operacoes condicionais

Antes de iniciar, avalie automaticamente:
- **OP15 Implementabilidade:** Ativar se o output e orientado a acao (projeto, estrategia, plano, sistema). NAO ativar para outputs puramente analiticos ou criativos.
- **OP16 Falsificabilidade:** Ativar se o output e argumentativo, academico ou faz claims verificaveis. NAO ativar para outputs criativos ou operacionais puros.
- **OP17 Precedentes Historicos:** Ativar SOMENTE se ha acesso a web (WebSearch/WebFetch disponiveis). Caso contrario, declarar: "OP17 indisponivel — sem acesso a web."

A flag `--full` forca ativacao de todas as condicionais (exceto OP17 se nao ha acesso a web).

Declare quais condicionais foram ativadas antes de iniciar.

---

## AS 17 OPERACOES

Cada operacao deve ser executada com raciocinio profundo e estendido (chain-of-thought). Nao responder superficialmente em nenhuma operacao.

---

### CLUSTER A — MAPEAMENTO
> Objetivo: mapear o terreno — o que existe, falta, distorce e importa.

#### OP1 — ENRIQUECIMENTO
Pergunta-guia: "Que pequenos detalhes poderiam agregar valor substancial a esta estrutura?"
- Foco em micro-elementos de alto impacto
- Nao adicionar volume — adicionar precisao
- Cada detalhe sugerido deve explicar POR QUE agrega valor

#### OP2 — PONTOS CEGOS
Pergunta-guia: "Existem pontos cegos prejudiciais aos objetivos?"
- Se encontrar: clarificar explicitamente, com evidencia
- Se NAO encontrar: declarar "Nenhum ponto cego identificado" (NUNCA inventar)
- Pontos cegos = o que o autor nao sabe que nao sabe

#### OP3 — VIESES
Pergunta-guia: "Existem vieses prejudiciais aos objetivos?"
- Se encontrar: mitigar concretamente (nao apenas apontar — propor correcao)
- Se NAO encontrar: declarar honestamente
- Considerar vieses cognitivos, de confirmacao, de disponibilidade, de ancoragem, de sobrevivencia

#### OP4 — ALAVANCAGEM PARETO
Tres zooms telescopicos progressivos:
- **20/80** — Quais 20% dos elementos geram 80% do valor? Liste-os.
- **5/95** — Quais 5% sao absolutamente criticos? Reduza ao essencial.
- **1/99** — Qual e O UNICO elemento que, se perfeito, transforma tudo? Identifique-o.

Para cada zoom: justifique a selecao. O zoom progressivo forca compressao — nao e permitido repetir os mesmos elementos nos tres niveis.

#### → MICRO-CONSOLIDACAO A
Integre todas as descobertas do Cluster A ao output original. O produto desta consolidacao e o input do Cluster B. Preservar o original onde nao foi tocado. Marcar o que mudou.

---

### CLUSTER B — STRESS-TEST
> Objetivo: testar a resistencia, coerencia e robustez do output ja consolidado por A.

#### OP5 — CONTRADICOES INTERNAS
Pergunta-guia: "Ha pontos onde o output diz X num lugar e nao-X em outro? A estrutura e internamente coerente?"
- Verificar coerencia entre secoes, premissas e conclusoes
- Contradicoes ≠ tensoes (tensoes sao trade-offs legitimos; contradicoes sao erros)
- Se encontrar: apontar os trechos especificos que conflitam e propor resolucao
- Se NAO encontrar: declarar "Coerencia interna verificada"

#### OP6 — CONSEQUENCIAS TEMPORAIS
Pergunta-guia: "Se isso for implementado/aceito: o que acontece em 1 semana? Em 3 meses? Em 1 ano? Quais efeitos de 2a e 3a ordem emergem?"
- Analisar em tres horizontes: curto (dias/semanas), medio (meses), longo (anos)
- Identificar efeitos de 2a ordem (consequencias das consequencias)
- Identificar efeitos de 3a ordem (consequencias das consequencias das consequencias)
- Outputs estaticos: "O que muda se o contexto evoluir?"

#### OP7 — INVERSAO
Pergunta-guia: "E se a premissa central estivesse errada? E se fizessemos exatamente o oposto? O que aprendemos com a inversao?"
- Identificar a premissa central do output
- Inverter deliberadamente
- Analisar o que a inversao revela sobre dependencias ocultas
- Nao e para "destruir" — e para iluminar por contraste

#### OP8 — SIMPLIFICACAO ATIVA
Pergunta-guia: "O que pode ser REMOVIDO sem perda de valor? Qual elemento, se eliminado, na verdade melhora o todo?"
- Para cada elemento: "Se eu remover isso, o que se perde? Se nada se perde, remover."
- Diferente de Pareto (que identifica o essencial) — aqui se identifica o DISPENSAVEL
- Saint-Exupery: "Perfeicao nao e quando nao ha mais nada a adicionar, mas quando nao ha mais nada a remover"
- Limite: sugerir no maximo 5 remocoes, cada uma justificada

#### → MICRO-CONSOLIDACAO B
Integre os resultados do Cluster B ao output consolidado por A. Resolver contradicoes encontradas. Incorporar insights temporais. Aplicar simplificacoes aprovadas. O produto e o input do Cluster C.

---

### CLUSTER C — ANALISE ESTRUTURAL
> Objetivo: analisar a arquitetura profunda — dependencias, tensoes e limites.

#### OP9 — DEPENDENCIAS ESTRUTURAIS
Pergunta-guia: "Quais sao as dependencias ocultas? Se o pressuposto X mudar, o que desmorona em cadeia? Qual e a peca que, se removida, derruba a estrutura inteira?"
- Mapear pressupostos load-bearing (os que sustentam tudo)
- Para cada um: "Se isso mudar, o que quebra em cascata?"
- Identificar single points of failure
- Formato: Pressuposto → Dependentes → Risco se falhar

#### OP10 — SINTESE DE TENSOES
Pergunta-guia: "Quais sao as tensoes inerentes que nao podem ser eliminadas, apenas navegadas? Onde ha trade-offs legitimos, e como estao sendo arbitrados?"
- Tensoes ≠ contradicoes (contradicoes sao erros; tensoes sao dilemas reais)
- Para cada tensao: "Este trade-off esta explicito e consciente, ou implicito e acidental?"
- Exemplos comuns: velocidade vs. qualidade, abrangencia vs. profundidade, simplicidade vs. completude
- Tornar explicito o que era implicito

#### OP11 — CONDICOES DE CONTORNO
Pergunta-guia: "O que acontece nos extremos? E se escalar 100x? E se os recursos cairem a zero? E se a pessoa-chave sair? E se o contexto mudar radicalmente?"
- Testar o output nos limites: escala maxima, recursos minimos, mudanca de contexto
- Identificar onde a estrutura quebra (ponto de ruptura)
- Diferente de inversao (que inverte premissas) — aqui se ESTICA premissas ate o limite
- Formato: Variavel → Extremo testado → O que quebra → Implicacao

#### OP15 — IMPLEMENTABILIDADE (condicional)
> Ativa se: output orientado a acao (projeto, estrategia, plano, sistema) OU flag --full

Pergunta-guia: "Isso pode de fato ser executado? Qual e o gap entre o que esta descrito e o que a realidade permite? O que falta para isso sair do papel?"
- Avaliar: recursos necessarios vs. disponiveis
- Avaliar: competencias necessarias vs. existentes
- Avaliar: dependencias externas e riscos de execucao
- Formato: Aspecto → Gap identificado → O que falta → Sugestao

#### → MICRO-CONSOLIDACAO C
Integre a analise estrutural ao output consolidado por A+B. Explicitar dependencias criticas. Tornar tensoes visiveis. Registrar condicoes de contorno. O produto e o input do Cluster D.

---

### CLUSTER D — META-ANALISE
> Objetivo: ir alem do visivel — expandir, questionar, transferir, verificar.

#### OP12 — EXPANSAO
Pergunta-guia: "O que mais poderia ser melhorado, refinado, expandido que agregue valor inestimavel?"
- Priorizar sugestoes acionaveis sobre aspiracionais
- Cada sugestao deve ter: o que mudar + por que + como
- Limite: maximo 5 sugestoes por pass (densidade > volume)

#### OP13 — PERGUNTAS NAO-FEITAS
Pergunta-guia: "Que perguntas eu deveria ter feito e nao fiz, que elevariam isso a nivel SOTA+?"
- Meta-cognicao de segundo ordem: o gap do gap
- Incluir alertas de seguranca se aplicavel
- RESPONDER as proprias perguntas levantadas (nao apenas lista-las)
- Incluir: "Ha algo mais que deveria ser considerado?"

#### OP14 — ANALOGIA CROSS-DOMAIN
Pergunta-guia: "O que um especialista de um campo completamente diferente veria aqui que insiders do dominio nao veem? Que framework de outra area ilumina este problema?"
- Escolher 2-3 dominios distantes (nao adjacentes) ao dominio do output
- Para cada: "Um [biologo/arquiteto/musico/fisico/antropologo] olhando isso veria..."
- Foco em transferencias nao-obvias que gerem insight genuino
- NAO forcar analogias artificiais — se nenhuma analogia cross-domain agrega, declarar

#### OP16 — FALSIFICABILIDADE (condicional)
> Ativa se: output argumentativo, academico ou com claims verificaveis OU flag --full

Pergunta-guia: "Que evidencia, se encontrada, invalidaria esta conclusao/estrutura? O que me faria mudar de ideia?"
- Criterio de Popper: se nada pode falsificar, nao e conhecimento — e dogma
- Para cada claim central: "Que dado/evento/descoberta provaria que isso esta errado?"
- Nao e para enfraquecer — e para fortalecer pela consciencia dos limites

#### OP17 — PRECEDENTES HISTORICOS (condicional)
> Ativa SOMENTE se: ha acesso a web (WebSearch/WebFetch disponiveis) OU flag --full com web

Pergunta-guia: "Isso ja foi tentado antes? Por quem? O que aconteceu? Que licoes dos precedentes se aplicam aqui?"
- Usar WebSearch para investigar precedentes reais
- Para cada precedente encontrado: contexto, resultado, licao transferivel
- Se ha precedentes de sucesso: o que fizeram diferente?
- Se ha precedentes de fracasso: quais armadilhas evitar?
- NAO inventar precedentes — se a busca nao encontrar, declarar "Nenhum precedente identificado via web"
- Se nao ha acesso a web: pular e declarar "OP17 indisponivel — sem acesso a web nesta sessao"

#### → CONSOLIDACAO FINAL (encerramento do pass)
Instrucao: "Consolide TODAS as melhorias dos 4 clusters, preservando os elementos originais que nao foram objeto de aprimoramento."
- Output deve ser robusto, coeso, harmonico e completo
- Refinamento ≠ substituicao — o original permanece intacto onde nao foi tocado
- Marcar claramente o que mudou vs. o que foi preservado
- A consolidacao e o PRODUTO do pass, nao um resumo
- Esta consolidacao integra as 3 micro-consolidacoes anteriores + as descobertas do Cluster D

---

## ESTRUTURA DOS PASSES

### PASS 1 — DESCOBERTA (divergente)
Objetivo: Revelar tudo que esta oculto no output original.
Executar: Cluster A → Micro-Consolidacao A → Cluster B → Micro-Consolidacao B → Cluster C → Micro-Consolidacao C → Cluster D → Consolidacao Final
Produto: **Versao lapidada v1**

### PASS 2 — REFINAMENTO (convergente)
Objetivo: Aprofundar sobre o que o Pass 1 revelou.
Sobre a v1, executar:
- OP12 Expansao → OP13 Perguntas Nao-Feitas → OP14 Analogia Cross-Domain → Consolidacao
Produto: **Versao lapidada v2**

### PASS 3 — POLIMENTO (divergente→convergente)
Objetivo: Ultimo ciclo — encontrar o que dois passes ainda nao alcancaram.
Sobre a v2, executar:
- OP12 Expansao → OP13 Perguntas Nao-Feitas → OP14 Analogia Cross-Domain → Consolidacao Final
Produto: **Versao lapidada FINAL**

Se em qualquer pass nao houver mais refinamentos substantivos, declarar: "Lapidacao convergiu — output estavel no Pass [N]." e encerrar. NAO gerar passes vazios.

---

## PRINCIPIO DA MICRO-CONSOLIDACAO

Cada micro-consolidacao entre clusters serve como ALICERCE para o cluster seguinte. O Cluster B nao opera sobre o output original — opera sobre o output ja transformado pelo Cluster A. O Cluster C opera sobre A+B. O Cluster D opera sobre A+B+C.

Metafora: construcao de edificio. O terceiro andar so e possivel a partir da construcao do segundo, que so e possivel a partir do primeiro. Cada micro-consolidacao e um andar concluido — solido o suficiente para suportar o proximo.

Regras da micro-consolidacao:
1. Integrar descobertas ao output (nao apenas lista-las ao lado)
2. Resolver conflitos entre o original e as descobertas
3. Preservar o que nao foi tocado
4. O produto da micro-consolidacao e o INPUT do proximo cluster
5. Micro-consolidacao deve ser concisa — nao e relatorio, e versao atualizada do output

---

## PRINCIPIOS TRANSVERSAIS (aplicar em TODOS os passes e clusters)

1. **Anti-bloat:** Nao transformar o output em acumulo de telas e campos. Menos elementos com mais inteligencia. Favorecer clareza operacional, baixa friccao, reaproveitamento de informacao e capacidade de tomada de decisao.

2. **Densidade:** Se a resposta ficar longa, priorizar densidade, estrutura e utilidade pratica. Em cada secao, explicar o racional das decisoes e nao apenas a lista de itens.

3. **Processamento profundo:** Utilizar raciocinio estendido em cada operacao. Cada analise deve demonstrar profundidade real, nao checklist superficial.

4. **Julgamento artesanal:** O praticante decide quando aplicar o protocolo e quando parar. A ferramenta serve ao artesao, nao o contrario.

---

## FORMATO DE OUTPUT

### Modo Automatico (--auto)

```
## Lapidacao — Pass 1 (Descoberta)

### Cluster A: Mapeamento

#### OP1: Enriquecimento
[resultado com justificativas]

#### OP2: Pontos Cegos
[resultado ou "Nenhum identificado"]

#### OP3: Vieses
[resultado ou "Nenhum identificado"]

#### OP4: Alavancagem Pareto
- **20/80:** [elementos + justificativa]
- **5/95:** [elementos + justificativa]
- **1/99:** [o elemento + justificativa]

### → Micro-Consolidacao A
[versao atualizada do output integrando descobertas do Cluster A]

---

### Cluster B: Stress-Test

#### OP5: Contradicoes Internas
[resultado]

#### OP6: Consequencias Temporais
[curto / medio / longo + efeitos 2a e 3a ordem]

#### OP7: Inversao
[premissa invertida + o que revela]

#### OP8: Simplificacao Ativa
[ate 5 remocoes sugeridas com justificativa]

### → Micro-Consolidacao B
[versao atualizada integrando stress-test]

---

### Cluster C: Analise Estrutural

#### OP9: Dependencias Estruturais
[mapa: pressuposto → dependentes → risco]

#### OP10: Sintese de Tensoes
[tensoes explicitas + como estao sendo navegadas]

#### OP11: Condicoes de Contorno
[variavel → extremo → ponto de ruptura]

#### OP15: Implementabilidade (se ativa)
[gap plano vs. realidade]

### → Micro-Consolidacao C
[versao atualizada integrando analise estrutural]

---

### Cluster D: Meta-Analise

#### OP12: Expansao
[ate 5 sugestoes acionaveis]

#### OP13: Perguntas Nao-Feitas
[perguntas + respostas]

#### OP14: Analogia Cross-Domain
[2-3 dominios distantes + transferencias]

#### OP16: Falsificabilidade (se ativa)
[criterios de falsificacao por claim]

#### OP17: Precedentes Historicos (se ativa + web)
[precedentes encontrados + licoes]

### → Consolidacao Final v1
[versao consolidada completa — produto do Pass 1]

---

## Lapidacao — Pass 2 (Refinamento)

### OP12: Expansao (sobre v1)
[...]

### OP13: Perguntas Nao-Feitas (sobre v1)
[...]

### OP14: Analogia Cross-Domain (sobre v1)
[...]

### Consolidacao v2
[versao consolidada]

---

## Lapidacao — Pass 3 (Polimento)

### OP12: Expansao (sobre v2)
[...]

### OP13: Perguntas Nao-Feitas (sobre v2)
[...]

### OP14: Analogia Cross-Domain (sobre v2)
[...]

### Versao Final Lapidada
[versao definitiva — o produto final]

---

## Sintese da Lapidacao
- **Operacoes executadas:** [N de 17 — listar quais condicionais ativaram]
- **Facetas reveladas:** [quantas melhorias substantivas em N passes]
- **Ponto de maior impacto:** [o 1/99 que emergiu]
- **Tensoes identificadas:** [lista resumida]
- **Dependencias criticas:** [lista resumida]
- **Convergencia:** [convergiu no pass N / ainda divergente]
```

### Modo Interativo (--interativo)
Executar UMA operacao por vez. Apos cada uma, mostrar o resultado e perguntar:
"→ Prosseguir para [proxima operacao]? (s / n / ajustar)"

Micro-consolidacoes sao executadas automaticamente ao final de cada cluster.
Se o usuario disser "ajustar", perguntar o que mudar antes de prosseguir.
Se "n" em qualquer ponto: executar consolidacao com tudo ate aqui e encerrar.

### Modo Progressivo (--progressivo)
Executar Pass completo (todos os clusters com micro-consolidacoes). Ao final, mostrar a consolidacao e perguntar:
"→ Pass [N] concluido. Continuar para Pass [N+1]? (continuar / parar / ajustar)"

Se "parar": a consolidacao do ultimo pass executado e o produto final.

---

## REGRAS INEGOCIAVEIS

1. **Nao inventar problemas.** Se nao ha ponto cego, contradicao, vies ou tensao real, diga. Fabricar fragilidades para parecer rigoroso e o oposto de rigor.
2. **Preservar o original.** Consolidacao integra — nunca substitui silenciosamente o que o usuario construiu.
3. **Densidade > Volume.** Uma melhoria cirurgica vale mais que dez sugestoes vagas.
4. **Cada sugestao deve ser acionavel.** "Poderia ser melhor" sem dizer como nao e lapidacao, e ruido.
5. **Honestidade sobre convergencia.** Se nao ha mais o que refinar, declare e encerre. Passes vazios sao proibidos.
6. **Processamento real, nao checklist.** Cada operacao exige raciocinio profundo. Respostas rasas em qualquer OP invalidam o protocolo.
7. **Micro-consolidacao e alicerce, nao resumo.** Cada micro-consolidacao produz versao atualizada do output, nao lista de achados.
8. **Condicionais sao honestas.** Se OP15/OP16/OP17 nao se aplicam, nao forcar. Declarar "nao aplicavel" e seguir.

---

## CONEXAO COM O ECOSSISTEMA

| Componente | Relacao com Lapidacao |
|---|---|
| **Artesanato Digital** | Filosofia mae — lapidacao e oficio artesanal |
| **Tempera Adversarial** | Irmao complementar: Tempera testa resistencia, Lapidacao aprofunda e revela |
| **AGORA Intelligence** | Pode lapidar relatorios AGORA; OP14 (Analogia) usa rotacao cross-domain |
| **Framework Injection** | Pode lapidar FIs em construcao |
| **Protocolo LER** | Pode lapidar analises de leitura densa |
| **Densidade Semiotica** | Motor analitico — OP4 (Pareto) e rarefacao, OP13 e subtracao, OP8 e rarefacao ativa |
| **STEER** | Infraestrutura quantitativa — operacoes SDE mapeiam para embedding space |
| **IMI** | Memoria — preserva resultados de lapidacao entre sessoes |
