# KIT DO FACILITADOR — Aula Framework Injection (Academia Lendária / Hub SP)

> Documento operável, separado do corpo-mestre. O corpo-mestre é o *porquê*; este kit é o *como rodar*. Quem dá a aula usa ISTO.

---

## ⏱️ SCRIPT MINUTO-A-MINUTO

### PAINEL (60min)
| Min | Faça | Slide/recurso |
|---|---|---|
| 0–10 | Gancho do pidgin digital. Pergunta: "quem aqui acha que já sabe dar prompt?" | analogia do porto |
| 10–22 | As 3 eras no quadro (receita→cozinha→ensino) + exemplo do analista de risco | tabela PE⊂CE⊂FI |
| 22–38 | Mapa das 4 engenharias + tabela priming vs enforcement + analogia técnico/bandeirinha | desenho do mapa |
| 38–50 | **DEMO A/B AO VIVO** — pegar tarefa da plateia, rodar Prompt-Forge, mostrar DS subir + benchmark n=49 + o que FALHOU | terminal + slide dos 4 braços |
| 50–60 | FAQ (as 6 perguntas) + tarefa de casa | cartão de respostas |

### WORKSHOP (90min)
| Min | Faça | Pilar |
|---|---|---|
| 0–10 | Setup + regra do jogo | — |
| 10–22 | Poda sintática no prompt de cada um | 1. Syntactic Pruning |
| 22–48 | Prompt-Forge ao vivo: cada aluno gera seu FI de 8 seções | 2-3. SDE + CodePrompt |
| 48–70 | `/forja` em cada FI (forjar→martelar→recozer→resfriar) | Têmpera (enforcement) |
| 70–85 | Definir [OUTPUT] + (se código) DS-d + [META-RACIOCÍNIO] | 5-6. Delivery Arch + Agent First + MetaBlock |
| 85–90 | Showcase 1-2-4-All + "Antes/Agora penso" | — |

---

## 🎯 AS 6 PERGUNTAS DIFÍCEIS — respostas decoradas

1. **"Isso não é só um system prompt grande?"** → "Volume é tamanho; FI é estrutura. No benchmark, FI longo+raso (1180 chars) perdeu pra FI curto+denso. É densidade acionável, não comprimento."
2. **"Difere de DSPy / context engineering?"** → "DSPy otimiza a mecânica do pipeline; CE gerencia o que o modelo vê; FI determina como ele pensa. Biblioteca vs metodologia de pesquisa."
3. **"Por que a IA não cria o próprio framework?"** → "Paradoxo do Artesão: criar framework exige conhecimento tácito (Polanyi). O framework É a externalização do tácito; a IA opera dentro mas não gera a externalização."
4. **"Qual a base teórica?"** → "6 tradições: Vygotsky, Sweller, Wittgenstein, Polanyi, Peirce, Greenberg. 4 DOIs no Zenodo."
5. **"Funciona em qualquer modelo?"** → "Honestamente: portabilidade cross-modelo não validada. E densidade é condicional à força do modelo. Método robusto, dose model-dependent."
6. **"Escala ou é artesanato de um cara só?"** → "Barreira alta (6/10 acessibilidade, eu admito). Por isso existe o Prompt-Forge: destila o artesanato em ferramenta. O workshop é isso."

### 3 perguntas de pânico (operacionais)
- **"O Prompt-Forge deu erro"** → "Usa o link Colab de fallback (modo CLI puro, sem instalar nada). Link no chat."
- **"Não trouxe prompt"** → "Pega um do banco de emergência (Anexo I do corpo). Escolhe o do teu domínio."
- **"Isso é hype de IA?"** → "Trago os dados que FALHARAM, não só os que funcionaram. Ciência, não folheto. (mostra a tabela H3-média)."

---

## ✅ CHECKLIST DE PRONTIDÃO (bloqueante — sem isto, NÃO rodar)

- [ ] **Dry-run completo feito** — rodei a aula inteira sozinho, incluindo Prompt-Forge + `/forja` na minha pele.
- [ ] **Vídeo de tom** do autor (abertura + demo A/B) assistido.
- [ ] **Vídeo de 90s da demo A/B** gravado (fallback se a rede cair).
- [ ] **Link Colab do Prompt-Forge** hospedado e testado (modo offline/CLI).
- [ ] **Slide do benchmark n=49** (4 braços: A=2%, B=0%, C=8%, D=88%) pronto.
- [ ] **Slide do que FALHOU** (H3 média + Adaptive H0) pronto — é a credibilidade.
- [ ] **Pré-distribuição 48h** enviada (pacote + selftest + 1 prompt real pedido).
- [ ] **Wi-Fi da sala** testado com carga real (vários acessos ao Prompt-Forge/web).
- [ ] **3 cápsulas de reforço** (D+1/D+3/D+7) pré-gravadas e agendadas.

---

## 🗺️ DOIS MODOS DE RODAR

| | **MVP replicável** (qualquer facilitador treinado) | **Edição completa** (autor / facilitador que dominou o paper) |
|---|---|---|
| Painel | gancho pidgin + 3 eras + 1 demo A/B + FAQ básico | + Bloco 3 (ponte H3 priming↔enforcement) + dados que falharam |
| Workshop | poda + Prompt-Forge + ler o DS | + têmpera adversarial completa + bridge_width + Agent First DS-d |
| Risco | baixo (escala) | alto (depende de domínio profundo) |

---

## ⚠️ PENDÊNCIAS ANTES DA PRIMEIRA TURMA (do red-team/pre-mortem)
1. Gravar vídeo de 90s da demo A/B (fallback).
2. Hospedar Colab de fallback do Prompt-Forge (modo CLI puro).
3. Confirmar versão do Prompt-Forge distribuída = engine v2 (`~/.aiox/tools/prompt-forge`).
4. Preparar slides do benchmark (4 braços) e do "o que falhou" (H3 média).
5. Gravar as 3 cápsulas de reforço.

---

**Gerado por:** aula-forge v1.0 | **Fonte:** corpo-mestre `AULA — Framework Injection (Painel + Workshop).md`
