import numpy as np


def delta_signal(n):
    """
    Gera um sinal impulso unitário (delta de Kronecker).
    
    Fórmula: δ[n] = 1 se n = 0, caso contrário 0
    
    Parameters
    ----------
    n : int ou array-like
        Índice(s) do sinal discreto
    
    Returns
    -------
    float ou ndarray
        Valor(es) do sinal impulso unitário
    
    Examples
    --------
    >>> delta_signal(0)
    1.0
    >>> delta_signal(5)
    0.0
    >>> delta_signal(np.arange(-5, 6))
    array([0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.])
    """
    # Converte para array numpy se necessário
    n_array = np.atleast_1d(n)
    
    # Calcula o sinal: 1 em n=0, 0 caso contrário
    result = np.where(n_array == 0, 1.0, 0.0)
    
    # Retorna escalar se a entrada foi escalar
    if np.isscalar(n):
        return float(result[0])
    
    return result