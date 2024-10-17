# Faça um programa que leia duas séries com 10 números inteiros cada e ao final mostre a soma, a subtração, a multiplicação e a divisão entre elas.

import pandas as pd

# Leitura das duas séries
print("Digite 10 números inteiros para a primeira série:")
serie1 = pd.Series([int(input(f"Elemento {i+1}: ")) for i in range(10)])

print("\nDigite 10 números inteiros para a segunda série:")
serie2 = pd.Series([int(input(f"Elemento {i+1}: ")) for i in range(10)])

# Realizando as operações
soma = serie1 + serie2
subtracao = serie1 - serie2
multiplicacao = serie1 * serie2
# Usando o método .where() para evitar divisão por zero e retornando None nesses casos
divisao = serie1.where(serie2 != 0, None) / serie2.where(serie2 != 0, None)

# Mostrando os resultados
print("\nSoma das séries:")
print(soma)

print("\nSubtração das séries:")
print(subtracao)

print("\nMultiplicação das séries:")
print(multiplicacao)

print("\nDivisão das séries (com tratamento de divisão por zero):")
print(divisao)

