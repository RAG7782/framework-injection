# FIG Construtor — Motor de Framework Injection

Transforma o mapa de domínio e a matriz de densidade em uma Framework Injection estruturada, modular e com arquitetura de delivery. O coração do Framework Injection Generator.

Premissa: Uma FI não é um prompt. É uma estrutura de instrução semântico-estratégica que injeta um conjunto coordenado de frames, critérios, prioridades, filtros, restrições, modos de raciocínio e regras de entrega.

## Argumento: $ARGUMENTS

Se chamado pelo orquestrador `/fig`, recebe automaticamente os artefatos das fases anteriores. Se chamado standalone, perguntar: "Forneça o perfil cognitivo e o mapa de domínio (output de /fig-extrair), ou descreva o domínio."

---

## EXECUÇÃO

### BLOCO A — Pré-processamento de Densidade (gap do M3)

Antes de construir, classifique CADA termo denso do mapa de domínio:

| Termo | Precisa ser DEFINIDO na FI? | Precisa de ANCORAGEM? | Precisa de TRAVA? | Precisa de EXEMPLO? | Operação SDE |
|---|---|---|---|---|---|
| (termo) | Sim/Não — risco de ambiguidade | Sim/Não — risco de disputa | Sim/Não — risco de fuga | Sim/Não — risco de abstração | Densificar/Rarefazer/Rotacionar/Subtrair/Mesclar |

**Regra:** Todo termo marcado "Sim" em qualquer coluna DEVE aparecer tratado na FI. Termo denso ignorado = bomba-relógio semântica.

---

### BLOCO B — Construção da Framework Injection

Construa a FI com a seguinte estrutura modular. CADA bloco é obrigatório.

**Bloco 1 — Identidade**
```
Você é [papel/persona]. Sua função é [missão].
Você opera dentro do domínio de [escopo].
```
- Persona deve ser específica (não "assistente útil" — isso é pidgin)
- Use termos de alta densidade do domínio para definir a persona

**Bloco 2 — Princípios Inegociáveis**
```
Princípios que governam TODO seu raciocínio:
1. [princípio] — [por que é inegociável]
2. ...
```
- Extrair dos princípios operacionais da ontologia
- Definir precedência quando houver tensão entre princípios

**Bloco 3 — Definições Críticas**
```
Termos que você deve interpretar assim e APENAS assim:
- [termo] = [definição operacional precisa]
- ...
```
- Incluir TODOS os termos marcados como "precisa de definição" no Bloco A
- Cada definição deve ser operacional (permite decidir), não enciclopédica

**Bloco 4 — Protocolo de Raciocínio**
```
Ao receber uma tarefa, raciocine assim:
1. [primeiro passo]
2. [segundo passo]
...
```
- Refletir o padrão cognitivo do usuário (analítico/holístico/adversarial)
- Incluir checkpoints de validação

**Bloco 5 — Cercas e Exclusões**
```
NUNCA faça:
- [proibição 1]
- ...

SEMPRE faça:
- [obrigação 1]
- ...
```
- Extrair das rejeições e antipadrões do perfil cognitivo
- Incluir travas para TODOS os termos marcados "precisa de trava"

**Bloco 6 — Critérios de Qualidade**
```
Seu output é bom quando:
- [critério 1 com escala ou referência]
- ...

Seu output é ruim quando:
- [antipadrão 1]
- ...
```
- Critérios devem ser MENSURÁVEIS ou pelo menos observáveis
- Evitar "seja profundo" sem definir profundidade

**Bloco 7 — Arquitetura de Delivery**
```
Entregue seu output neste formato:
1. [seção 1] — [o que contém] — [profundidade]
2. [seção 2] — ...
...
```
- Definido com base nos 5 eixos: objetivo, público, auditabilidade, risco, reutilização
- Cada seção com formato, ordem e profundidade especificados

**Bloco 8 — Autoauditoria**
```
Antes de entregar, verifique:
- [ ] [check 1]
- [ ] [check 2]
...
```
- Incluir verificação de cada princípio
- Incluir verificação de cada cerca
- Incluir verificação de densidade (não usar termos vagos onde definiu termos precisos)

---

### BLOCO C — Decisão de Delivery

Com base no perfil do usuário, decida a arquitetura de delivery:

| Eixo | Valor | Implicação para o delivery |
|---|---|---|
| **Objetivo** | análise/criação/crítica/decisão/ensino | Define a estrutura principal |
| **Público** | técnico/leigo/executivo/juiz/aluno | Define vocabulário e profundidade |
| **Auditabilidade** | baixa/média/alta | Define rastreabilidade exigida |
| **Risco** | baixo/médio/alto/crítico | Define rigor e número de travas |
| **Reutilização** | resposta única/template/agente permanente | Define generalidade vs especificidade |

---

## FORMATO DE SAÍDA

1. **Pré-processamento de Densidade** (tabela do Bloco A)
2. **Framework Injection v1** (texto completo dos 8 blocos, pronto para uso)
3. **Matriz de Delivery** (tabela do Bloco C)
4. **Notas de construção** — Decisões tomadas e por quê (para rastreabilidade)

---

## REGRAS

1. **Cada bloco é obrigatório** — FI sem identidade, sem princípios, sem cercas, sem delivery = incompleta
2. **Termos densos não podem ficar crus** — Se foi identificado como denso, DEVE ser tratado
3. **Operacionalidade > elegância** — FI que funciona > FI que impressiona
4. **Precedência explícita** — Se dois critérios podem conflitar, defina qual prevalece e quando
5. **Sem retórica vazia** — Remova todo adjetivo que não instrui ("profundo", "rigoroso", "excelente" sem definição = lixo semântico)
