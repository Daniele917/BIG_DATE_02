# Calcule a variância e o desvio padrão do conjunto de dados: 5, 10, 15.

import statistics

# Conjunto de dados
dados = [5, 10, 15]

# Cálculo da variância
variancia = statistics.variance(dados)

# Cálculo do desvio padrão
desvio_padrao = statistics.stdev(dados)

print(f"Variância: {variancia}")
print(f"Desvio Padrão: {desvio_padrao}")

# Variância: 25
# Desvio Padrão: 5