# Calcule a média, mediana e moda do conjunto de dados: 10, 20, 20, 30, 40.

import statistics

# Conjunto de dados
dados = [10, 20, 20, 30, 40]

# Cálculo da média
media = statistics.mean(dados)

# Cálculo da mediana
mediana = statistics.median(dados)

# Cálculo da moda
moda = statistics.mode(dados)

print(f"Média: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")

Média: 24
Mediana: 20
Moda: 20