# Scripts de Visualização de Sinais

Este diretório contém scripts para visualizar os sinais discretos básicos implementados na biblioteca.

## Arquivos de Plot

### Plots Individuais

1. **plot_delta.py** - Plot do impulso unitário (Delta de Kronecker)
   - Fórmula: δ[n] = 1 se n = 0, caso contrário 0

2. **plot_unit_step.py** - Plot do degrau unitário
   - Fórmula: u[n] = 1 se n ≥ 0, caso contrário 0

3. **plot_exp_decay.py** - Plot do decaimento exponencial
   - Fórmula: x[n] = |a|ⁿu[n], onde |a| < 1
   - Parâmetro padrão: a = 0.8

### Plot Combinado

4. **plot_all_signals.py** - Exibe todos os três sinais em uma única figura

## Como Executar

Para executar qualquer plot individualmente:

```bash
python3 tests/plot_delta.py
python3 tests/plot_unit_step.py
python3 tests/plot_exp_decay.py
```

Para visualizar todos os sinais de uma vez:

```bash
python3 tests/plot_all_signals.py
```

## Correções Realizadas

As funções `delta_signal` e `unitstep_signal` foram atualizadas para:
- ✅ Suportar arrays numpy como entrada
- ✅ Retornar arrays quando a entrada é um array
- ✅ Retornar escalares quando a entrada é escalar
- ✅ Incluir documentação completa (docstrings)
- ✅ Seguir o mesmo padrão da função `exp_decay_signal`

## Dependências

Os scripts de plot requerem:
- numpy
- matplotlib

Certifique-se de que essas dependências estão instaladas no seu ambiente.
