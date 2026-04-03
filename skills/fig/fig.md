# FIG — Framework Injection Generator

Orquestrador adaptativo para criação de Framework Injections. Transforma conhecimento tácito em instruções semântico-estratégicas robustas, auditáveis e reutilizáveis.

Não é um gerador de prompts. É um sistema de externalização, estruturação, validação e operacionalização da inteligência humana.

## Argumento: $ARGUMENTS

Aceita flags opcionais:
- `--didatico` → Modo didático: entre cada fase, explica o que está fazendo e por quê (para curso/aprendizagem)
- `--rapido` → Pula variantes e governança (para prototipagem rápida)
- `--validar` → Ao final, executa /fig-validar automaticamente

Se vazio, perguntar: "Para qual domínio de conhecimento você quer criar uma Framework Injection? Descreva sua área, objetivo e público-alvo."

---

## INTEGRAÇÃO COM MEMÓRIA (IMI)

Antes de iniciar a Fase 1, verifique se existe perfil cognitivo salvo:
- Busque em `/Users/renatoaparegomes/experimentos/framework-injections/perfis/` por perfil do usuário
- Se encontrar: carregue e pergunte "Encontrei seu perfil de [data]. Deseja reutilizá-lo ou começar do zero?"
- Se não encontrar: prossiga normalmente com a entrevista completa

---

## AVALIAÇÃO DE COMPLEXIDADE (automática)

Antes de iniciar, avalie o caso e decida o modo:

| Indicador | Simples | Complexo |
|---|---|---|
| Domínios envolvidos | 1 | 2+ |
| Públicos-alvo | 1 | 3+ |
| Nível de risco | Baixo/Médio | Alto/Crítico |
| Variantes necessárias | 0-1 | 3+ |
| Tensões internas do domínio | Poucas | Muitas |

**Modo Linear:** Maioria simples → pipeline sequencial, mais rápido
**Modo Adaptativo:** Maioria complexo → pode voltar a fases anteriores, gerar pods especializados, ativar quorum

Declare o modo escolhido antes de começar.

---

## PIPELINE

```
/fig [objetivo]
  │
  ├── Avaliação de complexidade → Linear ou Adaptativo
  │
  ▼
FASE 1 — EXTRAIR (/fig-extrair)
  Entrevista maiêutica
  Perfil cognitivo
  Ontologia artesanal
  Pré-classificação de termos densos
  │
  ▼
FASE 2 — ESCANEAR (/ler + /agora)
  /ler: análise dos termos densos do domínio
  /agora: rotações semânticas, subtrações, hipocampo
  Produto: Matriz de Densidade Semiótica completa
  │
  ▼
FASE 3 — CONSTRUIR (/fig-construir)
  Pré-processamento de densidade (gap M3 → 100%)
  Construção dos 8 blocos da FI
  Arquitetura de delivery
  Produto: Framework Injection v1
  │
  ▼
FASE 4 — TEMPERAR (/tempera)
  11 testes (7 universais + 4 específicos FI)
  Ciclo recozer → resfriar
  Se IC < 0.80 → volta para FASE 3 (modo adaptativo)
  Produto: Framework Injection v2 (temperada)
  │
  ▼
FASE 5 — VARIAR (/fig-variantes) [opcional]
  Só se o perfil pedir múltiplos públicos/contextos
  Gera versões: técnica, didática, executiva, litigiosa, agente
  Produto: Biblioteca de variantes
  │
  ▼
FASE 6 — GOVERNAR (/fig-governanca)
  Ficha técnica completa
  Limites, riscos, revisão
  Produto: Ficha de governança
```

---

## MODO ADAPTATIVO — Regras especiais

Quando em modo adaptativo, as seguintes regras se ativam:

**Retroalimentação:** Se a têmpera (Fase 4) encontra falhas críticas, o pipeline volta:
- Falha de densidade → volta para Fase 2 (escanear melhor)
- Falha de estrutura → volta para Fase 3 (reconstruir)
- Falha de extração → volta para Fase 1 (perguntar mais ao usuário)

**Pods especializados:** Se o domínio cruza áreas (ex: tributário + constitucional), a Fase 2 forma investigações paralelas por área antes de consolidar.

**Quorum de decisão:** Para FIs de alto risco:
- Construção + Têmpera devem concordar na versão final
- Se discordarem, escalar ao usuário com as duas versões e a divergência explícita

---

## FORMATO DE SAÍDA FINAL

### I. Perfil e Domínio
- Perfil cognitivo do usuário
- Ontologia artesanal do domínio

### II. Matriz de Densidade
- Termos densos classificados
- Operações SDE aplicadas
- Insights do AGORA (rotações, subtrações)

### III. Framework Injection
- Versão final temperada (8 blocos completos)
- IC (Índice de Confiança)
- Notas de construção (decisões e justificativas)

### IV. Variantes (se geradas)
- Tabela comparativa
- Cada variante com texto completo

### V. Governança
- Ficha técnica completa
- Limites e riscos
- Protocolo de revisão

### VI. Síntese
- O que essa FI faz que um prompt genérico não faz
- Onde está o valor agregado (em 1 parágrafo)
- Recomendação de próximos passos

---

## CRITÉRIOS DE SUCESSO

A FI gerada é bem-sucedida quando:

1. Extrai conhecimento tácito do usuário com poucas interações
2. Transforma isso em FI reutilizável
3. Explica por que cada bloco existe
4. Detecta ambiguidades antes que virem erro
5. Gera versões calibradas para contextos distintos
6. Resiste a 11 testes adversariais
7. Produz delivery realmente útil
8. O usuário se reconhece nela

---

## PRINCÍPIO FUNDACIONAL

> O risco número 1 é criar uma FI que fala bonito mas não modela nada de verdade.
> Sinais de alerta: excesso de abstração, termos sofisticados sem função, frameworks longas e pouco operacionais, ausência de teste adversarial real, delivery sem conexão com uso.
> Em resumo: luxo verbal sem musculatura semântica.

---

## PERSISTÊNCIA (salvar tudo em arquivos)

Ao final de CADA execução, salve automaticamente os artefatos:

```
/Users/renatoaparegomes/experimentos/framework-injections/
  perfis/
    [usuario]-perfil-cognitivo.md          → reutilizável entre sessões
  [slug-do-dominio]/
    README.md                               → índice do que foi gerado
    perfil-cognitivo.md                     → Fase 1
    ontologia.md                            → Fase 1
    matriz-densidade.md                     → Fase 2
    fi-v1.md                                → Fase 3 (antes da têmpera)
    fi-v2-temperada.md                      → Fase 4 (versão final)
    relatorio-tempera.md                    → Fase 4
    governanca.md                           → Fase 6
    variantes/                              → Fase 5 (se geradas)
      tecnica.md
      didatica.md
      executiva.md
      litigiosa.md
      agente.md
    validacao/                              → se --validar foi usado
      relatorio-comparativo.md
```

Use Write tool para criar os arquivos. Pergunte ao usuário o nome/slug do domínio.

---

## MODO DIDÁTICO (--didatico)

Quando a flag `--didatico` estiver ativa, entre CADA fase:

1. **Explique O QUE vai fazer:** "Agora vamos [ação]. Isso serve para [objetivo]."
2. **Explique O PRINCÍPIO por trás:** "Esse passo se baseia em [conceito]. A ideia é que [explicação acessível]."
3. **Mostre UM EXEMPLO antes de executar:** "Por exemplo, num domínio de [X], isso ficaria assim: [exemplo curto]."
4. **Após executar, destaque O INSIGHT:** "Perceba que [observação não óbvia sobre o resultado]."

O modo didático transforma a ferramenta em experiência de aprendizagem. O aluno não apenas recebe a FI — ele entende como e por que cada peça foi construída.

Conexão com cada princípio:

| Fase | Princípio explicado |
|---|---|
| Extrair | Polanyi — conhecimento tácito: "Você sabe mais do que consegue dizer" |
| Escanear | Densidade Semiótica — "Palavras pequenas por fora, enormes por dentro" |
| Construir | Framework Injection — "Não é instruir, é transferir raciocínio" |
| Temperar | ATP — "Validação verifica; têmpera transforma" |
| Variar | Vygotsky — "Scaffold para iniciantes, bússola para experts" |
| Governar | Lakatos — "Programa de pesquisa com núcleo duro e cinturão protetor" |

---

## CONEXÃO COM O ECOSSISTEMA

| Componente | Papel no FIG |
|---|---|
| **Artesanato Digital** | Filosofia fundacional — cada FI é peça artesanal |
| **Framework Injection** | O produto — o que o sistema gera |
| **Densidade Semiótica** | O motor analítico — como os termos são tratados |
| **SDE (5 operações)** | As ferramentas — densificar, rarefazer, rotacionar, subtrair, mesclar |
| **Têmpera Adversarial** | O controle de qualidade — 11 testes |
| **AGORA Intelligence** | O descobridor — ângulos invisíveis |
| **STEER** | Infraestrutura quantitativa — onde SDE opera no embedding |
| **IMI** | Memória — preserva a FI entre interações |
| **SYMBIONT** | Orquestração bio-inspirada (modo adaptativo) |
