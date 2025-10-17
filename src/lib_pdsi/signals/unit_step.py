import numpy as np


def unitstep_signal(n):
    """
    Gera um sinal degrau unitário.
    
    Fórmula: u[n] = 1 se n >= 0, caso contrário 0
    
    Parameters
    ----------
    n : int ou array-like
        Índice(s) do sinal discreto
    
    Returns
    -------
    float ou ndarray
        Valor(es) do sinal degrau unitário
    
    Examples
    --------
    >>> unitstep_signal(0)
    1.0
    >>> unitstep_signal(-5)
    0.0
    >>> unitstep_signal(np.arange(-5, 6))
    array([0., 0., 0., 0., 0., 1., 1., 1., 1., 1., 1.])
    """
    # Converte para array numpy se necessário
    n_array = np.atleast_1d(n)
    
    # Calcula o sinal: 1 para n >= 0, 0 para n < 0
    result = np.where(n_array >= 0, 1.0, 0.0)
    
    # Retorna escalar se a entrada foi escalar
    if np.isscalar(n):
        return float(result[0])
    
    return result