# Universal AI Prompt & Style Guide for LaTeX Education

This guide specifies strict syntactic constraints, component patterns, and prompt templates for Large Language Models (Gemini, ChatGPT, Claude, Antigravity, Cursor) generating educational and academic \LaTeX\ documents across three dedicated subject suites: **Statistics & Probability**, **Econometrics & Causal Inference**, and **Biophysics & Ecological Systems**.

---

## 1. Golden Rules for AI LaTeX Generation

### 1.1 Strict Escaping & Special Characters
* **Reserved Symbols:** Always escape `%`, `_`, `&`, `$`, `#`, `{`, `}` when used in regular text (e.g. `10\%`, `user\_id`, `Q\&A`, `item \#1`).
* **Equations & Math:** Ensure every math formula is balanced with `$` (inline) or `\begin{equation*} ... \end{equation*}` (display).
* **Quotes:** Never use standard double quotes (`"word"`). Use proper \LaTeX\ quotes: `` ``word'' `` or `\enquote{word}`.
* **Typewriter Font Linebreaks:** In code listings and typewriter text, use `\texttt{...}` or the `listings` package.

### 1.2 Prohibited vs. Modern Packages
| Prohibited (Obsolete) | Modern Standard Equivalent | Rationale |
| :--- | :--- | :--- |
| `\usepackage{a4wide}` | `\usepackage[a4paper]{geometry}` | Precise margin control without layout bugs |
| `\usepackage{epsfig}` | `\usepackage{graphicx}` | Native PDF image support |
| `\usepackage{t1enc}` | `\usepackage[T1]{fontenc}` | Modern font encoding |
| `\usepackage{times}` | `\usepackage{mathptmx}` | Full Times font including math symbols |
| `\usepackage{doublespace}` | `\usepackage{setspace}` | Safe line spacing adjustments |

### 1.3 Figure & Graphic Strategy (Deterministic Python & Native TikZ)
* **Zero AI-Generated Images:** Do not use or embed generic AI-generated images for data plots, econometric curves, or biological mechanisms.
* **Python / Seaborn Figures:** Generate all empirical, statistical, and econometric charts deterministically using Python (`matplotlib`, `seaborn`, `scipy.stats`, `numpy`) at $\ge 300\text{ DPI}$ with clean annotations and palette alignment.
* **Native TikZ for Biology & Life Sciences:** Typeset biological, cellular, ecological, or anatomical processes directly in native TikZ (e.g., Trophic Energy Pyramids, Food Webs, Reaction Pathways).
* **Graphic Search Paths:** Always configure `\graphicspath{{../assets/}{assets/}{templates/assets/}{../../templates/assets/}{./}}` in the preamble.
* **Aspect Ratios & Dimensions:** Include images using `\includegraphics[width=\linewidth, keepaspectratio]{filename.png}`. In Beamer columns, limit `height=0.68\textheight` to preserve breathing room.
* **Subfigures:** In reports, use `\usepackage{subcaption}` with `\begin{subfigure}[b]{0.48\textwidth}` for multi-panel comparisons.

### 1.4 Mandatory Multi-Pass Compilation & Auxiliary Lifecycle
* **Two-Pass Compilation Requirement:** \LaTeX\ uses an auxiliary pipeline (`.aux`, `.toc`, `.out`). Always compile at least **twice** when modifying documents to resolve:
  * **Dynamic & Complex Tables:** Dynamic width calculations, table row/column shading (`colortbl`), and exam grade summary matrices (`\gradetable`) output "Run LaTeX again to produce the table" or placeholder headers on the initial pass.
  * **Cross-References & Page Counters:** Numbered references (`\ref`, `\eqref`, `\label`), total page counts (`\numpages`, `\numpoints`), and Table of Contents (`\tableofcontents`).
* **Bibliography 3-Step Lifecycle:** For documents with citations, execute:
  1. `pdflatex <doc>.tex` (writes citation keys to `.aux` or `.bcf`)
  2. `biber <doc>` (for Beamer `biblatex`) OR `bibtex <doc>` (for Report `natbib`)
  3. `pdflatex <doc>.tex` (embeds `.bbl` entries; run twice if cross-references shift)
* **Automated Building:** In scripts and IDE tasks, prefer `latexmk -pdf <doc>.tex` which automatically determines the exact number of passes needed.

---

## 2. Subject-Specific Educational Suites

### 2.1 Statistics & Probability (`templates/statistics/`)
* **Core Topics:** Kolmogorov axioms, conditional probability, Bayes' Theorem, moments ($\mathbb{E}[X], \mathrm{Var}(X)$), Lindeberg-L\'{e}vy Central Limit Theorem, Gaussian standard normal density modeling, and contingency association.
* **Key Visuals:** High-DPI `gaussian_distribution.png` with empirical rule bands ($\pm 1\sigma, \pm 2\sigma, \pm 3\sigma$) and critical rejection regions ($\alpha=0.05, z=\pm 1.96$), and pretty 2x2 contingency tables with Pearson's $\chi^2$ and Odds Ratios.

### 2.2 Econometrics & Causal Inference (`templates/econometrics/`)
* **Core Topics:** Potential outcomes (Rubin causal model, SUTVA), Two-Way Fixed Effects (TWFE) within transformation, Difference-in-Differences (DiD) parallel trends identification, Instrumental Variables (2SLS), and Liang-Zeger cluster-robust inference.
* **Key Visuals:** High-DPI `econometric_did_plot.png` showing treatment, control, and counterfactual trajectories, and publication-grade regression comparison tables.

### 2.3 Biophysics & Ecological Systems (`templates/biology/`)
* **Core Topics:** Lindeman's 10\% trophic energy law, thermodynamic dissipation, food web cascades, cooperative Hill/Michaelis-Menten enzyme kinetics, and Lotka-Volterra predator-prey non-linear dynamics.
* **Key Visuals:** Native vector TikZ Ecological Trophic Energy Pyramid with solar assimilation and metabolic heat dissipation arrows.

---

## 3. Document Class & Layout Patterns

### 3.1 16:9 Beamer Presentations (`presentation.tex`)
* **Fragile Frames:** Whenever inserting a code listing, verbatim block, or TikZ matrix with special tokens, **always** specify `\begin{frame}[fragile]{Title}`.
* **Visual Hierarchy UI Helpers:**
  * **Primary Badges:** `\pill{OBJECTIVE}`, `\pill{RESULT}`, `\pill{SUMMARY}` (Vivid Crimson).
  * **Secondary Badges:** `\pillalt{STAGE 1}`, `\pillalt{METHOD}`, `\pillalt{ESTIMATOR}` (Slate Charcoal).
  * **Callout Cards:** Wrap key conclusions in `\begin{takeaway} ... \end{takeaway}`.
  * **KPI Stat Cards:** Use `\kpicard{METRIC}{VALUE}{SUBTITLE}` for empirical stats.
* **Layout Discipline & Breathing Room:** Keep bullet points crisp and punchy (1--2 lines max, 8--14 words). Maintain generous margins.

### 3.2 Academic Technical Reports (`report.tex`)
* **Color Identity:** Use `journalblue` (`\definecolor{journalblue}{RGB}{26, 82, 118}`) for section headers, links, and card borders.
* **Code Snippets:** Wrap code in `\begin{pythonbox}[label={lst:...}]{Listing Title} ... \end{pythonbox}`.
* **Cross-Referencing:** Always use `\label{sec:...}`, `\label{fig:...}`, `\label{tab:...}`, `\label{eq:...}` and reference with `\ref{...}` or `\eqref{...}`.

### 3.3 Examinations and Quizzes (`exam.tex`)
* **Exam Class:** `\documentclass[addpoints, 12pt]{exam}` with toggleable `\printanswers`.
* **Solutions & Rubrics:** Wrap answers in `\begin{solution} ... \end{solution}` and grading criteria in `\begin{rubricbox} ... \end{rubricbox}`.

### 3.4 Homework and Problem Sets (`assignment.tex`)
* **Homework Class:** `\documentclass[12pt, a4paper]{article}` with `\ifsolutions ... \fi` conditional rendering and `\begin{problembox}` wrappers.

### 3.5 Course Syllabi (`syllabus.tex`)
* **Class & Layout:** Professional 11pt article with instructor logistics card, grading weights table, academic integrity policy, and 15-week milestone roadmap.

---

## 4. Ready-to-Use Prompt Templates for Educators

### Prompt 1: Generate Statistics & Probability Slides (16:9 Beamer)
```text
Act as a university professor in Statistics. Using our templates/statistics/presentation.tex style:
- Slide 1: Probability axioms, Bayes' theorem, and CLT formulas using \pillalt{PROBABILITY} and \begin{takeaway}.
- Slide 2: Two-column layout embedding gaussian_distribution.png with empirical rule (68-95-99.7) and rejection region cutoff rules (z = \pm 1.96).
- Slide 3: Pretty 2x2 contingency table using booktabs and colortbl, calculating Pearson's Chi-Square and Odds Ratio with bulleted interpretations.
```

### Prompt 2: Generate Econometric Identification & DiD Lecture Slides
```text
You are an educator in Econometrics. Using our templates/econometrics/presentation.tex style:
- Slide 1: Panel TWFE regression equation and cluster-robust covariance matrix formulas using \pillalt{PANEL}.
- Slide 2: Difference-in-Differences slide embedding econometric_did_plot.png with counterfactual trajectory analysis and parallel trends takeaway.
- Slide 3: Publication-grade regression comparison table (OLS, Fixed Effects, 2SLS) using booktabs and \kpicard{} summary cards.
```

### Prompt 3: Generate Ecological & Biophysical Lecture Slides with TikZ
```text
You are an educator creating modern lecture slides in Biophysics and Ecology using our templates/biology/presentation.tex style:
- Slide 1: Lindeman 10% efficiency law and bio-energetic conservation formulas using \pillalt{BIO-ENERGETICS}.
- Slide 2: A native TikZ Ecological Trophic Energy Pyramid diagram (Producers -> Primary Consumers -> Secondary Consumers -> Apex Predators with metabolic heat loss arrows).
- Slide 3: Michaelis-Menten / Hill kinetics formulation with \begin{takeaway} on enzymatic saturation.
```

### Prompt 4: Create a Quantitative Problem Set with Proof & Rubric
```text
Write a rigorous problem set question on [TOPIC, e.g., Cluster-Robust Covariance Estimation or Contingency Odds Ratios] using our templates/statistics/assignment.tex or templates/econometrics/assignment.tex format.
- Wrap the problem in \begin{problembox}[25 Points]{Problem Title}.
- Part (a): State the estimator formula and null hypothesis.
- Part (b): Mathematical derivation of the asymptotic variance or test statistic.
- Wrap full solutions in \ifsolutions \begin{solutionbox} ... \end{solutionbox} \fi with complete step-by-step proofs.
```
