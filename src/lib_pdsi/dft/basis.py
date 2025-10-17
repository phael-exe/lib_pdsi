import numpy as np

def BasisDFT(N, arg):
    '''
    DFT basis
    '''
    return np.exp(-1j * (2*np.pi / N) * arg)    