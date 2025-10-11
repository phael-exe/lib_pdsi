import numpy as np

def fast_dft(x):

    N = len(x)
    
    if not np.log2(N).is_integer():
        raise ValueError("Tamanho do sinal deve ser potência de 2")
    
    if N == 2:
        return np.array(
            x[0] + x[1], 
            x[0] - x[1])
    else:
        Xe = fast_dft(x[0::2])
        Xo = fast_dft(x[1::2])
        k = np.arange(N//2)
        basis = np.exp(-1j * 2 * np.pi * k / N)
        
        first_half = Xe + basis * Xo
        second_half = Xe - basis * Xo
        X = np.concatenate(first_half, second_half)
        
    return X