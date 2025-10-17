import numpy as np
import matplotlib.pyplot as plt
import sys
from pathlib import Path

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from lib_pdsi.signals.unit_step import unitstep_signal


def plot_unit_step():
    """
    Gera o plot do sinal degrau unitário.
    u[n] = 1 se n >= 0, caso contrário 0
    """
    # Define o range de n
    n = np.arange(-10, 11)
    
    # Gera o sinal
    x = unitstep_signal(n)
    
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
    ax.set_ylabel('u[n]', fontsize=12, color='lime')
    ax.set_title('2. The unit step\nu[n] = 1 if n ≥ 0, else 0', 
                 fontsize=16, color='lime', pad=20)
    ax.grid(True, alpha=0.3, color='gray')
    ax.axhline(y=0, color='white', linewidth=0.5)
    ax.axvline(x=0, color='white', linewidth=0.5)
    ax.set_ylim(-0.2, 1.3)
    
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    plot_unit_step()
