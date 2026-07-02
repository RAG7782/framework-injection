# Resumo Executivo — "Artesanato Digital" (Renato)

> 1 página. Tese, modelo mental e os 5 movimentos práticos. Detalhamento completo em `Renato - Destilação.md`.

---

## A tese em uma frase

**Pare de *comandar* a IA; passe a *educá-la*.** A interação humano-LLM hoje é um *pidgin* ("pedir digital") — comunicação rústica de porto. O objetivo é adquirir **fluência**: mais precisão, menos tokens, menos alucinação.

## O modelo mental (3 camadas)

1. **Densidade semiótica** — escolha termos que carregam carga implícita ("selfie", "stress test", "anamnese"). Cada termo denso "acende uma galáxia" no espaço de embedding. *Podar ≠ resumir*: tire ruído sem quebrar o conceito.
2. **Framework Injection (FI)** — transfira seu *método completo de raciocínio* (não só a tarefa) **antes** da inferência. 5 modalidades: declarativa · procedimental · avaliativa · ética · composicional.
3. **Eixo priming ↔ enforcement** — todo elemento do prompt ou **induz** (priming, estocástico, "placa do metrô") ou **obriga** (enforcement, determinístico, "catraca"). A arte é saber escalar de um ao outro.

## O insight central (o de maior valor prático)

**O modelo é réu e juiz na mesma cabeça.** Escrever "a saída deve conter X" não garante nada — quem julga é o próprio modelo, que se auto-aprova. Isso é *priming disfarçado* (confiança).
**Enforcement real = verificador externo.** Um `grep -q X saida.md` é um terceiro determinístico, sem interesse em agradar (exit code 0/1). Isso é **prova**, não confiança.

> Regra de ouro: **toda exigência crítica precisa de um *assert* externo que possa falhar.** Se nada externo verifica, é só sugestão.

## Os 5 movimentos (checklist operacional)

1. **Densifique a entrada** — abra o prompt com o termo mais denso da área ("contrato de compra e venda:", não "analise esse documento").
2. **Injete o método, não só a tarefa** — diga *como* você raciocinaria (passo a passo, hierarquia de fontes, critérios de julgamento).
3. **Âncoras no início e no fim** — papel, objetivo, limites e verificação nas bordas; o miolo do prompt se perde ("lost in the middle"). Repita o termo denso numa *coda* no fim.
4. **Escale priming → enforcement** onde for crítico — troque "deve conter" por um *check* externo (`grep`, schema/structured output, teste, lint).
5. **Valide contra fonte de verdade externa** — nunca aceite a auto-avaliação do modelo nem troque fonte primária por resumo. "Entra pouco, sai linguiça."

## Princípios de fundo

- **Conhecimento tácito é o ouro.** O que você sabe fazer mas custa verbalizar é exatamente o método transferível — "a dor é o sinal de que há ouro".
- **Curva J, não U.** Terceirizar a cognição (YOLO, "deixa rodar enquanto durmo") → perda cognitiva. Usar como parceiro de pesquisa → ganho exponencial. "Não tem almoço grátis."
- **Wu-wei / Michelangelo.** Engenharia de prompt é *subtração*: tire o excesso até a obra aparecer; exponha o vazio para a atividade do modelo acontecer.
- **Intenção não se terceiriza.** A IA tem "intenção delegada": executa, nunca pretende. A orquestração é sempre humana.

## Para quem comunica/vende isso

- Público que paga é **B2B** (tem verba); áreas sensíveis (direito, medicina, finanças) é onde o uso raso "ferra a carreira".
- **Simplificar ≠ resumir** — simplificar abre acesso sem degradar o ativo profundo.
- Achar um **tradutor** (quem verta a profundidade para a linguagem do público); usar credencial (ex.: cadeira no MBA) para abrir portas corporativas.

---

## Insight do Arquiteto — o método virando template reutilizável

A própria palestra **é** um Framework Injection. Abaixo, o esqueleto que destila o método de Renato num molde aplicável a qualquer pedido sério à IA — junta densidade + 5 modalidades + eixo priming/enforcement + verificação externa:

```
[PAPEL — denso]        Você é um <termo denso da área> especializado em <recorte>.
[CONTEXTO]             Fundo não-acionável: domínio, restrições reais, "porquê".
[MÉTODO — procedim.]   Raciocine assim, passo a passo: 1)… 2)… 3)…
[FONTES — declarat.]   Hierarquia: <fonte primária> > <secundária>. Ontologia: <fundamentos>.
[JULGAMENTO — avaliat.] Critérios de qualidade: <rubrica>. Compare/classifique por <métrica>.
[LIMITES — ético/enf.]  NUNCA <X>. Recuse <Y>. (enforcement, não sugestão)
[OUTPUT]               Formato exato da entrega (definido ANTES — "planta da casa").
[VERIFICAÇÃO — assert] Checagem externa que pode FALHAR:
                       ex.: grep -q "<padrão>" saida.md  &&  grep -q "<padrão2>" saida.md
[CODA densa]           Reancore o termo denso central no fim (combate lost-in-the-middle).
```

**Como aplicar em 30s:** identifique o termo mais denso do seu pedido (movimento 1) → diga *como você faria* (movimento 2) → defina o formato de saída no início → feche com **um teste externo que possa falhar** (movimento 4). Se não há teste externo, você ainda está em "pedir digital".

> Nota: o repertório de skills já existe nesta máquina e operacionaliza isto — `fi-forja` (gera FI), `ds-meter` (mede densidade), `fi-enforce` (cria os asserts que faltam), `fi-tempera` (ataca p/ fortalecer). O tripé da aula: **gerar · medir · atravessar**.
