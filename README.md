# macOS LaTeX and AI Starter Kit for Educators

> **Zero-configuration, publication-grade LaTeX environment, deterministic Python figure generator, and AI prompt framework designed for professors, educators, and researchers across Statistics, Econometrics, and Life Sciences on macOS.**

---

## 1. Quick Start Installation

Open the **Terminal** application on macOS (`Command + Space`, type `Terminal`, and press `Return`), then execute the following installation command:

```bash
curl -fsSL https://raw.githubusercontent.com/chrismitsacopoulos/education_stack/main/install.sh | zsh
```

### Automated Configuration Steps:
1. **Silent Typesetting Engine Installation:** Downloads and installs the lightweight MacTeX BasicTeX engine (~130 MB) without prompting for Xcode Command Line Tools or developer dependencies.
2. **Package Resolution:** Synchronizes and installs all required educational fonts, color themes, and diagram libraries via `tlmgr`.
3. **IDE Integration:** Pre-configures Visual Studio Code and Cursor with build-on-save (`latexmk`/`pdflatex`) and side-by-side tabbed PDF previewing.
4. **Workspace Deployment:** Unpacks clean starter templates directly into `~/Documents/Teaching-LaTeX`.

---

## 2. Thematic Educational Suites Catalog

The templates library is structured **thematically by subject**, giving each discipline a complete, coherent teaching suite:

### 2.1 Statistics & Probability Suite (`templates/statistics/`)
| Document | File Path | Focus & Content |
| :--- | :--- | :--- |
| **Lecture Slides (16:9)** | [`templates/statistics/presentation.tex`](templates/statistics/presentation.tex) | Probability axioms, Bayes' rule, CLT asymptotics, standard normal density plot (`gaussian_distribution.png`), and 2x2 contingency tables. |
| **Technical Report** | [`templates/statistics/report.tex`](templates/statistics/report.tex) | Probability spaces, moment transformations, Central Limit Theorem proofs, and categorical $\chi^2$ independence tests. |
| **Midterm Examination** | [`templates/statistics/exam.tex`](templates/statistics/exam.tex) | Probability MCQs, Gaussian $z$-score calculations, and sample Odds Ratio derivations with answer key toggle (`\printanswers`). |
| **Problem Set** | [`templates/statistics/assignment.tex`](templates/statistics/assignment.tex) | Moment generating function derivations, Central Limit Theorem proof, and log Odds Ratio asymptotic variance. |
| **Course Syllabus** | [`templates/statistics/syllabus.tex`](templates/statistics/syllabus.tex) | STAT 401 syllabus with instructor card, grading weights, and 15-week milestone roadmap. |

### 2.2 Econometrics & Causal Inference Suite (`templates/econometrics/`)
| Document | File Path | Focus & Content |
| :--- | :--- | :--- |
| **Lecture Slides (16:9)** | [`templates/econometrics/presentation.tex`](templates/econometrics/presentation.tex) | Potential outcomes, Two-Way Fixed Effects (TWFE), Difference-in-Differences simulation (`econometric_did_plot.png`), and cluster-robust standard errors. |
| **Technical Report** | [`templates/econometrics/report.tex`](templates/econometrics/report.tex) | Panel data identification, within-group demeaning, DiD parallel trends proof, and multi-specification regression tables. |
| **Midterm Examination** | [`templates/econometrics/exam.tex`](templates/econometrics/exam.tex) | Gauss-Markov properties, OLS residual sum of squares minimization proof, and instrument exogeneity conditions. |
| **Problem Set** | [`templates/econometrics/assignment.tex`](templates/econometrics/assignment.tex) | Double-demeaning algebraic proofs, $2 \times 2$ DiD sample mean equivalence, and 2SLS asymptotics. |
| **Course Syllabus** | [`templates/econometrics/syllabus.tex`](templates/econometrics/syllabus.tex) | ECON 401 syllabus with grading scale, term paper requirements, and course policies. |

### 2.3 Biophysics & Ecological Systems Suite (`templates/biology/`)
| Document | File Path | Focus & Content |
| :--- | :--- | :--- |
| **Lecture Slides (16:9)** | [`templates/biology/presentation.tex`](templates/biology/presentation.tex) | Bio-energetics, Lindeman 10% efficiency law, native TikZ Trophic Energy Pyramid, Hill/Michaelis-Menten kinetics, and Lotka-Volterra dynamics. |
| **Technical Report** | [`templates/biology/report.tex`](templates/biology/report.tex) | Trophic thermodynamic dissipation, allosteric enzyme cooperativity, and Lotka-Volterra ODE numerical simulations. |
| **Midterm Examination** | [`templates/biology/exam.tex`](templates/biology/exam.tex) | Competitive inhibition kinetics, trophic energy transfer calculations, and Lineweaver-Burk double-reciprocal derivation. |
| **Problem Set** | [`templates/biology/assignment.tex`](templates/biology/assignment.tex) | Briggs-Haldane quasi-steady-state derivation of Michaelis-Menten kinetics and predator-prey equilibrium stability. |
| **Course Syllabus** | [`templates/biology/syllabus.tex`](templates/biology/syllabus.tex) | BIO 401 syllabus with wet lab schedule, grading components, and course roadmap. |

---

## 3. Shared Python Figure Generator & Assets (`templates/assets/`)

* `templates/assets/generate_figures.py` : Standalone Python script to generate high-DPI ($300\text{ DPI}$) figures using `matplotlib`, `seaborn`, `scipy.stats`, and `numpy`.
* `templates/assets/gaussian_distribution.png` : Standard normal distribution with empirical 68-95-99.7 rule intervals and critical rejection regions ($\alpha=0.05$).
* `templates/assets/econometric_did_plot.png` : Difference-in-Differences simulation displaying treatment, control, and counterfactual trajectories.
* `templates/assets/university_seal.jpg` : Academic crest for title pages and document headers.

To regenerate all figures at any time:
```bash
python3 templates/assets/generate_figures.py
```

---

## 4. Standard Workflow

### Step 1: Choose Your Subject Suite
Open your `Teaching-LaTeX` directory in **Visual Studio Code** or **Cursor** and navigate to your subject folder:
- `templates/statistics/`
- `templates/econometrics/`
- `templates/biology/`

### Step 2: Edit or Prompt an AI Assistant
Edit any `.tex` file directly, or use the pre-formatted AI prompt templates in [`AGENTS.md`](AGENTS.md) to generate exam questions, lecture slides, or assignments.

### Step 3: Compile to PDF
Press **`Cmd + S`**. The editor compiles your document in the background via `latexmk`/`pdflatex`.

### Step 4: Preview Side-by-Side
Click the **View LaTeX PDF** action in the editor title bar (or press `Cmd + Option + V`).

---

## 5. Troubleshooting & FAQ

### How to toggle between Student Exam and Instructor Answer Key?
In any subject's `exam.tex`:
* **Show Solutions:** Uncomment `\printanswers`
* **Hide Solutions (Student Distribution):** Comment out `% \printanswers`

### How to toggle Homework Solutions?
In any subject's `assignment.tex`:
* **Show Solutions:** Set `\solutionstrue`
* **Hide Solutions:** Set `\solutionsfalse`

### Why does my document say "Run LaTeX again to produce the table" or show `[?]`?
LaTeX resolves dynamic table dimensions (like `\gradetable` in `exam.tex`), table column widths, and cross-references (`\label`, `\ref`, `\eqref`) across a two-pass pipeline:
1. **Pass 1:** Scans the document structure and writes coordinates/dimensions to the `.aux` file.
2. **Pass 2:** Reads the `.aux` file to render the aligned table geometry and resolved reference numbers.

When compiling manually via the terminal, run `pdflatex` **twice** (or use `latexmk -pdf`, which handles this automatically). For documents with citations, run `pdflatex` $\to$ `biber`/`bibtex` $\to$ `pdflatex`.

---

## 6. License
MIT License. Open for educational and academic use worldwide.
