import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lib_pdsi.signals.delta import delta_signal
from lib_pdsi.signals.unit_step import unitstep_signal
from lib_pdsi.signals.exp_decay import exp_decay_signal


def plot_all_signals():
    """
    Gera plots de todos os sinais básicos em uma única figura.
    """
    # Define o range de n
    n = np.arange(-10, 16)
    
    # Gera os sinais
    delta = delta_signal(n)
    unit_step = unitstep_signal(n)
    exp_decay = exp_decay_signal(n, a=0.8)
    
    # Cria a figura com fundo escuro
    plt.style.use('dark_background')
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    # Plot 1: Delta
    markerline, stemlines, baseline = axes[0].stem(n, delta, linefmt='r-', markerfmt='ro', basefmt='r-')
    markerline.set_markerfacecolor('red')
    markerline.set_markersize(8)
    stemlines.set_linewidth(2)
    axes[0].set_xlabel('n', fontsize=11, color='lime')
    axes[0].set_ylabel('δ[n]', fontsize=11, color='lime')
    axes[0].set_title('1. The unit impulse (Kronecker delta)\nδ[n] = 1 if n = 0, else 0', 
                      fontsize=14, color='lime', pad=15)
    axes[0].grid(True, alpha=0.3, color='gray')
    axes[0].axhline(y=0, color='white', linewidth=0.5)
    axes[0].axvline(x=0, color='white', linewidth=0.5)
    axes[0].set_ylim(-0.2, 1.3)
    
    # Plot 2: Unit Step
    markerline, stemlines, baseline = axes[1].stem(n, unit_step, linefmt='r-', markerfmt='ro', basefmt='r-')
    markerline.set_markerfacecolor('red')
    markerline.set_markersize(8)
    stemlines.set_linewidth(2)
    axes[1].set_xlabel('n', fontsize=11, color='lime')
    axes[1].set_ylabel('u[n]', fontsize=11, color='lime')
    axes[1].set_title('2. The unit step\nu[n] = 1 if n ≥ 0, else 0', 
                      fontsize=14, color='lime', pad=15)
    axes[1].grid(True, alpha=0.3, color='gray')
    axes[1].axhline(y=0, color='white', linewidth=0.5)
    axes[1].axvline(x=0, color='white', linewidth=0.5)
    axes[1].set_ylim(-0.2, 1.3)
    
    # Plot 3: Exponential Decay
    markerline, stemlines, baseline = axes[2].stem(n, exp_decay, linefmt='r-', markerfmt='ro', basefmt='r-')
    markerline.set_markerfacecolor('red')
    markerline.set_markersize(8)
    stemlines.set_linewidth(2)
    axes[2].set_xlabel('n', fontsize=11, color='lime')
    axes[2].set_ylabel('x[n]', fontsize=11, color='lime')
    axes[2].set_title('3. The exponential decay\nx[n] = |a|ⁿu[n],  |a| < 1', 
                      fontsize=14, color='lime', pad=15)
    axes[2].grid(True, alpha=0.3, color='gray')
    axes[2].axhline(y=0, color='white', linewidth=0.5)
    axes[2].axvline(x=0, color='white', linewidth=0.5)
    axes[2].text(0.02, 0.98, 'a = 0.8', 
                transform=axes[2].transAxes, 
                fontsize=11, 
                color='lime',
                verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_all_signals()
