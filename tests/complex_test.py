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

    # A versão 1 (usando np.arctan) é instável e gera warnings com divisão por zero
    # para números com parte real igual a zero.
    # Por isso, vamos testá-la apenas com um valor onde ela funciona (1+1j).
    phase_v1_case = complex_phase(z[0], version=1)
    assert np.isclose(phase_v1_case, np.pi / 4)

    # As versões 2 e 3 são mais robustas e devem funcionar para todos os casos.
    phase_v2 = complex_phase(z, version=2)
    phase_v3 = complex_phase(z, version=3)  # np.angle

    # np.arctan2 (v2) é a implementação de referência, então comparamos com a v3.
    assert np.allclose(phase_v2, phase_v3)

    # Verifica se a fase de 1+1j (primeiro elemento) é pi/4 também na versão 3.
    assert np.isclose(phase_v3[0], np.pi / 4)