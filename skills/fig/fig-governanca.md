# FIG Governança — Ficha Técnica e Controle de Framework Injection

Gera a documentação de governança de uma Framework Injection: quando usar, quando não usar, riscos, limites, necessidade de revisão humana, histórico de versões. Impede que a FI vire peça solta sem controle.

## Argumento: $ARGUMENTS

Se chamado pelo `/fig`, recebe a FI final. Se standalone: "Cole a Framework Injection para a qual deseja gerar a ficha de governança."

---

## EXECUÇÃO

### Gerar Ficha de Governança

```
═══════════════════════════════════════════
FICHA DE GOVERNANÇA — FRAMEWORK INJECTION
═══════════════════════════════════════════

IDENTIFICAÇÃO
  Nome: [nome descritivo da FI]
  Versão: [X.Y]
  Data de criação: [data]
  Autor/Domínio: [quem criou / para qual domínio]
  Temperada: [Sim/Não] — IC: [valor]

PROPÓSITO
  Para que serve: [descrição em 1-2 frases]
  Problema que resolve: [o que acontecia sem ela]

CONTEXTO DE USO
  Quando usar:
    - [situação 1]
    - [situação 2]
    ...

  Quando NÃO usar:
    - [situação 1 — e por quê]
    - [situação 2 — e por quê]
    ...

PÚBLICO-ALVO
  Quem pode usar: [perfil mínimo de quem opera a FI]
  Conhecimento prévio necessário: [o que o operador precisa saber]

DEPENDÊNCIAS
  Modelo mínimo recomendado: [Haiku/Sonnet/Opus — e por quê]
  Contexto mínimo: [tamanho estimado em tokens]
  Dados externos necessários: [fontes, bases, documentos]

RISCOS CONHECIDOS
  - [risco 1] — mitigação: [como lidar]
  - [risco 2] — mitigação: [como lidar]
  ...

LIMITES DE CONFIANÇA
  A FI é confiável para: [escopo]
  A FI NÃO é confiável para: [fora do escopo]
  Índice de Confiança da têmpera: [valor]
  Vulnerabilidades residuais: [o que a têmpera não conseguiu eliminar]

REVISÃO HUMANA
  Necessária antes de: [decisões de alto risco / publicação / uso externo]
  Frequência de revisão: [a cada X meses / a cada mudança de contexto]
  Responsável pela revisão: [quem]

VARIANTES DISPONÍVEIS
  - [variante 1] — para [público/contexto]
  - [variante 2] — para [público/contexto]
  ...

HISTÓRICO DE VERSÕES
  v1.0 — [data] — versão inicial
  v1.1 — [data] — [o que mudou e por quê]
  ...

CONEXÃO COM O ECOSSISTEMA
  Skills usadas na criação: [/fig-extrair, /agora, /fig-construir, /tempera, etc.]
  Programa de pesquisa: Artisanal Intelligence Program
  Princípios: Artesanato Digital, Framework Injection, Densidade Semiótica

═══════════════════════════════════════════
```

---

## REGRAS

1. **Toda FI precisa de ficha** — FI sem governança é FI fora de controle
2. **Limites de confiança são obrigatórios** — Nunca afirmar que uma FI é "universal"
3. **Riscos devem ser honestos** — Se a têmpera encontrou vulnerabilidades, elas aparecem aqui
4. **"Quando NÃO usar" é tão importante quanto "quando usar"**
5. **Revisão humana tem frequência definida** — Não é "quando der"
