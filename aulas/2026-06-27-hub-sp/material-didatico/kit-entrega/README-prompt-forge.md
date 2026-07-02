# Prompt-Forge — README de 1 página (distribuição aluno)

> **O que é:** não é um gerador de prompts. É um **injetor de método de raciocínio** — transmuta texto cru num **Framework Injection** denso (priming) com cláusula de verificação (enforcement). Autor: Renato Aparecido Gomes · Licença MIT.

## A ideia em uma frase
Você dá um **carry** (sua intenção crua, texto ou áudio). Ele devolve um **FI**: papel + método + restrições + `[VERIFICAÇÃO]`. O cru induz pouco; o FI dispõe o método e marca o que obriga.

---

## ⚠️ O que você precisa saber ANTES (leia — evita o erro nº1 do workshop)

O Prompt-Forge é um **destilador** — ele não tem um modelo dentro dele. Ele **chama um modelo de fora** para fazer a forja. Por isso você precisa apontar para um endpoint de LLM. Dois caminhos, escolha um:

- **Caminho A — sua própria chave OpenRouter (recomendado para a aula).** Funciona em qualquer máquina, sem depender de nenhuma infra do facilitador. É o caminho default deste README.
- **Caminho B — Colab no navegador** (se sua máquina não roda Python). Ver `colab-fallback.ipynb` — mesmo princípio, tudo no browser.

> **Por que isto importa (honestidade):** a versão interna do autor aponta para um gateway local (`localhost:8001`). **Esse endereço NÃO existe na sua máquina.** Se você rodar sem configurar a env abaixo, dá erro de conexão. Os 3 `export` abaixo resolvem — é o passo que todo mundo esquece.

---

## Instalação (1 minuto)
```bash
# requer Python 3.9+
# copie a pasta prompt-forge/ que o facilitador distribuiu (ou git clone <repo>)
cd prompt-forge
pip install pyyaml rich            # opcionais (yaml + saída bonita); o núcleo roda sem eles
```

## Configuração do endpoint (o passo que destrava tudo)
```bash
# 1. Crie uma chave grátis em https://openrouter.ai/keys  (tem crédito de teste)
# 2. Aponte o Prompt-Forge para a OpenRouter pública e cole sua chave:
export FORGE_LLM_URL='https://openrouter.ai/api/v1'
export OPENROUTER_API_KEY='sk-or-...'                       # <- sua chave, entre aspas simples
export FORGE_MODEL='anthropic/claude-sonnet-4.6'           # forjador forte (recomendado)
export FORGE_FALLBACK_MODEL='anthropic/claude-sonnet-4.5'  # rota de reserva (id válido OpenRouter)
export FORGE_MAX_TOKENS='4000'                             # ESSENCIAL: o default (1300) trunca o FI
```
> **⚠️ Os 4 exports são testados (G4, 26-jun) — não improvise os ids.** Pontos que derrubam quem improvisa: (1) `anthropic/claude-3.5-sonnet` **não existe** no OpenRouter (dá HTTP 404) — use os ids acima, que estão na lista oficial; (2) sem `FORGE_MAX_TOKENS=4000`, o Claude é mais verboso que o default e o JSON do FI **trunca** (erro de parse); (3) **sempre rode com `--no-daemon`** (ver abaixo) — o daemon quente ignora suas envs e tenta a infra do autor.
> **Dica de forja (vem da pesquisa):** *quem forja importa tanto quanto o método.* Forja por modelo frontier rende ~88%; por modelo médio, ~6%. Na aula, use um modelo forte no `FORGE_MODEL` — você vê o teto do que o FI faz. Em casa, com modelo médio, o FI ainda vence o prompt cru, mas o ganho é menor — e é aí que a densidade semiótica mais compensa.

## Teste de fumaça (faça ANTES da aula — é a sua "lista de presença")
```bash
python3 fi --no-daemon "faça uma análise de risco de crédito da empresa X"
```
Saiu um FI com `[PAPEL] [MÉTODO] [VERIFICAÇÃO]` e o stderr mostrou `model=anthropic/claude-sonnet-4.6`? Pronto. Erro de conexão / 404 / erro de parse? Revise os 4 `export` acima — é sempre a env (id de modelo, `FORGE_MAX_TOKENS`, ou env não setada na mesma janela).

## Uso
```bash
# básico — texto cru → FI (stdout = só o artefato; SEMPRE --no-daemon no seu setup)
python3 fi --no-daemon "Seu texto aqui"

# ou por pipe
echo "seu texto" | python3 fi --no-daemon

# escolher o modelo forjador na hora
python3 fi --no-daemon --model 'anthropic/claude-opus-4.8' "..."

# registro bruto (JSON) com a proveniência da forja
python3 fi --no-daemon --json "..."

# versão legível para humano
python3 fi --no-daemon --human "..."
```
> **Por que `--no-daemon` sempre:** o Prompt-Forge mantém um daemon "quente" para velocidade. Mas o daemon foi iniciado com a config interna do autor e **ignora as suas envs** — ele tentaria a infra local (`localhost`) que você não tem. O `--no-daemon` força o caminho in-process que lê os seus `export`. *(O launcher chama-se `fi`, não `promptforge.py`. Se reclamar de permissão: `chmod +x fi && ./fi --no-daemon "..."`.)*

---

## O ciclo completo (o que você leva da aula)
```
texto cru  ──Prompt-Forge──►  FI denso  ──/forja──►  FI temperado
 (induz pouco)              (priming forte)        (enforcement endurecido)
```
1. **Prompt-Forge** gera o FI denso (o priming).
2. **`/forja`** tempera com martelo adversarial (endurece o enforcement linguístico).
3. O FI temperado é o que você usa no dia a dia — leva no bolso.

> **Sobre `/forja`:** a têmpera roda dentro de um ambiente de agente (Claude Code/CLI) com as skills instaladas. Sem esse ambiente, **simule a têmpera manualmente**: pegue cada `[VERIFICAÇÃO]` e pergunte *"este ASSERT roda de verdade? o que ele reprova?"*. Se não reprova nada, é priming disfarçado de enforcement.

## A régua de bolso (como ler o seu próprio FI)
Para cada cláusula que o Forge gerar, pergunte:
> **"isto induz ou constrange? E qual dos dois deveria?"**
- `[META-RACIOCÍNIO]`, `[PAPEL]`, `[MÉTODO]` → **induzem** (priming).
- `[VERIFICAÇÃO]` com ASSERT executável → **constrange** (enforcement) — só vale se dispara um teste real.
- Uma cláusula que induz onde deveria constranger = **dívida**. A maturidade do seu FI = quantas âncoras críticas escalaram de induzir para obrigar.
- A **largura da ponte** (`bridge_width`) do seu FI = asserts ÷ (asserts + checagens). Quanto dele *obriga* vs só *sugere*.

## Onde aprofundar
- Conceito canônico Priming/Enforcement (método Feynman) — pasta da Aula FI.
- `fi_system_prompt.md` (dentro da pasta `prompt-forge/`) — o injetor por dentro.
