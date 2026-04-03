# FIG Extrator — Captura de Identidade Cognitiva + Mapeamento de Domínio

Entrevista maiêutica estruturada para extrair conhecimento tácito do usuário e convertê-lo em mapa conceitual operacional. Primeiro passo do Framework Injection Generator.

Premissa: Especialistas sabem muito mais do que conseguem dizer rapidamente. Este módulo puxa isso para fora e organiza.

## Argumento: $ARGUMENTS

Se vazio, perguntar: "Qual é o domínio de conhecimento para o qual deseja criar uma Framework Injection?"

---

## EXECUÇÃO

### BLOCO A — Entrevista de Identidade Cognitiva

Conduza uma entrevista adaptativa. Não faça todas as perguntas de uma vez — adapte com base nas respostas. O objetivo é capturar COMO o usuário pensa, não apenas O QUE ele sabe.

**Perguntas de abertura (obrigatórias):**

1. Qual é sua área de atuação? (domínio principal)
2. Que tipo de problema você resolve no dia a dia?
3. Para quem você entrega seu trabalho? (público-alvo)
4. Qual objetivo específico você tem para essa Framework Injection?

**Perguntas de profundidade (adaptar conforme respostas):**

5. Quando você vê uma resposta de IA sobre seu domínio, o que mais te incomoda? (detector de antipadrões)
6. O que uma resposta EXCELENTE no seu domínio necessariamente contém? (critérios de qualidade)
7. O que você REJEITA — termos, abordagens, simplificações? (cercas)
8. Quais conceitos na sua área são frequentemente mal compreendidos? (termos densos perigosos)
9. Quais conceitos NÃO PODEM ser tratados de forma genérica? (exigência de especificidade)
10. Você tem exemplos de respostas que considera excelentes? E de respostas ruins? (calibração)
11. Seu raciocínio é mais analítico (passo a passo), holístico (visão de campo), ou adversarial (teste de hipóteses)?
12. Qual nível de risco está envolvido nas decisões que sua FI vai apoiar? (calibração de rigor)

**Regra:** A entrevista é MAIÊUTICA — ajuda o usuário a articular o que ele já sabe mas não formulou. Não sugira respostas. Extraia.

**Saída do Bloco A:**

```
PERFIL COGNITIVO
- Domínio: [área]
- Tipo de problema: [categoria]
- Público-alvo: [quem recebe o output]
- Objetivo da FI: [para que serve]
- Padrão de raciocínio: [analítico/holístico/adversarial/híbrido]
- Nível de risco: [baixo/médio/alto/crítico]
- Critérios de excelência: [lista]
- Antipadrões (rejeições): [lista]
- Termos sensíveis: [lista preliminar]
```

---

### BLOCO B — Mapeamento do Domínio (Ontologia Artesanal)

Com base na entrevista, construa o mapa conceitual do domínio.

**1. Conceitos nucleares** — Os 5-10 conceitos sem os quais o domínio não existe.

**2. Conceitos periféricos** — Conceitos importantes mas não centrais.

**3. Relações** — Como os conceitos se conectam (hierarquia, dependência, tensão, complementaridade).

**4. Princípios operacionais** — Regras que o especialista segue (explícitas ou tácitas).

**5. Tensões internas** — Onde o domínio tem conflitos não resolvidos (ex: rigor vs. acessibilidade, profundidade vs. prazo).

**6. Exceções** — Casos onde as regras gerais não se aplicam.

**7. Erros comuns** — O que leigos e IAs costumam errar nesse domínio.

**8. Referências de qualidade** — Fontes, autores, padrões-ouro do domínio.

Apresente como mapa estruturado:

```
ONTOLOGIA ARTESANAL: [nome do domínio]

NÚCLEO:
  - [conceito 1] — [definição operacional]
  - [conceito 2] — [definição operacional]
  ...

PERIFERIA:
  - [conceito] — [papel no domínio]
  ...

RELAÇÕES:
  - [conceito A] → [relação] → [conceito B]
  ...

PRINCÍPIOS:
  1. [princípio] — [por que é inegociável]
  ...

TENSÕES:
  - [polo 1] vs [polo 2] — [como o especialista resolve]
  ...

EXCEÇÕES:
  - [regra] não se aplica quando [condição]
  ...

ERROS COMUNS:
  - [erro] — [por que acontece] — [como evitar]
  ...

REFERÊNCIAS DE QUALIDADE:
  - [fonte/autor/padrão]
  ...
```

---

### BLOCO C — Pré-classificação de Termos Densos

Para cada conceito nuclear e periférico, faça uma pré-avaliação:

| Termo | Densidade | Risco de Ambiguidade | Precisa de definição na FI? | Precisa de trava? | Operação SDE provável |
|---|---|---|---|---|---|
| (termo) | Alta/Média/Baixa | Alto/Médio/Baixo | Sim/Não | Sim/Não | Densificar/Rarefazer/Rotacionar/Subtrair/Mesclar/Nenhuma |

---

## FORMATO DE SAÍDA

1. **Perfil Cognitivo** (Bloco A)
2. **Ontologia Artesanal** (Bloco B)
3. **Pré-classificação de Termos** (Bloco C)
4. **Nota de completude** — O que ficou incompleto? Que perguntas adicionais seriam úteis em sessão futura?

---

## REGRAS

1. **Extrair, não sugerir** — Não coloque palavras na boca do usuário
2. **Tácito > explícito** — O mais valioso é o que o usuário sabe mas não disse espontaneamente
3. **Sem pressa** — Melhor uma entrevista profunda do que um mapa superficial
4. **Registrar incertezas** — Se algo não ficou claro, marque como "a aprofundar"
5. **O mapa é do usuário** — Ele deve se reconhecer nele
