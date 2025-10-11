import numpy as np
import pytest

from core.complex.magnitude import complex_magnitude
from core.complex.phase import complex_phase

@pytest.fixture
def sample_complex_numbers():
    """Retorna um array de números complexos para os testes."""
    return np.array([
        1 + 1j,   # Fase: pi/4
        -1 + 1j,  # Fase: 3pi/4
        -1 - 1j,  # Fase: -3pi/4
        1 - 1j,   # Fase: -pi/4
        3 + 4j,   # Magnitude: 5
        0 + 0j
    ])

def test_complex_magnitude(sample_complex_numbers):
    """Testa as duas versões do cálculo de magnitude."""
    z = sample_complex_numbers
    
    # Compara a versão 1 (manual) com a versão 2 (np.abs)
    mag_v1 = complex_magnitude(z, version=1)
    mag_v2 = complex_magnitude(z, version=2)
    
    assert np.allclose(mag_v1, mag_v2)
    
    # Verifica um valor conhecido (3+4j tem magnitude 5)
    assert np.isclose(mag_v1[4], 5)

def test_complex_phase(sample_complex_numbers):
    """Testa as três versões do cálculo de fase."""
    z = sample_complex_numbers
    
    # Compara as versões 1, 2 e 3 entre si
    phase_v1 = complex_phase(z, version=1)
    phase_v2 = complex_phase(z, version=2)
    phase_v3 = complex_phase(z, version=3) # np.angle
    
    # np.arctan2 é a referência mais robusta, então comparamos com a v2 e v3
    assert np.allclose(phase_v2, phase_v3)
    
    # A versão 1 (arctan) falha em alguns quadrantes, então não comparamos com as outras.
    # Mas podemos verificar um valor conhecido onde ela funciona (1+1j).
    assert np.isclose(phase_v1[0], np.pi / 4)
    assert np.isclose(phase_v3[0], np.pi / 4)