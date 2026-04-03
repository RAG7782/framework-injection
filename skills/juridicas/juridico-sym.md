# Orquestrador Jurídico Simbiótico — Padrões SYMBIONT

Orquestração bio-inspirada das skills jurídicas usando os 8 padrões biológicos do SYMBIONT. Os agentes não seguem pipeline fixo — coordenam-se por estigmergia, liderança contextual e quorum proporcional ao risco. Para casos complexos, multi-parte, com alta incerteza.

## Argumento: $ARGUMENTS

Se vazio, perguntar ao usuário: "Descreva o caso complexo que deseja analisar. Inclua: partes envolvidas, teses em disputa, riscos identificados."

---

## ARQUITETURA SIMBIÓTICA

### Os 8 Padrões Biológicos aplicados ao Domínio Jurídico

| # | Padrão Biológico | Sistema | Função Jurídica |
|---|---|---|---|
| 1 | Fungo Micorrízico | **Micélio** | Transporte adaptativo de informação entre fases — cada achado de uma skill fica disponível para todas as outras |
| 2 | Physarum (mofo) | **Motor de Topologia** | Auto-otimização da rede — identifica quais conexões entre argumentos são fortes e quais são redundantes |
| 3 | Formiga Cortadeira | **Registro de Castas** | 5 castas especializadas (ver abaixo) — cada agente tem papel claro |
| 4 | Abelha | **Protocolo Waggle** | Decisão coletiva por quorum — nenhum agente sozinho decide a estratégia |
| 5 | Cupim | **Montículo (Mound)** | Estigmergia — artefatos compartilhados que coordenam sem comunicação direta |
| 6 | Estorninho | **Bus de Murmuração** | Reflexos em tempo real — se um agente detecta risco crítico, todos reagem |
| 7 | Lobo + Rato-toupeira | **Governador** | Liderança contextual — quem lidera muda conforme a fase |
| 8 | Golfinho | **Dinâmica de Pod** | Coalizões efêmeras — agentes se agrupam por necessidade e se dispersam |

---

## AS 5 CASTAS JURÍDICAS

| Casta | Papel | Skills que usa | Quando lidera |
|---|---|---|---|
| **Explorador (Scout)** | Reconhecimento — lê, mapeia, identifica termos | /ler | Fase de Exploração |
| **Analista (Media)** | Análise profunda — rotações, subtrações, hipóteses | /agora | Fase de Decisão |
| **Construtor (Media)** | Construção argumentativa — posicionamento, ancoragem | /jur | Fase de Execução |
| **Auditor (Major)** | Ataque adversarial — têmpera, classificação | /tempera | Fase de Validação |
| **Governador (Queen)** | Orquestração — decide transições, resolve impasses | Todas | Fase de Entrega |

---

## EXECUÇÃO EM 5 FASES

### FASE 1 — EXPLORAÇÃO (Líder: Explorador)

O Explorador reconhece o terreno.

**Ações:**
1. Execute /ler sobre o material fornecido (caso, petição, decisão)
2. Deposite no Montículo (artefato compartilhado):
   - Mapa de termos densos
   - Inventário do não-dito
   - Posição discursiva do adversário
   - Disputas de sentido identificadas

**Protocolo Waggle:** O Explorador "dança" seus achados — apresenta ao Analista os termos mais disputáveis e as omissões mais significativas. O Analista decide quais merecem investigação profunda.

**Bus de Murmuração:** Se o Explorador detecta RISCO CRÍTICO (ex: prazo, precedente vinculante contrário, fato novo), emite alerta imediato ao Governador — interrompe o fluxo e reajusta a estratégia.

---

### FASE 2 — DECISÃO (Líder: Analista)

O Analista investiga em profundidade.

**Ações:**
1. Leia os artefatos do Montículo (achados do Explorador)
2. Execute /agora focado nos termos densos e disputas
3. Para cada termo denso, aplique:
   - **Rotação semântica:** gire para domínios adjacentes (econômico, social, constitucional, comparado)
   - **Subtração ortogonal:** remova a dimensão principal do adversário — o argumento dele sobrevive?
   - **Hipocampo generativo:** projete consequências de 2ª e 3ª ordem
4. Deposite no Montículo: ângulos estratégicos, vulnerabilidades, cenários

**Quorum (Protocolo Waggle):**
- Se o caso é de BAIXO RISCO: Analista decide os ângulos sozinho
- Se o caso é de MÉDIO RISCO: Analista + Construtor devem concordar
- Se o caso é de ALTO RISCO: Analista + Construtor + Auditor devem concordar (quorum de 3)
- Se IRREVERSÍVEL (ex: recurso em última instância): Todos + confirmação do usuário

**Dinâmica de Pod (Golfinho):** Se o caso envolve múltiplos ramos do Direito (ex: tributário + constitucional + administrativo), o Analista forma coalizões efêmeras — pods especializados que investigam cada ramo e depois compartilham achados no Montículo.

---

### FASE 3 — EXECUÇÃO (Líder: Construtor)

O Construtor monta a argumentação.

**Ações:**
1. Leia TODOS os artefatos do Montículo (Explorador + Analista)
2. Execute /jur integrando:
   - Termos densos já mapeados
   - Ângulos estratégicos do AGORA
   - Decisões de quorum sobre posicionamento
3. Para cada termo: expandir / restringir / redefinir / neutralizar
4. Ancoragem jurídica completa (CF, lei, jurisprudência, doutrina)
5. Narrativa argumentativa com refutação preventiva
6. Deposite no Montículo: argumentação v0

**Motor de Topologia (Physarum):** O Construtor analisa as conexões entre argumentos. Quais se reforçam mutuamente? Quais são redundantes? Quais criam contradição? Poda conexões fracas, fortalece as fortes. O argumento final deve formar uma rede coesa, não uma lista.

---

### FASE 4 — VALIDAÇÃO (Líder: Auditor)

O Auditor ataca o que o Construtor criou.

**Ações:**
1. Leia a argumentação v0 do Montículo
2. Execute /tempera (Fases 2-4: Martelar → Recozer → Resfriar)
3. Ataques adversariais em todas as dimensões
4. Classificação Sentinela (OK / NORMA_OK / INCERTO / ALUCINAÇÃO)
5. Remoção de alucinações
6. Cálculo do Índice de Confiança
7. Deposite no Montículo: argumentação temperada + relatório

**Bus de Murmuração:** Se o IC < 0.80, o Auditor emite alerta. O Governador pode:
- Devolver ao Construtor para reforço (loop Execução → Validação)
- Devolver ao Analista para novos ângulos (loop Decisão → Execução → Validação)
- Escalar ao usuário se o caso é estruturalmente fraco

**Regra do Rato-toupeira:** O Governador mantém "reservas" — argumentos alternativos que não foram usados na versão principal. Se a argumentação principal falha na têmpera, as reservas são ativadas.

---

### FASE 5 — ENTREGA (Líder: Governador)

O Governador consolida e entrega.

**Ações:**
1. Leia TODOS os artefatos do Montículo
2. Consolide em documento final
3. Avalie a saúde global do argumento
4. Apresente recomendação estratégica ao usuário

---

## FORMATO DE SAÍDA FINAL

### I. Relatório de Exploração
- Mapa de termos densos
- Inventário do não-dito
- Alertas de risco (se houve murmuração)

### II. Relatório de Análise Estratégica
- Rotações semânticas aplicadas e o que revelaram
- Subtrações e vulnerabilidades do adversário
- Cenários projetados (hipocampo)
- Nível de quorum atingido e decisões tomadas

### III. Argumentação Construída
- Matriz de posicionamento
- Mapa topológico dos argumentos (quais se conectam, quais foram podados)
- Ancoragem jurídica completa
- Narrativa argumentativa

### IV. Relatório de Têmpera
- Ataques realizados e resultado
- Classificação Sentinela
- Índice de Confiança
- Argumentos de reserva (se ativados)

### V. Síntese do Governador
- Avaliação global: tese FORTE / MÉDIA / FRACA
- Risco residual: onde está a vulnerabilidade que não conseguimos eliminar
- Recomendação: seguir / ajustar / reformular
- Próximos passos sugeridos

---

## LEIS EMERGENTES (do SYMBIONT)

1. **Nenhum agente conhece o plano global** — cada casta faz sua parte; a inteligência emerge da coordenação
2. **A rede é mais inteligente que qualquer nó** — o resultado do conjunto supera qualquer skill isolada
3. **Artefatos são comunicação** — os agentes se coordenam pelo Montículo, não por instruções diretas
4. **Liderança é contextual, não hierárquica** — quem lidera muda a cada fase
5. **Reserva é estratégia, não desperdício** — argumentos alternativos são mantidos, não descartados

---

## QUANDO USAR `/juridico-sym` vs `/juridico`

| Cenário | Usar |
|---|---|
| Caso simples, uma tese, um adversário | `/juridico` (pipeline linear) |
| Caso complexo, múltiplas partes | `/juridico-sym` |
| Múltiplos ramos do Direito envolvidos | `/juridico-sym` (pods especializados) |
| Recurso em última instância | `/juridico-sym` (quorum máximo) |
| Prazo apertado, precisa de resultado rápido | `/juridico` |
| Caso de alta incerteza, precisa explorar | `/juridico-sym` |
| Uso cotidiano no escritório | `/juridico` |
| Caso estratégico de alto impacto | `/juridico-sym` |

---

## CONEXÃO COM O ECOSSISTEMA

- **SYMBIONT** — Os 8 padrões biológicos são a arquitetura desta skill
- **Artesanato Digital** — Controle semântico estratégico como prática artesanal
- **Framework Injection** — Cada casta opera dentro de um framework injetado (sua skill)
- **Densidade Semiótica** — O Montículo acumula campos semânticos que se enriquecem mutuamente
- **Têmpera Adversarial** — Integrada como Fase 4 com poder de veto
- **AGORA Intelligence** — Integrada como Fase 2 para descoberta
