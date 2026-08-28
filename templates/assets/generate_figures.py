#!/usr/bin/env python3
"""
Publication-Grade Figure Generation Engine
Generates high-DPI (300 DPI) scientific and statistical figures using Matplotlib, Seaborn, SciPy, and NumPy.
Theme: Crimson (#DC2828), Dark Slate (#1E1E28), Journal Navy (#1A5276), Muted Slate (#505060).
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
from scipy import stats

# Configure styling
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans, sans-serif'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['mathtext.fontset'] = 'cm'  # Computer Modern for LaTeX math look
plt.rcParams['figure.autolayout'] = False
plt.rcParams['axes.edgecolor'] = '#32323C'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#E2E8F0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.alpha'] = 0.7

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def generate_gaussian_distribution():
    """Generates a high-DPI annotated Standard Normal Distribution with empirical rule and rejection regions."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=300)
    
    mu, sigma = 0, 1
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, mu, sigma)
    
    # Base density curve
    ax.plot(x, y, color='#1E1E28', lw=2.2, label=r'Standard Normal $\mathcal{N}(0, 1)$', zorder=5)
    
    # 3-Sigma Interval (99.73%)
    mask_3 = (x >= -3) & (x <= 3)
    ax.fill_between(x[mask_3], y[mask_3], color='#1A5276', alpha=0.12, label=r'$\pm 3\sigma$ (99.73\%)', zorder=2)
    
    # 2-Sigma Interval (95.45%)
    mask_2 = (x >= -2) & (x <= 2)
    ax.fill_between(x[mask_2], y[mask_2], color='#1A5276', alpha=0.20, label=r'$\pm 2\sigma$ (95.45\%)', zorder=3)
    
    # 1-Sigma Interval (68.27%)
    mask_1 = (x >= -1) & (x <= 1)
    ax.fill_between(x[mask_1], y[mask_1], color='#1A5276', alpha=0.35, label=r'$\pm 1\sigma$ (68.27\%)', zorder=4)
    
    # Rejection Regions (alpha = 0.05, two-tailed: z < -1.96 or z > 1.96)
    z_crit = 1.96
    mask_left = x <= -z_crit
    mask_right = x >= z_crit
    ax.fill_between(x[mask_left], y[mask_left], color='#DC2828', alpha=0.55, zorder=6)
    ax.fill_between(x[mask_right], y[mask_right], color='#DC2828', alpha=0.55, zorder=6)
    
    # Vertical Reference Lines
    for val in [-3, -2, -1, 1, 2, 3]:
        ax.axvline(val, color='#718096', linestyle=':', lw=0.9, alpha=0.6, zorder=4)
    ax.axvline(0, color='#1E1E28', linestyle='--', lw=1.2, alpha=0.85, zorder=5)
    
    # Annotations
    ax.annotate(r'$\mu = 0$', xy=(0, stats.norm.pdf(0, mu, sigma)), xytext=(0, 0.43),
                ha='center', fontsize=10, fontweight='bold', color='#1E1E28',
                arrowprops=dict(arrowstyle='->', color='#1E1E28', lw=1.0))
    
    # Rejection region labels
    ax.annotate(r'Critical Region' + '\n' + r'$\alpha/2 = 0.025$ ($z < -1.96$)',
                xy=(-2.2, 0.02), xytext=(-3.5, 0.14),
                fontsize=8.5, color='#DC2828', fontweight='bold', ha='center',
                arrowprops=dict(arrowstyle='->', color='#DC2828', lw=1.1, connectionstyle="arc3,rad=-0.2"))
    
    ax.annotate(r'Critical Region' + '\n' + r'$\alpha/2 = 0.025$ ($z > +1.96$)',
                xy=(2.2, 0.02), xytext=(3.5, 0.14),
                fontsize=8.5, color='#DC2828', fontweight='bold', ha='center',
                arrowprops=dict(arrowstyle='->', color='#DC2828', lw=1.1, connectionstyle="arc3,rad=0.2"))
    
    # Empirical Rule text box
    emp_text = (r"$\mathbf{Empirical\ Rule:}$" + "\n"
                r"$\bullet\ P(\mu \pm 1\sigma) = 68.27\%$" + "\n"
                r"$\bullet\ P(\mu \pm 2\sigma) = 95.45\%$" + "\n"
                r"$\bullet\ P(\mu \pm 3\sigma) = 99.73\%$")
    ax.text(0.04, 0.93, emp_text, transform=ax.transAxes, fontsize=8.5,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.5', facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=0.8))
    
    # Formatting
    ax.set_title(r'Standard Normal Distribution $\mathcal{N}(\mu=0, \sigma^2=1)$ and Hypothesis Testing',
                 fontsize=11.5, fontweight='bold', color='#1E1E28', pad=12)
    ax.set_xlabel(r'Standardized Value ($z = \frac{X - \mu}{\sigma}$)', fontsize=9.5, fontweight='bold', color='#1E1E28')
    ax.set_ylabel('Probability Density $f(z)$', fontsize=9.5, fontweight='bold', color='#1E1E28')
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 0.46)
    ax.grid(True, zorder=1)
    ax.set_axisbelow(True)
    
    # Custom ticks
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_xticklabels([r'$-3\sigma$', r'$-2\sigma$', r'$-1\sigma$', r'$\mu$', r'$+1\sigma$', r'$+2\sigma$', r'$+3\sigma$'], fontsize=9)
    
    plt.tight_layout()
    output_path = os.path.join(SCRIPT_DIR, 'gaussian_distribution.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated: {output_path}")


def generate_econometric_did():
    """Generates a high-DPI Difference-in-Differences (DiD) simulation plot with counterfactual and parallel trends."""
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=300)
    
    # Simulation Parameters
    np.random.seed(42)
    time_periods = np.array([1, 2, 3, 4, 5, 6])
    t_intervention = 3.5
    
    # Baseline trends
    trend_control = 10.0 + 1.2 * time_periods
    trend_treated_pre = 14.0 + 1.2 * time_periods
    
    # Counterfactual without treatment (parallel trends continued)
    counterfactual = trend_treated_pre.copy()
    
    # True treatment effect delta = +3.2 starting from period 4
    treatment_effect = np.array([0, 0, 0, 3.2, 3.4, 3.6])
    trend_treated_post = trend_treated_pre + treatment_effect
    
    # Add simulated cohort scatter points
    n_samples = 40
    for t_idx, t in enumerate(time_periods):
        # Control scatter
        ctrl_y = trend_control[t_idx] + np.random.normal(0, 0.65, n_samples)
        ax.scatter(np.repeat(t - 0.08, n_samples), ctrl_y, color='#1A5276', alpha=0.15, s=12, zorder=3)
        
        # Treated scatter
        treat_y = (trend_treated_post[t_idx] if t > t_intervention else trend_treated_pre[t_idx]) + np.random.normal(0, 0.65, n_samples)
        ax.scatter(np.repeat(t + 0.08, n_samples), treat_y, color='#DC2828', alpha=0.15, s=12, zorder=3)
    
    # Plot Trajectory Lines
    ax.plot(time_periods, trend_control, marker='o', markersize=6, color='#1A5276', lw=2.4,
            label='Control Group ($D=0$)', zorder=5)
    
    # Treated observed trajectory (pre & post)
    ax.plot(time_periods[:3], trend_treated_pre[:3], marker='s', markersize=6, color='#DC2828', lw=2.4,
            label='Treated Group ($D=1$, Pre)', zorder=5)
    ax.plot(time_periods[2:], trend_treated_post[2:], marker='s', markersize=6, color='#DC2828', lw=2.4,
            label='Treated Group ($D=1$, Post)', zorder=5)
    
    # Counterfactual line (dashed)
    ax.plot(time_periods[2:], counterfactual[2:], marker='^', markersize=5, color='#718096', lw=2.0,
            linestyle='--', label=r'Counterfactual $\mathbb{E}[Y(0) \mid D=1]$', zorder=4)
    
    # Intervention vertical divider
    ax.axvline(t_intervention, color='#32323C', linestyle='-', lw=1.5, alpha=0.75, zorder=4)
    ax.text(t_intervention, 23.8, 'Policy Reform ($t^*$)', ha='center', va='bottom',
            fontsize=9, fontweight='bold', color='#32323C',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor='#F59E0B', lw=0.8))
    
    # Pre-intervention parallel trends shaded band
    ax.axvspan(0.6, t_intervention, color='#F1F5F9', alpha=0.8, zorder=1, label='Pre-Treatment Horizon')
    
    # Highlight Treatment Effect Delta at t=6
    t_end = 6
    y_actual = trend_treated_post[-1]
    y_counter = counterfactual[-1]
    
    # Double-headed delta arrow / bracket
    ax.annotate('', xy=(t_end + 0.18, y_actual), xytext=(t_end + 0.18, y_counter),
                arrowprops=dict(arrowstyle='<->', color='#DC2828', lw=2.0))
    ax.text(t_end + 0.28, (y_actual + y_counter) / 2, r'$\hat{\delta}_{\mathrm{DiD}} = +3.60^{***}$' + '\n' + r'($p < 0.001$)',
            va='center', fontsize=9, fontweight='bold', color='#DC2828')
    
    # Formula & Key Invariant Card
    formula_card = (r"$\mathbf{Difference\text{-}in\text{-}Differences\ Identification:}$" + "\n"
                    r"$\hat{\delta}_{\mathrm{DiD}} = (\bar{Y}_{T,2} - \bar{Y}_{T,1}) - (\bar{Y}_{C,2} - \bar{Y}_{C,1})$" + "\n"
                    r"$\mathbf{Parallel\ Trends:}\ \mathbb{E}[\Delta Y_i(0) \mid D_i=1] = \mathbb{E}[\Delta Y_i(0) \mid D_i=0]$")
    ax.text(0.04, 0.93, formula_card, transform=ax.transAxes, fontsize=8.2,
            verticalalignment='top', bbox=dict(boxstyle='round,pad=0.45', facecolor='#F8FAFC', edgecolor='#CBD5E1', lw=0.8))
    
    # Formatting
    ax.set_title(r'Causal Identification: Difference-in-Differences with Parallel Trends',
                 fontsize=11.5, fontweight='bold', color='#1E1E28', pad=12)
    ax.set_xlabel('Time Horizon / Cohort Period ($t$)', fontsize=9.5, fontweight='bold', color='#1E1E28')
    ax.set_ylabel('Outcome Variable ($Y_{it}$)', fontsize=9.5, fontweight='bold', color='#1E1E28')
    ax.set_xlim(0.6, 6.9)
    ax.set_ylim(8.5, 25.5)
    ax.set_xticks(time_periods)
    ax.set_xticklabels([f'Period {t}' for t in time_periods], fontsize=8.5)
    ax.grid(True, zorder=1)
    ax.set_axisbelow(True)
    
    plt.tight_layout()
    output_path = os.path.join(SCRIPT_DIR, 'econometric_did_plot.png')
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Generated: {output_path}")

if __name__ == '__main__':
    print("Generating publication-grade scientific figures...")
    generate_gaussian_distribution()
    generate_econometric_did()
    print("All figures successfully created at 300 DPI.")
