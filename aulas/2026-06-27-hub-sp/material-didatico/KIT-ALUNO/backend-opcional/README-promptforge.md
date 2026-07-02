# PromptForge — Reasoning Framework Injection

> **Não gere prompts. Injete raciocínio.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

PromptForge é o primeiro pipeline de **Reasoning Framework Injection (RFI)** — a disciplina de transferir frameworks cognitivos completos para modelos de linguagem, transformando-os de geradores de texto em operadores de método.

**Não é prompt engineering.** Prompt engineering ajusta o que o modelo faz. RFI transforma como o modelo pensa.

---

## O Problema

O mercado de IA trabalha em três camadas:

```
CAMADA 3 — INFRAESTRUTURA     → LangChain, DSPy, CrewAI
CAMADA 2 — GESTÃO DE PROMPTS  → PromptHub, Braintrust, Vellum
CAMADA 1 — TEMPLATES          → PromptBase, AIPRM, God of Prompt
CAMADA 0 — ??? (VAZIA)        → Transferência de framework cognitivo
```

**Nenhum player opera na Camada 0.** O mercado inteiro trabalha na superfície sem tocar no que realmente importa: **o framework de raciocínio do modelo**.

---

## A Solução

PromptForge injeta **frameworks cognitivos de domínio** diretamente no raciocínio do LLM:

```
# Prompt convencional:
"Analise este contrato e identifique riscos jurídicos"
→ Output genérico, alucina, superficial

# Reasoning Framework Injection:
Produza o parecer jurídico estratégico e a análise de risco legal sobre: [caso]

hermeneutica_aplicada:
  controle_constitucionalidade: analise_difusa_e_concentrada
  jurisprudencia_dominante: stj_teses_repetitivas_e_stf_repercussao_geral
mitigacao_risco:
  responsabilidade_civil: distinguir_objetiva_de_subjetiva
  excludentes_nexo_causal: avaliar_forca_probatoria_bayesiana

Antes de concluir, explicite o precedente jurisprudencial mais frágil
e calibre seu grau de confiança na segurança jurídica da tese.

Produza o parecer jurídico estratégico e fundamentado.
```

O segundo **não é um prompt melhor**. É a injeção de um framework jurídico completo — hermenêutica, teses repetitivas, análise bayesiana, stress-test metacognitivo.

---

## Como Funciona

Pipeline de 5 etapas:

```
Carry (texto/voz)
  → 1. Syntactic Pruning (limpeza de fillers, hesitações)
  → 2. Classificação (domínio + tipo de FI)
  → 3. Semiotic Density Engineering (SDE)
  → 4. Framework Injection (FI-Máquina + FI-Humano)
  → 5. Cálculo de DS (Semiotic Density)
```

### Métrica: Semiotic Density (DS)

| DS | Nível | Descrição |
|----|-------|-----------|
| 1.0–1.5 | Pidgin | Termos genéricos, sem frame de domínio |
| 1.5–2.5 | Informal | Alguns termos de domínio, estrutura fraca |
| 2.5–3.5 | Competente | Frame reconhecível, falta profundidade |
| 3.5–4.5 | Funcional | Domínio ativado, método presente, constraints claras |
| 4.5–5.0 | Expert | Raciocínio de domínio transferido, metacognição projetada |

**Benchmark interno:** DS +117% em carry real, +161% em carries vagos.

---

## Instalação

```bash
# Clone
git clone https://github.com/renatoapgomes/promptforge.git
cd promptforge

# Instalar dependências
pip install -r requirements.txt

# Uso direto
python promptforge.py "Analise este contrato e identifique riscos jurídicos"
```

---

## Uso

### Básico
```bash
python promptforge.py "Seu texto aqui"
```

### Com domínio específico
```bash
python promptforge.py --domain juridico "Parecer sobre cláusula de não-concorrência"
python promptforge.py --domain business "Estratégia de go-to-market para SaaS"
python promptforge.py --domain engenharia "Arquitetura de sistema distribuído"
```

### Com áudio (voice mode)
```bash
python promptforge.py --audio recording.mp3
```

### Output formatos
```bash
python promptforge.py --format yaml "..."      # FI-Máquina (YAML)
python promptforge.py --format human "..."      # FI-Humano (render)
python promptforge.py --format both "..."       # Ambos (default)
```

### Modo verboso
```bash
python promptforge.py --verbose "..."           # Mostra pipeline completo
```

---

## Domínios Suportados

| Domínio | Framework | Exemplo |
|---------|-----------|---------|
| **Jurídico** | Hermenêutica constitucional + teses STJ/STF + análise bayesiana | `examples/juridico.md` |
| **Business** | Diagnóstico competitivo + GTM + unit economics + Bullseye | `examples/business.md` |
| **Engenharia** | Teorema CAP + circuit breaker + sharding + cache policies | `examples/engenharia.md` |
| **Pesquisa** | Validade epistemológica + falseabilidade + carga cognitiva | `examples/pesquisa.md` |
| **Marketing** | Persuasão cognitiva + heurística + jornada Schwartz | `examples/marketing.md` |
| **Médico** | Diagnóstico diferencial + etiopatogenia + probabilidade bayesiana | `examples/medico.md` |

---

## Anatomia do Framework Injection

Cada FI segue a **Curva-U** em 4 posições:

```
POSIÇÃO 1 (Primacy): Instruction-First + Âncora de Domínio
         ↓
POSIÇÃO 2–N-2 (Miolo): CodePrompt REAL em YAML + SDE
         ↓
POSIÇÃO N-1 (Penúltima): MetaBlock REAL (auto-supervisão)
         ↓
POSIÇÃO N (Recency): Coda Densa (re-ancoragem)
```

### Dual Legibilidade

Cada FI gera dois artefatos:

1. **FI-Máquina** — O que vai para o LLM. YAML puro, sem andaimes visuais.
2. **FI-Humano** — Projeção pedagógica para auditoria. Render do FI-Máquina.

---

## Diferencial Competitivo

| Aspecto | Prompt Engineering | Reasoning Framework Injection |
|---------|-------------------|-------------------------------|
| O que faz | Ajusta instruções | Injeta frameworks cognitivos |
| Output | Prompt melhor | Método de raciocínio transferido |
| Métrica | Subjetiva | Semiotic Density (DS) |
| Domínio | Genérico | 6 domínios especializados |
| Verificação | Manual | MetaBlock (auto-supervisão) |
| Alucinação | Não endereça | Reduzida via framework estruturado |

---

## Papers Publicados

| Paper | DOI | Domínio |
|-------|-----|---------|
| Semiotic Density | [10.5281/zenodo.19645955](https://doi.org/10.5281/zenodo.19645955) | Teoria |
| Framework Injection | [10.5281/zenodo.19344789](https://doi.org/10.5281/zenodo.19344789) | Método |
| Delivery Architecture | [10.5281/zenodo.19939303](https://doi.org/10.5281/zenodo.19939303) | Arquitetura |
| A²RAG (STEER) | [10.5281/zenodo.19645965](https://doi.org/10.5281/zenodo.19645965) | Pesquisa |
| Adaptive FI | [10.5281/zenodo.20040726](https://doi.org/10.5281/zenodo.20040726) | Evolução |

---

## Roadmap

- [x] Pipeline 5 etapas funcional
- [x] 6 domínios canônicos
- [x] Métrica DS implementada
- [x] Voice detection (PT-BR)
- [x] Dual Legibilidade (FI-Máquina + FI-Humano)
- [ ] CLI tool completa com argparse
- [ ] Integração com LangChain/DSPy
- [ ] Marketplace de frameworks de domínio
- [ ] Certificação FI Master
- [ ] Paper DS peer-reviewed (arXiv)

---

## Contribuição

Contribuições são bem-vindas! Veja [CONTRIBUTING.md](CONTRIBUTING.md) para diretrizes.

### Como contribuir:
1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/novo-dominio`)
3. Commit suas mudanças (`git commit -m 'Adiciona domínio medicina'`)
4. Push para a branch (`git push origin feature/novo-dominio`)
5. Abra um Pull Request

### Áreas de contribuição:
- Novos domínios (educação, finanças, ciência, etc.)
- Melhorias no pipeline SDE
- Integrações com outros frameworks
- Testes e benchmarks
- Documentação

---

## Licença

Apache License 2.0 — veja [LICENSE](LICENSE)

---

## Autor

**Renato Aparecido Gomes**
- Sócio-fundador AGAC (advocaciagac.com.br)
- Criador do Framework Injection (Cognitive Metaprogramming)
- 9 DOIs publicados (Zenodo/arXiv)
- ORCID: [0009-0005-7380-9876](https://orcid.org/0009-0005-7380-9876)

---

## Contato

- **GitHub:** [github.com/renatoapgomes](https://github.com/renatoapgomes)
- **LinkedIn:** [linkedin.com/in/renatoapgomes](https://linkedin.com/in/renatoapgomes)
- **Email:** renatoapgomes@gmail.com

---

> **"Não gere prompts. Injete raciocínio."**

---

## Agradecimentos

- Bruno Okamoto (Nous Research) — Metodologia de agentes
- Fábio Akita — Método de desenvolvimento
- Comunidade open-source — Inspiração e suporte
