# 🛠️ Kit do Aluno — Framework Injection

Bem-vindo. Este kit tem tudo que você precisa para forjar os seus próprios
Framework Injections depois da aula. Comece por aqui.

---

## O que tem neste kit

```
KIT-ALUNO/
├── COMECE-AQUI.md          ← você está aqui
├── skills/                 ← as 4 skills (o fluxo da forja)
│   ├── fi-forja/           gera o FI canônico
│   ├── ds-meter/           mede a densidade semiótica (e explica)
│   ├── fi-enforce/         transforma "sugestão" em "obrigação"
│   ├── fi-tempera/         ataca e fortalece o FI (forjar→martelar→recozer→resfriar)
│   └── README.md           como as skills se encadeiam
├── referencia/             ← a teoria, para consultar
│   ├── glossario-FI-completo.md       os 7 instrumentos + conceitos (Definição→Feynman→Exemplo)
│   ├── como-classificar-priming-enforcement.md  o critério sem achismo
│   ├── GABARITO-lakatos-modalidades.md   onde cada modalidade mora (núcleo/cinturão/borda)
│   ├── CATRACA-sem-codigo.md             enforcement sem terminal (schema, duplo-agente)
│   ├── TESTE-densificacao.md             o termo é denso p/ o MODELO ou só p/ você?
│   ├── CONCEITO — Priming e Enforcement (método Feynman).md
│   └── CONCEITO — Artesanato Digital (ofício e princípio).md
├── backend-opcional/       ← só se você usa Python (não é obrigatório)
│   ├── LEIA-backend.md     por que as skills são a versão atual
│   ├── promptforge.py      o motor que dá o número exato
│   ├── requirements.txt
│   └── colab-fallback.ipynb  rode no navegador, sem instalar nada
└── materiais/              ← apoio
    ├── cartao-do-aluno.html        cola de bolso (abra no navegador)
    ├── capsulas-reforco-texto.md   os reforços D+1/D+3/D+7
    ├── exemplo-fluxo-completo.md   as 4 skills rodando no mesmo caso
    ├── exemplo-caso-trilho.md      um FI completo de exemplo
    └── exemplos-fi-extra.md        mais FIs prontos (financeiro, pesquisa)
```

---

## Instalação das skills (2 minutos, sem Python)

As 3 skills funcionam **só com o seu Claude** — zero instalação técnica.

1. Localize a pasta de skills do seu Claude:
   - **Claude Code (terminal):** `~/.claude/skills/`
2. Copie as 3 pastas de `skills/` (fi-forja, ds-meter, fi-enforce) para lá.
3. Pronto. Digite `/fi-forja` no Claude para testar.

> Não tem Claude Code? As skills são arquivos de texto (`SKILL.md`) — você pode
> colar o conteúdo de cada uma direto na conversa do Claude como instrução. O
> método é o mesmo.

---

## O fluxo da aula (use as 4 em sequência)

```
1.  /fi-forja "seu pedido cru aqui"
    → nasce o seu Framework Injection canônico (8 seções)

2.  /ds-meter "seu pedido cru"  e depois no FI gerado
    → veja a densidade subir — e entenda POR QUÊ

3.  /fi-enforce  (cole o FI gerado)
    → descubra o que só SUGERE vs o que OBRIGA, e crie os critérios que faltam

4.  /fi-tempera  (cole o FI)
    → ataque a própria obra e fortaleça-a. Output não-temperado é rascunho.
```

São independentes (cada uma roda sozinha) mas se encadeiam. O seu projeto é
forjar **o seu FI**, passando pelas quatro. Veja o exemplo completo em
`materiais/exemplo-fluxo-completo.md`.

---

## As 3 micro-ações de reforço (não deixe a aula evaporar)

Em `materiais/capsulas-reforco-texto.md` você recebe, espaçadas no tempo:
- **D+1** — transforme 1 sugestão em obrigação (um assert que reprova)
- **D+3** — densifique 1 termo do seu domínio
- **D+7** — forje um FI novo e mostre a alguém (o teste de transferência)

---

## O essencial em uma frase

**Pare de comandar a IA. Comece a educá-la.** Um FI não é um prompt melhor — é o
seu método de raciocínio, transferido para a máquina.

---
*Academia Lendária / Hub SP · Aula Framework Injection · Renato Aparecido Gomes*
