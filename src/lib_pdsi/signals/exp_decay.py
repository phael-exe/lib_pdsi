import numpy as np


def exp_decay_signal(n, a):
    """
    Gera um sinal de decaimento exponencial.
    
    Fórmula: x[n] = |a|^n * u[n], onde |a| < 1
    
    Parameters
    ----------
    n : int ou array-like
        Índice(s) do sinal discreto
    a : float
        Coeficiente de decaimento (deve satisfazer |a| < 1)
    
    Returns
    -------
    float ou ndarray
        Valor(es) do sinal de decaimento exponencial
    
    Examples
    --------
    >>> exp_decay_signal(0, 0.8)
    1.0
    >>> exp_decay_signal(5, 0.8)
    0.32768
    >>> exp_decay_signal(np.arange(-5, 10), 0.8)
    array([0.   , 0.   , ..., 0.134])
    """
    if np.abs(a) >= 1:
        raise ValueError(f"O coeficiente 'a' deve satisfazer |a| < 1, mas foi fornecido a={a}")
    
    # Converte para array numpy se necessário
    n_array = np.atleast_1d(n)
    
    # Calcula o sinal: |a|^n * u[n]
    # u[n] é 1 para n >= 0 e 0 para n < 0
    result = np.where(n_array >= 0, np.abs(a) ** n_array, 0)
    
    # Retorna escalar se a entrada foi escalar
    if np.isscalar(n):
        return float(result[0])
    
    return result
