#Escreva um programa que leia uma série com 10 notas e ao final separe as que estão acima das que estão abaixo da média (Média = 70).

import pandas as pd

# Leitura da série de notas
print("Digite 10 notas:")
notas = pd.Series([float(input(f"Nota {i+1}: ")) for i in range(10)])

# Definindo a média
media = 70

# Separando as notas acima ou iguais e abaixo da média
notas_acima = notas[notas >= media]
notas_abaixo = notas[notas < media]

# Mostrando os resultados
print("\nNotas acima ou iguais a 70:")
print(notas_acima)

print("\nNotas abaixo de 70:")
print(notas_abaixo)
