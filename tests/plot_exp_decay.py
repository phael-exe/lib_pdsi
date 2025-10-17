import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lib_pdsi.signals.exp_decay import exp_decay_signal


def plot_exp_decay():
    """
    Gera o plot do sinal de decaimento exponencial.
    x[n] = |a|^n * u[n], |a| < 1
    """
    # Define o range de n
    n = np.arange(-5, 16)
    
    # Parâmetro de decaimento
    a = 0.8
    
    # Gera o sinal
    x = exp_decay_signal(n, a)
    
    # Cria a figura com fundo escuro
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot do sinal como stem (hastes)
    markerline, stemlines, baseline = ax.stem(n, x, linefmt='r-', markerfmt='ro', basefmt='r-')
    markerline.set_markerfacecolor('red')
    markerline.set_markersize(8)
    stemlines.set_linewidth(2)
    
    # Configurações do gráfico
    ax.set_xlabel('n', fontsize=12, color='lime')
    ax.set_ylabel('x[n]', fontsize=12, color='lime')
    ax.set_title('3. The exponential decay\nx[n] = |a|ⁿu[n],  |a| < 1', 
                 fontsize=16, color='lime', pad=20)
    ax.grid(True, alpha=0.3, color='gray')
    ax.axhline(y=0, color='white', linewidth=0.5)
    ax.axvline(x=0, color='white', linewidth=0.5)
    
    # Adiciona texto com o valor de a
    ax.text(0.02, 0.98, f'a = {a}', 
            transform=ax.transAxes, 
            fontsize=12, 
            color='lime',
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='black', alpha=0.5))
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_exp_decay()
