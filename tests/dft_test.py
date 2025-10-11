import numpy as np
import pytest

# Importando as suas funções para serem testadas
from core.dft.versions.signal import signal_dft
from core.dft.versions.basis import basis_dft
from core.dft.versions.mtx import matrix_dft
from core.dft.versions.fft import fast_dft

# --- Sinais de Teste ---
# Usamos o pytest.fixture para criar sinais que podem ser reutilizados em vários testes.
@pytest.fixture
def signal_impulse():
    """Sinal de impulso: [1, 0, 0, 0]"""
    return np.array([1, 0, 0, 0])

@pytest.fixture
def signal_dc():
    """Sinal constante (DC): [1, 1, 1, 1]"""
    return np.ones(4)

@pytest.fixture
def signal_sinusoid():
    """Sinal senoidal simples com 8 amostras."""
    N = 8
    n = np.arange(N)
    return np.sin(2 * np.pi * n / N)

# --- Testes Parametrizados ---
# Usamos pytest.mark.parametrize para testar várias funções com o mesmo teste.
@pytest.mark.parametrize("dft_function", [
    signal_dft,
    basis_dft,
    matrix_dft
])
def test_dft_implementations(dft_function, signal_impulse, signal_dc, signal_sinusoid):
    """
    Testa as implementações da DFT comparando com a np.fft.fft.
    Este teste serve para signal_dft, basis_dft e matrix_dft.
    """
    # Teste 1: Impulso
    expected_impulse = np.fft.fft(signal_impulse)
    actual_impulse = dft_function(signal_impulse)
    assert np.allclose(actual_impulse, expected_impulse)

    # Teste 2: Sinal DC
    expected_dc = np.fft.fft(signal_dc)
    actual_dc = dft_function(signal_dc)
    assert np.allclose(actual_dc, expected_dc)

    # Teste 3: Senoide
    expected_sinusoid = np.fft.fft(signal_sinusoid)
    actual_sinusoid = dft_function(signal_sinusoid)
    assert np.allclose(actual_sinusoid, expected_sinusoid)

def test_fft_implementation(signal_sinusoid):
    """
    Teste específico para a implementação da FFT (fast_dft).
    """
    # A FFT precisa de um sinal com tamanho potência de 2. signal_sinusoid tem 8 amostras.
    expected = np.fft.fft(signal_sinusoid)
    actual = fast_dft(signal_sinusoid)
    assert np.allclose(actual, expected)

def test_fft_raises_error_for_non_power_of_two():
    """
    Verifica se a fast_dft levanta um ValueError para sinais de tamanho não-potência de 2.
    """
    signal_not_power_of_2 = np.zeros(7) # 7 não é potência de 2
    with pytest.raises(ValueError):
        fast_dft(signal_not_power_of_2)