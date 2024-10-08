# Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo
#que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado
#GABARITO com as seguintes respostas: A, B, B, D, E.

# Solicita ao usuário para digitar 10 números inteiros e armazena em uma lista
numeros = []

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)

# Conta quantos números são pares e quantos são ímpares
pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibe a quantidade de números pares e ímpares
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")

# Exibe o vetor principal na ordem inversa
print(f"Vetor na ordem inversa: {numeros[::-1]}")

# Exibe o vetor principal na ordem crescente
print(f"Vetor em ordem crescente: {sorted(numeros)}")
