#!/usr/bin/env python3
"""
PromptForge — Reasoning Framework Injection Pipeline

Transforma carries (texto ou áudio) em Framework Injections completos.
Não é um gerador de prompts. É um injetor de método de raciocínio.

Uso:
    python promptforge.py "Seu texto aqui"
    python promptforge.py --domain juridico "Parecer sobre contrato"
    python promptforge.py --audio recording.mp3
    python promptforge.py --format yaml "..."
    python promptforge.py --verbose "..."

Autor: Renato Aparecido Gomes
Licença: MIT
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

# Try optional imports
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text
    HAS_RICH = True
except ImportError:
    HAS_RICH = False


# ============================================================================
# CONSTANTS
# ============================================================================

VERSION = "1.0.0"

FILLERS_PT_BR = [
    "enfim", "tipo", "né", "então", "assim", "sabe", "tá", "hm", "hmm",
    "ah", "eh", "ué", "bom", "é que", "como assim", "meio que", "tipo assim",
    "fazer uma coisa que", "de alguma forma", "basicamente",
]

DOMAINS = {
    "juridico": {
        "keywords": ["lei", "artigo", "contrato", "processo", "OAB", "LGPD",
                     "compliance", "direito", "penal", "civil", "parecer",
                     "jurisprudência", "tribunal", "advogado", "advocacia"],
        "name": "Jurídico",
        "template": "juridico",
    },
    "business": {
        "keywords": ["estratégia", "mercado", "competidor", "startup", "GTM",
                     "receita", "lucro", "cliente", "produto", "negócio",
                     "empresa", "marketing", "vendas", "pitch", "investimento"],
        "name": "Business",
        "template": "business",
    },
    "engenharia": {
        "keywords": ["sistema", "arquitetura", "API", "banco de dados", "deploy",
                     "infraestrutura", "microserviço", "escala", "performance",
                     "backend", "frontend", "docker", "kubernetes", "cloud"],
        "name": "Engenharia",
        "template": "engenharia",
    },
    "pesquisa": {
        "keywords": ["paper", "hipótese", "experimento", "metodologia", "revisão",
                     "benchmark", "valida", "falsifica", "evidência", "estudo",
                     "análise", "dados", "método", "resultado", "publicação"],
        "name": "Pesquisa",
        "template": "pesquisa",
    },
    "marketing": {
        "keywords": ["marca", "campanha", "público", "conteúdo", "copy",
                     "posicionamento", "branding", "redes sociais", "anúncio",
                     "conversão", "funil", "lead", "engajamento", "viral"],
        "name": "Marketing",
        "template": "marketing",
    },
    "medico": {
        "keywords": ["paciente", "diagnóstico", "sintoma", "tratamento", "clínico",
                     "exame", "doença", "patologia", "terapia", "prescrição",
                     "médico", "hospital", "saúde", "cirurgia", "medicamento"],
        "name": "Médico",
        "template": "medico",
    },
}

FI_TEMPLATES = {
    "juridico": {
        "instruction": "Produza o parecer jurídico estratégico e a análise de risco legal sobre:",
        "codeprompt": """hermeneutica_aplicada:
  controle_constitucionalidade: analise_difusa_e_concentrada
  jurisprudencia_dominante: stj_teses_repetitivas_e_stf_repercussao_geral
mitigacao_risco:
  responsabilidade_civil: distinguir_objetiva_de_subjetiva
  excludentes_nexo_causal: avaliar_forca_probatoria_bayesiana""",
        "metablock": "Antes de concluir, explicite o precedente jurisprudencial mais frágil utilizado na fundamentação e calibre seu grau de confiança na segurança jurídica da tese.",
        "coda": "Produza o parecer jurídico estratégico e fundamentado.",
    },
    "business": {
        "instruction": "Formule o diagnóstico competitivo e a estratégia de go-to-market (GTM) para:",
        "codeprompt": """vantagem_competitiva:
  barreiras_de_entrada: mapeamento_de_fosso_economico_moat
  elasticidade_demanda: matriz_sensibilidade_preco_cruzada
alocacao_recursos:
  unit_economics: otimizacao_cac_vs_ltv_e_payback
  canais_tracao: aplicacao_framework_bullseye""",
        "metablock": "Antes de consolidar a estratégia, aponte a hipótese de mercado assumida com o maior risco de invalidação empírica e proponha um teste de validação de baixo custo.",
        "coda": "Formule o diagnóstico competitivo e a estratégia de go-to-market.",
    },
    "engenharia": {
        "instruction": "Arquitete a topologia de sistema resiliente e distribuído para:",
        "codeprompt": """resiliencia_distribuida:
  tolerancia_a_particao: avaliacao_tradeoffs_teorema_cap
  circuit_breaker: politicas_de_fallback_e_degradacao_graciosa
escalabilidade_horizontal:
  sharding_estrategia: aplicacao_hashing_consistente
  gargalos_io: definicao_cache_invalidation_policies""",
        "metablock": "Antes de definir a arquitetura, isole o Single Point of Failure (SPOF) mais provável na infraestrutura e calibre a complexidade acidental que esta solução introduz.",
        "coda": "Arquitete a topologia de sistema resiliente e documentada.",
    },
    "pesquisa": {
        "instruction": "Estruture o desenho metodológico e a transposição didática para:",
        "codeprompt": """validade_epistemologica:
  controle_de_vieses: isolamento_de_variaveis_de_confusao
  potencial_falseabilidade: submissao_a_criterios_popperianos
transposicao_didatica:
  carga_cognitiva: minimizacao_segundo_teoria_sweller
  ancoragem_conceitual: formacao_de_subsuncores_ausubelianos""",
        "metablock": "Antes de fechar o modelo educacional, identifique o viés de confirmação latente no material e aponte qual bloco conceitual tem o maior risco de gerar dissonância cognitiva no aluno.",
        "coda": "Estruture o desenho metodológico e a transposição didática.",
    },
    "marketing": {
        "instruction": "Desenvolva a matriz de posicionamento de marca e a arquitetura de persuasão (copy) para:",
        "codeprompt": """persuasao_cognitiva:
  heuristica_disponibilidade: construcao_de_ancoragem_memoravel
  gatilhos_de_escassez: aplicacao_autentica_de_aversao_a_perda
arquitetura_mensagem:
  jornada_consciencia: niveis_de_consciencia_de_schwartz
  proposicao_valor: destilacao_de_unique_value_proposition""",
        "metablock": "Antes de finalizar a matriz, avalie se a promessa principal soa hiperbólica ou clichê, e calibre o tom de voz para garantir que a percepção de autenticidade supere a percepção de venda.",
        "coda": "Desenvolva a matriz de posicionamento de marca e a arquitetura de persuasão.",
    },
    "medico": {
        "instruction": "Produza o diagnóstico diferencial de:",
        "codeprompt": """etiopatogenia_critica:
  analise_fisiologica: profunda
  sintomatologia_cruzada: avaliar_exclusao
patologia_diferencial:
  criterio_primario: probabilidade_bayesiana
  mitigacao_risco: descartar_emergencias_fatais""",
        "metablock": "Antes de concluir, calibre sua confiança clínica e explicite a suposição mais frágil adotada no raciocínio.",
        "coda": "Produza o diagnóstico diferencial fundamentado.",
    },
}

FI_TYPES = {
    "declarativo": "Conhecimento/hierarquia/ontologia",
    "procedimental": "Como fazer/step-by-step/metodologia",
    "avaliativo": "Julgar/rubricas/critérios de qualidade",
    "etico": "Limites/compliance/o que recusar",
    "composicional": "Combinação dos anteriores",
}


# ============================================================================
# DATA CLASSES
# ============================================================================

class OutputFormat(Enum):
    YAML = "yaml"
    HUMAN = "human"
    BOTH = "both"


@dataclass
class PipelineResult:
    """Resultado completo do pipeline PromptForge."""
    original_text: str
    cleaned_text: str
    voice_detected: bool
    domain: str
    fi_type: str
    ds_original: float
    ds_fi: float
    ds_improvement: float
    fi_machine: str
    fi_human: str
    densifications: list = field(default_factory=list)


# ============================================================================
# PIPELINE STAGES
# ============================================================================

def detect_voice(text: str) -> bool:
    """Detecta se o texto é transcrição de voz."""
    filler_count = sum(1 for f in FILLERS_PT_BR if f.lower() in text.lower())
    has_long_sentences = any(len(s.split()) > 40 for s in text.split('.'))
    has_no_punctuation = text.count('.') < len(text) / 100
    return filler_count >= 2 or (has_long_sentences and has_no_punctuation)


def syntactic_pruning(text: str, voice_detected: bool) -> tuple[str, list]:
    """Etapa 1: Limpa o texto de fillers e hesitações."""
    cleaned = text
    removed = []

    # Remove fillers
    for filler in FILLERS_PT_BR:
        pattern = rf'\b{re.escape(filler)}\b'
        if re.search(pattern, cleaned, re.IGNORECASE):
            removed.append(filler)
            cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)

    # Remove reticências repetidas
    cleaned = re.sub(r'\.{3,}', '...', cleaned)

    # Remove espaços múltiplos
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    # Remove falsos começos comuns
    false_starts = [
        r'^(bom,?|então,?|assim,?|tipo,?|enfim,?)\s*',
        r'^(eu queria|eu quero|preciso que|gostaria que)\s*',
    ]
    for pattern in false_starts:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)

    return cleaned, removed


def classify_domain(text: str) -> tuple[str, str]:
    """Etapa 2: Classifica domínio e tipo de FI."""
    text_lower = text.lower()

    # Score each domain
    scores = {}
    for domain, config in DOMAINS.items():
        score = sum(1 for kw in config["keywords"] if kw in text_lower)
        scores[domain] = score

    # Best domain
    best_domain = max(scores, key=scores.get)
    if scores[best_domain] == 0:
        best_domain = "business"  # default

    # Classify FI type
    if any(w in text_lower for w in ["como", "passo", "processo", "método", "etapa"]):
        fi_type = "procedimental"
    elif any(w in text_lower for w in ["avalie", "compare", "julgue", "critério"]):
        fi_type = "avaliativo"
    elif any(w in text_lower for w in ["deve", "pode", "limite", "ético", "compliance"]):
        fi_type = "etico"
    elif any(w in text_lower for w in ["o que é", "conceito", "definição", "hierarquia"]):
        fi_type = "declarativo"
    else:
        fi_type = "composicional"

    return best_domain, fi_type


def sde_operations(text: str, domain: str) -> tuple[str, list]:
    """Etapa 3: Semiotic Density Engineering."""
    densifications = []

    # Densify: substituir termos genéricos por termos de domínio
    replacements = {
        "fazer": "implementar",
        "melhorar": "otimizar",
        "analisar": "dissecar",
        "verificar": "auditar",
        "problema": "disfunção",
        "solução": "intervenção",
        "resultado": "outcome",
        "processo": "pipeline",
        "sistema": "arquitetura",
        "dados": "dataset",
        "informação": "sinal",
        "erro": "desvio",
        "cliente": "stakeholder",
    }

    for old, new in replacements.items():
        if old in text.lower():
            text = re.sub(rf'\b{old}\b', new, text, flags=re.IGNORECASE)
            densifications.append(f"{old}→{new}")

    # Rarefy: remover termos vagos
    vague_terms = ["bom", "melhor", "ótimo", "eficiente", "eficaz"]
    for term in vague_terms:
        if term in text.lower():
            text = re.sub(rf'\b{term}\b', '', text, flags=re.IGNORECASE)
            densifications.append(f"removido: {term}")

    # Clean up
    text = re.sub(r'\s+', ' ', text).strip()

    return text, densifications


def calculate_ds(text: str) -> float:
    """Calcula Semiotic Density (DS) em escala 1.0-5.0."""
    words = text.split()
    if not words:
        return 1.0

    # Heuristic scoring
    score = 1.0

    # Domain-specific terms boost
    domain_terms = 0
    for domain_config in DOMAINS.values():
        domain_terms += sum(1 for kw in domain_config["keywords"] if kw in text.lower())
    score += min(domain_terms * 0.3, 1.5)

    # Technical terms boost
    technical_indicators = [
        "framework", "método", "análise", "diagnóstico", "estratégia",
        "arquitetura", "pipeline", "metodologia", "heurística", "bayesiana",
        "hermenêutica", "constitucionalidade", "falseabilidade", "epistemológica",
    ]
    tech_count = sum(1 for t in technical_indicators if t in text.lower())
    score += min(tech_count * 0.2, 1.0)

    # Structure indicators
    if ":" in text:
        score += 0.2
    if any(c in text for c in ["→", "↓", "•", "-"]):
        score += 0.2
    if re.search(r'\n\s+', text):
        score += 0.3

    # YAML indicators
    if re.search(r'\w+:', text):
        score += 0.3

    # Constraint indicators
    constraint_words = ["obrigatório", "nunca", "sempre", "antes de", "depois de"]
    constraint_count = sum(1 for c in constraint_words if c in text.lower())
    score += min(constraint_count * 0.15, 0.5)

    return min(round(score, 1), 5.0)


def generate_fi_machine(domain: str, user_input: str) -> str:
    """Etapa 4a: Gera o FI-Máquina."""
    template = FI_TEMPLATES.get(domain, FI_TEMPLATES["business"])

    fi = f"""{template['instruction']} {user_input}

{template['codeprompt']}

{template['metablock']}

{template['coda']}"""

    return fi


def generate_fi_human(domain: str, fi_type: str) -> str:
    """Etapa 4b: Gera o FI-Humano (render pedagógico)."""
    domain_name = DOMAINS[domain]["name"].upper()

    fi_human = f"""[FRAMEWORK INJECTION: {domain_name}]
[ABERTURA / PRIMACY] — Instruction-First: instrução de domínio + âncora
[CODEPROMPT / SP] — Estruturas de domínio codificadas em YAML
[SDE / DENSIDADE] — Radicais ativados via Semiotic Density Engineering
[METABLOCK / PENÚLTIMA POSIÇÃO] — Metacognição: auto-supervisão antes da conclusão
[CODA DENSA / RECENCY] — Re-ancoragem de domínio pura

Tipo de FI: {fi_type} ({FI_TYPES[fi_type]})"""

    return fi_human


# ============================================================================
# MAIN PIPELINE
# ============================================================================

def run_pipeline(text: str, domain: Optional[str] = None,
                 output_format: OutputFormat = OutputFormat.BOTH,
                 verbose: bool = False) -> PipelineResult:
    """Executa o pipeline completo do PromptForge."""

    # Stage 0: Original
    ds_original = calculate_ds(text)

    # Stage 1: Syntactic Pruning
    voice_detected = detect_voice(text)
    cleaned_text, removed_fillers = syntactic_pruning(text, voice_detected)

    # Stage 2: Classification
    if domain and domain in DOMAINS:
        detected_domain = domain
    else:
        detected_domain, fi_type = classify_domain(cleaned_text)
        if domain:
            detected_domain = domain  # override if specified

    detected_domain = detected_domain or "business"
    _, fi_type = classify_domain(cleaned_text)

    # Stage 3: SDE
    sde_text, densifications = sde_operations(cleaned_text, detected_domain)

    # Stage 4: Generate FI
    fi_machine = generate_fi_machine(detected_domain, sde_text)
    fi_human = generate_fi_human(detected_domain, fi_type)

    # Stage 5: Calculate DS
    ds_fi = calculate_ds(fi_machine)
    ds_improvement = ((ds_fi - ds_original) / ds_original * 100) if ds_original > 0 else 0

    return PipelineResult(
        original_text=text,
        cleaned_text=cleaned_text,
        voice_detected=voice_detected,
        domain=detected_domain,
        fi_type=fi_type,
        ds_original=ds_original,
        ds_fi=ds_fi,
        ds_improvement=ds_improvement,
        fi_machine=fi_machine,
        fi_human=fi_human,
        densifications=densifications,
    )


# ============================================================================
# OUTPUT FORMATTERS
# ============================================================================

def format_output(result: PipelineResult, output_format: OutputFormat,
                  verbose: bool = False) -> str:
    """Formata o output do pipeline."""

    if HAS_RICH:
        return format_output_rich(result, output_format, verbose)
    else:
        return format_output_plain(result, output_format, verbose)


def format_output_rich(result: PipelineResult, output_format: OutputFormat,
                       verbose: bool) -> str:
    """Formata output usando Rich."""
    console = Console(record=True, width=80)

    # Header
    console.print()
    console.print(Panel.fit(
        "[bold cyan]PROMPTFORGE[/bold cyan]\n"
        "[dim]Reasoning Framework Injection[/dim]",
        border_style="cyan"
    ))

    # Metadata
    domain_name = DOMAINS.get(result.domain, {}).get("name", result.domain)
    voice_tag = " [yellow]🎙 Voz detectada[/yellow]" if result.voice_detected else ""

    console.print(f"\n📍 Domínio: [bold]{domain_name}[/bold]   "
                  f"🧠 Tipo FI: [bold]{result.fi_type}[/bold]{voice_tag}")

    # DS metrics
    ds_color = "green" if result.ds_improvement > 0 else "red"
    console.print(f"📊 DS: [bold]{result.ds_original}[/bold] → "
                  f"[bold {ds_color}]{result.ds_fi}[/bold {ds_color}] "
                  f"([bold {ds_color}]+{result.ds_improvement:.0f}%[/bold {ds_color}] melhoria)")

    # Verbose: show pipeline stages
    if verbose:
        console.print("\n" + "=" * 60)
        console.print("[bold]PIPELINE DETALHADO[/bold]")
        console.print("=" * 60)

        console.print(f"\n[bold]1. SYNTACTIC PRUNING[/bold]")
        console.print(f"   Texto limpo: {result.cleaned_text[:100]}...")

        console.print(f"\n[bold]2. CLASSIFICAÇÃO[/bold]")
        console.print(f"   Domínio: {result.domain}")
        console.print(f"   Tipo FI: {result.fi_type}")

        console.print(f"\n[bold]3. SDE[/bold]")
        console.print(f"   Densificações: {', '.join(result.densifications) if result.densifications else 'nenhuma'}")

    # Output
    console.print("\n" + "─" * 60)

    if output_format in (OutputFormat.YAML, OutputFormat.BOTH):
        console.print("\n[bold green]─── FI-MÁQUINA ────────────────────────────[/bold green]")
        console.print(result.fi_machine)

    if output_format in (OutputFormat.HUMAN, OutputFormat.BOTH):
        console.print("\n[bold yellow]─── FI-HUMANO ─────────────────────────────[/bold yellow]")
        console.print(result.fi_human)

    # Densifications
    if result.densifications:
        console.print("\n" + "─" * 60)
        console.print(f"💡 Densificações: {', '.join(result.densifications)}")

    console.print("\n" + "═" * 60)
    console.print("[dim]Quer refinar? refinar: [instrução] | mais conciso | mais técnico | versão [domínio][/dim]")
    console.print()

    return console.export_text()


def format_output_plain(result: PipelineResult, output_format: OutputFormat,
                        verbose: bool) -> str:
    """Formata output em texto puro."""
    lines = []

    lines.append("")
    lines.append("=" * 60)
    lines.append("PROMPTFORGE")
    lines.append("Reasoning Framework Injection")
    lines.append("=" * 60)

    domain_name = DOMAINS.get(result.domain, {}).get("name", result.domain)
    voice_tag = " [🎙 Voz detectada]" if result.voice_detected else ""

    lines.append(f"\nDomínio: {domain_name}   Tipo FI: {result.fi_type}{voice_tag}")
    lines.append(f"DS: {result.ds_original} → {result.ds_fi} (+{result.ds_improvement:.0f}% melhoria)")

    if verbose:
        lines.append("\n" + "=" * 60)
        lines.append("PIPELINE DETALHADO")
        lines.append("=" * 60)
        lines.append(f"\n1. SYNTACTIC PRUNING")
        lines.append(f"   Texto limpo: {result.cleaned_text[:100]}...")
        lines.append(f"\n2. CLASSIFICAÇÃO")
        lines.append(f"   Domínio: {result.domain}")
        lines.append(f"   Tipo FI: {result.fi_type}")
        lines.append(f"\n3. SDE")
        lines.append(f"   Densificações: {', '.join(result.densifications) if result.densifications else 'nenhuma'}")

    lines.append("\n" + "─" * 60)

    if output_format in (OutputFormat.YAML, OutputFormat.BOTH):
        lines.append("\n─── FI-MÁQUINA ────────────────────────────")
        lines.append(result.fi_machine)

    if output_format in (OutputFormat.HUMAN, OutputFormat.BOTH):
        lines.append("\n─── FI-HUMANO ─────────────────────────────")
        lines.append(result.fi_human)

    if result.densifications:
        lines.append("\n" + "─" * 60)
        lines.append(f"Densificações: {', '.join(result.densifications)}")

    lines.append("\n" + "=" * 60)
    lines.append("Quer refinar? refinar: [instrução] | mais conciso | mais técnico | versão [domínio]")
    lines.append("")

    return "\n".join(lines)


# ============================================================================
# CLI
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        prog="promptforge",
        description="PromptForge — Reasoning Framework Injection Pipeline",
        epilog="Não gere prompts. Injete raciocínio.",
    )

    parser.add_argument(
        "text",
        nargs="?",
        help="Texto (carry) para transformar em Framework Injection"
    )
    parser.add_argument(
        "--domain", "-d",
        choices=list(DOMAINS.keys()),
        help="Forçar domínio específico (auto-detectado se omitido)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["yaml", "human", "both"],
        default="both",
        help="Formato de output (default: both)"
    )
    parser.add_argument(
        "--audio", "-a",
        help="Arquivo de áudio para transcrever (requer speech_recognition)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Mostra pipeline detalhado"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output em formato JSON"
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"PromptForge {VERSION}"
    )

    args = parser.parse_args()

    # Get input text
    text = args.text

    if args.audio:
        # TODO: Implement audio transcription
        print("Erro: Processamento de áudio ainda não implementado.", file=sys.stderr)
        print("Use texto por enquanto.", file=sys.stderr)
        sys.exit(1)

    if not text:
        # Read from stdin
        if not sys.stdin.isatty():
            text = sys.stdin.read().strip()
        else:
            parser.print_help()
            sys.exit(1)

    if not text:
        print("Erro: Nenhum texto fornecido.", file=sys.stderr)
        sys.exit(1)

    # Run pipeline
    output_format = OutputFormat(args.format)
    result = run_pipeline(text, domain=args.domain,
                          output_format=output_format,
                          verbose=args.verbose)

    # Output
    if args.json:
        output = {
            "original": result.original_text,
            "cleaned": result.cleaned_text,
            "voice_detected": result.voice_detected,
            "domain": result.domain,
            "fi_type": result.fi_type,
            "ds_original": result.ds_original,
            "ds_fi": result.ds_fi,
            "ds_improvement": result.ds_improvement,
            "fi_machine": result.fi_machine,
            "fi_human": result.fi_human,
            "densifications": result.densifications,
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        formatted = format_output(result, output_format, args.verbose)
        print(formatted)


if __name__ == "__main__":
    main()
