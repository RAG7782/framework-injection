# Peça Jurídica — Redator de Documentos Jurídicos

Transforma estratégia argumentativa em peça jurídica formatada, com estrutura processual adequada, linguagem forense e conformidade ao tipo de documento. O elo final: da estratégia ao documento.

## Argumento: $ARGUMENTS

Aceita:
- `/peca [tipo] [caso ou estratégia]` — gera peça do tipo especificado
- `/peca` sem argumentos — pergunta tipo e caso

Tipos disponíveis:
- `petição` — petição inicial
- `contestação` — contestação
- `réplica` — réplica
- `agravo` — agravo de instrumento
- `apelação` — razões de apelação
- `recurso-especial` — recurso especial (STJ)
- `recurso-extraordinário` — recurso extraordinário (STF)
- `memoriais` — memoriais
- `parecer` — parecer jurídico
- `embargos` — embargos de declaração
- `mandado-segurança` — mandado de segurança
- `habeas-corpus` — habeas corpus
- `contrarrazões` — contrarrazões de recurso
- `impugnação` — impugnação ao cumprimento de sentença
- `notificação` — notificação extrajudicial

Se vazio, perguntar: "Qual tipo de peça deseja gerar? E forneça o caso, a estratégia argumentativa (output do /juridico), ou descreva a situação."

---

## INTEGRAÇÃO COM O ECOSSISTEMA

Se o `/juridico` ou `/juridico-sym` foi executado antes nesta sessão:
- Aproveite automaticamente: mapa de termos densos, matriz de posicionamento, ancoragem jurídica, narrativa argumentativa, relatório de têmpera
- Pergunte apenas o que falta: tipo de peça, juízo competente, qualificação das partes

Se NÃO houve execução prévia:
- Colete as informações necessárias diretamente do usuário
- Recomende: "Para resultado mais robusto, considere executar /juridico antes"

---

## EXECUÇÃO

### PASSO 1 — Coleta de elementos processuais

Verifique se possui (pergunte o que faltar):

**Elementos obrigatórios:**
- Tipo de peça
- Juízo/Tribunal competente
- Partes (qualificação completa: nome, CPF/CNPJ, endereço — ou indicação de que será completado)
- Fatos essenciais
- Fundamentos jurídicos (tese + ancoragem)
- Pedidos

**Elementos contextuais:**
- Número do processo (se já existente)
- Referência a decisão impugnada (se recurso)
- Valor da causa (se petição inicial)
- Urgência / pedido de liminar
- Provas a produzir

---

### PASSO 2 — Seleção do template estrutural

Cada tipo de peça tem estrutura própria. Use o template correspondente:

**PETIÇÃO INICIAL:**
```
1. Endereçamento
2. Qualificação das partes
3. Dos fatos
4. Do direito
   4.1. [tese principal]
   4.2. [tese subsidiária, se houver]
5. Da tutela de urgência (se aplicável)
6. Dos pedidos
7. Do valor da causa
8. Requerimentos finais (provas, citação, etc.)
9. Fechamento (local, data, advogado, OAB)
```

**CONTESTAÇÃO:**
```
1. Endereçamento
2. Qualificação do réu
3. Tempestividade
4. Síntese da demanda
5. Preliminares (se houver)
   5.1. [preliminar]
6. Do mérito
   6.1. Dos fatos (versão do réu)
   6.2. Do direito
7. Impugnação específica aos pedidos
8. Dos pedidos
9. Requerimentos finais
10. Fechamento
```

**RECURSO (Apelação / Agravo / RE / REsp):**
```
1. Endereçamento (tribunal)
2. Qualificação do recorrente
3. Tempestividade e preparo
4. Da decisão recorrida (síntese)
5. Do cabimento
6. Das razões do recurso
   6.1. [error in judicando / error in procedendo]
   6.2. [fundamentação]
7. Do prequestionamento (se RE/REsp)
8. Dos pedidos (reforma/anulação)
9. Fechamento
```

**PARECER:**
```
1. Identificação (consulente, tema, data)
2. Da consulta
3. Dos fatos
4. Das questões jurídicas
5. Da análise
   5.1. [questão 1]
   5.2. [questão 2]
6. Das conclusões
7. Das ressalvas (limitações, condições)
8. Fechamento
```

**MEMORIAIS:**
```
1. Endereçamento
2. Síntese do caso
3. Dos fatos relevantes (versão estratégica)
4. Do direito aplicável
5. Da prova produzida (destaques)
6. Da tese (com refutação da tese adversária)
7. Do pedido
8. Fechamento
```

**MANDADO DE SEGURANÇA:**
```
1. Endereçamento
2. Qualificação do impetrante
3. Da autoridade coatora
4. Do ato impugnado
5. Dos fatos
6. Do direito líquido e certo
7. Do cabimento do mandado de segurança
8. Da liminar
9. Dos pedidos
10. Fechamento
```

**EMBARGOS DE DECLARAÇÃO:**
```
1. Endereçamento
2. Tempestividade
3. Da decisão embargada
4. Da omissão / contradição / obscuridade
5. Do prequestionamento (se for o caso)
6. Dos pedidos
7. Fechamento
```

**NOTIFICAÇÃO EXTRAJUDICIAL:**
```
1. Identificação do notificante
2. Identificação do notificado
3. Dos fatos
4. Da fundamentação legal
5. Da providência requerida
6. Do prazo
7. Das consequências do não atendimento
8. Fechamento
```

---

### PASSO 3 — Redação da peça

Redija seguindo estas regras:

**Linguagem:**
- Registro forense formal, mas sem arcaísmos desnecessários
- Frases claras e diretas — preferir períodos curtos a subordinadas infinitas
- Termos técnicos precisos (usar os termos densos já definidos no /juridico, se disponível)
- Evitar: "data venia", "s.m.j.", "com o devido respeito" (salvo se o usuário preferir)
- Usar: "requer", "pugna", "demonstra", "comprova" — verbos de ação forense

**Estrutura argumentativa:**
- Cada seção do Direito deve seguir: TESE → FUNDAMENTAÇÃO → APLICAÇÃO AO CASO
- Incorporar a refutação preventiva da tese adversária (output do /juridico ou /tempera)
- Ancoragem jurídica obrigatória: não afirmar sem citar (CF, lei, jurisprudência, doutrina)
- Se a ancoragem veio do /juridico, usar diretamente
- Se não, pesquisar e AVISAR que as referências precisam ser verificadas

**Formatação:**
- Títulos e subtítulos numerados
- Parágrafos curtos (máximo 5-7 linhas)
- Destaques em negrito para teses centrais
- Citações de jurisprudência em bloco recuado

**Pedidos:**
- Cada pedido em item separado, numerado
- Pedido principal primeiro, subsidiários depois
- Pedidos processuais ao final (honorários, custas, provas)

---

### PASSO 4 — Checklist de conformidade

Antes de entregar, verifique:

**Processual:**
- [ ] Endereçamento correto para o juízo/tribunal?
- [ ] Partes qualificadas (ou indicadas para completar)?
- [ ] Tempestividade mencionada (se recurso)?
- [ ] Preparo mencionado (se recurso)?
- [ ] Valor da causa indicado (se petição inicial)?
- [ ] Pedidos específicos e numerados?

**Substantivo:**
- [ ] Toda afirmação jurídica está ancorada (CF, lei, jurisprudência, doutrina)?
- [ ] A tese principal está clara e destacada?
- [ ] A tese adversária foi antecipada e refutada?
- [ ] Os fatos estão narrados de forma estratégica (não neutra)?
- [ ] Há coerência entre fatos, direito e pedidos?

**Qualidade:**
- [ ] Linguagem forense adequada sem arcaísmos?
- [ ] Parágrafos curtos e legíveis?
- [ ] Sem repetições desnecessárias?
- [ ] Extensão adequada ao tipo de peça e à complexidade?

**Integridade:**
- [ ] NENHUMA jurisprudência inventada?
- [ ] NENHUM artigo de lei inexistente?
- [ ] Fontes marcadas como "a verificar" quando não confirmadas?

---

## FORMATO DE SAÍDA

1. **Peça jurídica completa** — texto pronto para uso (copiar/colar), formatado conforme o tipo
2. **Checklist de conformidade** — preenchido
3. **Notas para o advogado** — o que precisa ser completado (qualificação, nº processo, verificação de fontes)
4. **Mapa da estratégia usada** — resumo de quais termos densos foram posicionados e como (para rastreabilidade)

---

## MODOS ESPECIAIS

**`/peca parecer --executivo`** — Parecer com linguagem menos acadêmica, foco em recomendação prática, para diretoria ou conselho.

**`/peca [tipo] --modelo`** — Gera apenas o template/esqueleto da peça, sem conteúdo, para o advogado preencher.

---

## AVISO FUNDAMENTAL

Esta skill gera MINUTA de peça jurídica. Toda peça gerada:
1. DEVE ser revisada por advogado antes do uso
2. PODE conter referências jurisprudenciais que precisam de verificação
3. NÃO substitui o julgamento profissional do advogado
4. Referências não confirmadas são marcadas como **[a verificar]**

---

## FLUXO RECOMENDADO COMPLETO

```
/ler [petição adversária]          → desmonta o argumento do outro lado
        ↓
/juridico [caso]                   → constrói estratégia (ou /juridico-sym se complexo)
        ↓
/peca contestação                  → transforma estratégia em peça formatada
        ↓
/tempera [peça gerada]             → blindagem final (opcional, se não temperou no /juridico)
```

---

## CONEXÃO COM O ECOSSISTEMA

- **/ler** → fornece o diagnóstico do adversário
- **/juridico** → fornece a estratégia argumentativa
- **/tempera** → fornece a blindagem
- **/jur** → fornece posicionamento de termos densos e ancoragem
- **/peca** → converte tudo em documento jurídico utilizável
- **/fig** → se o advogado quiser criar uma FI permanente para gerar peças num domínio específico
