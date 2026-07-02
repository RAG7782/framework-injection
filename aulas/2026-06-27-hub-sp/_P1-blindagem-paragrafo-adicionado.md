# P1 — Parágrafo de blindagem adicionado ao paper

> **Arquivo real:** `experimentos/research/papers/paper6-artesanato-digital/paper-v2.tex`
> **Localização:** linha 594, no fim da §Positioning (antes da §Discussion)
> **Commit:** `c83799f`  ·  este arquivo é só uma VISUALIZAÇÃO do trecho (não é o paper).

---

## O texto exato que entrou no paper (LaTeX)

```latex
\paragraph{The category-mistake objection, and why heterogeneity is the point.} A philosopher 
of language will press a deeper objection than the prior-art one: priming and enforcement, she 
argues, are not two points on a scale of coercion but members of \emph{distinct ontological 
categories}---priming is a semantic--intentional property (about meaning and disposition), 
enforcement is a syntactic--mechanical property (about form and physical causation). To speak 
of ``escalating from one to the other'' would then commit the same error as ``escalating from 
yellow to the number seven'': there is no shared dimension, so the ``bridge'' is a mere 
\emph{juxtaposition} of heterogeneous systems, not a traversal. We concede the heterogeneity 
in full---and take it to be constitutive, not fatal. The axis does not assert that the two 
margins are made of one substance; it \emph{couples} two heterogeneous systems through a 
protocol. The shared dimension is not ontological but \emph{functional}: both poles answer one 
operational question---\emph{how much stochastic freedom does this element remove from the 
result?} Priming removes little (it biases the output distribution); enforcement removes all 
that its predicate covers (it rejects what violates). ``Degree of restriction of the output 
space'' is a genuine common dimension, and a measurable one. The governing image is therefore 
not two banks of a single river but \emph{impedance coupling}: two different media joined by 
an interface that transfers structure across their boundary. What FI names and operationalizes 
is precisely that interface---and its contribution survives only because it stops claiming the 
margins share a substance and claims instead that they share a \emph{measurable function}. A 
corollary discharges a residual overclaim: an external verifier secures \emph{verifiability}, 
not \emph{veracity}. A decidable gate (\texttt{grep~-q}, a schema parser, a Boolean second 
agent) proves that a \emph{checkable property} held; it does not prove the answer 
true---\texttt{grep~-q "rating"} passes on a hallucinated rating so long as the token appears. 
Enforcement thus renders a failure \emph{detectable and localizable}; deep semantic 
correctness remains, by construction, outside the gate and within human judgment.
```

---

## O que esse parágrafo faz (em português, sem LaTeX)

**A objeção que ele responde** (a única do red-team que o paper ainda NÃO cobria):
> Um filósofo da linguagem diz: priming e enforcement são categorias ontologicamente
> distintas — priming é semântico/intencional, enforcement é sintático/mecânico. Dizer
> que se 'escala de um ao outro' seria erro de categoria, como 'escalar do amarelo até o
> número sete'. Logo a 'ponte' não existiria — seria só justaposição de coisas incompatíveis.

**A resposta (3 movimentos):**
1. **Concede** a heterogeneidade ontológica — não nega que são categorias diferentes.
2. **Reframe:** a ponte não unifica substâncias, ela ACOPLA sistemas heterogêneos por um
   protocolo. A dimensão comum não é ontológica, é **funcional**: *quanta liberdade
   estocástica este elemento remove do resultado?* — e isso é mensurável ('grau de
   restrição do espaço de saída'). Imagem nova: **acoplamento de impedância**, não
   'margens do mesmo rio' (a metáfora do rio te traía).
3. **Corolário honesto:** o verificador externo garante **verificabilidade, não veracidade**.
   O `grep -q "rating"` passa num rating alucinado se a palavra aparecer. A catraca
   torna o erro *detectável e localizável* — não garante que a resposta é verdadeira.

> **Por que importava:** sem isso, um revisor forte de ML/filosofia derrubava o eixo
> central da tese. Com isso, cada ataque vira uma distinção mais fina. As outras 3
> objeções (prior-art, espectro, bridge_width) o paper JÁ blindava na §Positioning.
