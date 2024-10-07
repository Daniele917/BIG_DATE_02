# Utilizando a estrutura do programa anterior, identifique o nome da pessoa mais velha.



# Inicializa a soma das idades e o número de pessoas
soma_idades = 0
num_pessoas = 10  # Define o número total de pessoas

# Variáveis para armazenar o nome da pessoa mais velha e sua idade
nome_mais_velho = ""
idade_mais_velho = 0

# Lista para armazenar os nomes
nomes = []

# Solicita o nome e a idade de 10 pessoas
for i in range(num_pessoas):
    nome = input(f"Informe o nome da pessoa {i + 1}: ")  # Solicita o nome
    idade = int(input(f"Informe a idade de {nome}: "))  # Solicita a idade
    nomes.append(nome)  # Adiciona o nome à lista
    soma_idades += idade  # Adiciona a idade à soma total

    # Verifica se a idade atual é maior que a idade da pessoa mais velha
    if idade > idade_mais_velho:
        idade_mais_velho = idade  # Atualiza a idade da pessoa mais velha
        nome_mais_velho = nome  # Atualiza o nome da pessoa mais velha

# Calcula a média das idades
media_idade = soma_idades / num_pessoas

# Exibe os resultados
print("\nNomes das pessoas:")
for nome in nomes:
    print(nome)

print(f"\nA soma das idades é: {soma_idades}")
print(f"A média das idades é: {media_idade:.2f}")  # Exibe a média com duas casas decimais
print(f"A pessoa mais velha é: {nome_mais_velho} com {idade_mais_velho} anos.")
