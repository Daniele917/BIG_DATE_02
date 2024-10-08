# Faça um programa que receba do usuário um vetor com 10 posições. Em seguida deverá ser impresso o maior e o menor elemento do vetor.

# Solicita ao usuário para digitar 10 números e armazena em uma lista
numeros = []

print("Digite 10 números:")
for i in range(10):
    numero = float(input(f"Número {i+1}: "))
    numeros.append(numero)

# Encontra o maior e o menor número da lista
maior = max(numeros)
menor = min(numeros)

# Exibe o maior e o menor número
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
