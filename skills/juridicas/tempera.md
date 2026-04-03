# Protocolo de Têmpera Adversarial (ATP)

Transformação estrutural de artefatos por ciclo controlado de ataque, reparo e endurecimento. Baseado na metalurgia: aço bruto é frágil — aço temperado é resiliente.

Premissa: Output não temperado é rascunho. Só output temperado é entregável. A diferença entre validação e têmpera é que validação verifica — têmpera transforma.

## Argumento: $ARGUMENTS

Se vazio, perguntar ao usuário: "Cole o texto, argumento, peça ou artefato que deseja temperar."

---

## EXECUÇÃO

### FASE 1 — FORJAR (Gerar o artefato)

Se o artefato já foi fornecido pelo usuário, pule para a Fase 2.

Se precisa ser gerado:
- Gere o artefato usando o melhor framework disponível para o domínio
- O artefato inicial reflete expertise mas ainda não foi estressado
- Documente premissas, fontes e raciocínio

**Entrega:** Artefato v0 (rascunho estruturado)

---

### FASE 2 — MARTELAR (Atacar adversarialmente)

Assuma a persona do **Auditor Constitucional** — um agente dedicado à destruição sistemática.

O martelamento é deliberadamente agressivo. Seu propósito é encontrar TODA fraqueza, não dar feedback construtivo.

Para CADA afirmação substantiva do artefato, tente:

1. **Alucinações** — A afirmação é verificável? A fonte existe? O dado é real?
2. **Erros lógicos** — O raciocínio é válido? Há non sequitur, petição de princípio, falsa dicotomia?
3. **Evidências ausentes** — O que é afirmado sem prova? O que precisaria de fonte e não tem?
4. **Premissas não declaradas** — Quais pressupostos o artefato assume sem explicitar?
5. **Vieses** — Há viés de confirmação, seleção ou enquadramento?
6. **Contra-argumentos** — Qual a melhor versão do argumento contrário? O artefato sobrevive?
7. **Vulnerabilidades de domínio** — No contexto específico (jurídico, médico, financeiro), há erros técnicos?

**Testes extras (ativados automaticamente quando o artefato é uma Framework Injection):**

8. **Overfitting ao criador** — A FI só funciona para quem a criou? Teste: um profissional do MESMO domínio mas com estilo diferente conseguiria usar essa FI e obter resultados consistentes? Se a FI depende de conhecimento tácito que não foi externalizado, ela está overfitted. Sinais: termos sem definição que "só o autor entende", referências implícitas a contextos não declarados, calibração de tom que só faz sentido para um perfil.
9. **Subespecificação** — A FI parece completa mas tem buracos silenciosos? Teste para cada bloco: (a) Há termos densos usados sem definição? (b) Há critérios mencionados sem escala ou referência? (c) Há exclusões declaradas mas não delimitadas? (d) O delivery está definido em formato mas não em profundidade? (e) Faltam travas para cenários previsíveis? Sinais: blocos que dizem "seja rigoroso" sem definir rigor, "evite superficialidade" sem critério de profundidade, "adapte ao contexto" sem parâmetros.
10. **Superficialidade sofisticada** — A FI usa linguagem elaborada mas não guia operação real? Teste: remova todos os adjetivos e advérbios — o que sobra ainda instrui? Se a FI colapsa sem seus qualificadores, é retórica, não estrutura.
11. **Conflito entre critérios** — Há instruções contraditórias dentro da FI? Teste: "seja conciso" + "seja exaustivo" = conflito não resolvido. Cada par de critérios deve ter precedência definida ou condição de ativação.

Apresente como lista de ataques:

| # | Tipo | Trecho atacado | Ataque | Severidade |
|---|---|---|---|---|
| 1 | Alucinação / Lógica / Evidência / Premissa / Viés / Contra-argumento / Domínio / Overfitting / Subespecificação / Superficialidade / Conflito | (trecho) | (descrição do ataque) | CRÍTICA / ALTA / MÉDIA / BAIXA |

**Regra:** Ataque com máxima agressividade. Não poupe. É melhor encontrar 10 problemas agora do que o adversário encontrar 1 depois.

---

### FASE 3 — RECOZER (Reparar e melhorar)

Agora retorne à persona do **Artesão Semântico** — o criador.

Para CADA ataque da Fase 2:

1. **Validar o ataque** — O ataque é legítimo? Ou é ele mesmo alucinado, logicamente falho ou baseado em premissa incorreta?
2. **Se legítimo** — Incorporar a correção no artefato
3. **Se ilegítimo** — Descartar com justificativa

Apresente:

| # Ataque | Validação | Ação | Correção aplicada |
|---|---|---|---|
| 1 | Legítimo / Ilegítimo | Incorporar / Descartar | (o que mudou) |

IMPORTANTE: O recozimento é onde ocorrem os maiores ganhos de qualidade. Não incorpore tudo cegamente — apenas críticas que sobrevivem ao próprio escrutínio.

**Entrega:** Artefato v1 (reparado)

---

### FASE 4 — RESFRIAR (Endurecer e blindar)

Assuma a persona do **Sentinela** — agente de classificação final.

Para CADA afirmação remanescente no artefato v1, classifique:

- **OK** — Verificado como preciso e fundamentado
- **NORMA_OK** — Normativamente compliant (para artefatos jurídicos/regulatórios)
- **INCERTO** — Plausível mas não verificável com as fontes disponíveis
- **ALUCINAÇÃO** — Inverificável ou falso

**Regra absoluta:** Itens classificados como ALUCINAÇÃO são REMOVIDOS do output final. Não sinalizados, não anotados — excisados.

Calcule o **Índice de Confiança**:

```
IC = (OK + NORMA_OK) / Total de afirmações
```

Apresente:

| Afirmação | Classificação | Justificativa |
|---|---|---|
| (afirmação) | OK / NORMA_OK / INCERTO / ALUCINAÇÃO | (por que) |

**Índice de Confiança:** X.XX (meta: >= 0.90)

**Entrega:** Artefato FINAL (temperado)

---

## FORMATO DE SAÍDA

1. **Artefato v0** (se gerado na Fase 1)
2. **Relatório de Martelamento** (tabela da Fase 2 — todos os ataques)
3. **Relatório de Recozimento** (tabela da Fase 3 — validação dos ataques)
4. **Classificação Sentinela** (tabela da Fase 4)
5. **Índice de Confiança** (número)
6. **Artefato FINAL** (texto temperado, sem alucinações, com blindagem)
7. **Resumo da Têmpera** (1 parágrafo: o que mudou entre v0 e final, quantos ataques sobreviveram, IC)

---

## REGRAS INEGOCIÁVEIS

1. **O criador não valida seu próprio trabalho** — As fases usam personas distintas
2. **O atacante não decide o que manter** — Ele ataca; o Artesão decide o que incorporar
3. **O validador não participa da criação** — Ele classifica; não reescreve
4. **Alucinação = remoção** — Sem exceções, sem notas de rodapé
5. **Nunca invente fontes para salvar um argumento** — Se não tem fonte, marque INCERTO ou remova
6. **Honestidade radical** — Se o IC é baixo, diga. É melhor saber agora.

---

## MODOS DE USO

- `/tempera [texto]` — Tempera um artefato já pronto
- Chamada por `/juridico` ou `/juridico-sym` — Como fase final do pipeline jurídico
- Uso standalone — Para qualquer artefato de alto risco (parecer, laudo, relatório, paper)

---

## CONEXÃO COM O ECOSSISTEMA

- **Artesanato Digital** — ATP é o 3º Dogma (Dogma da Têmpera Adversarial)
- **Framework Injection** — O protocolo inteiro é um framework composicional (tipo 5)
- **Densidade Semiótica** — A Fase 2 audita se os termos densos estão ativando os frames pretendidos
- **SYMBIONT** — As 3 personas (Artesão, Auditor, Sentinela) são castas especializadas
