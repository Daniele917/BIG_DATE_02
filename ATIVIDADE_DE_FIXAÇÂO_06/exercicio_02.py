# Construa um programa que armazene em vetores o nome, a idade e o sexo de 10
# pessoas. Ao final informe o nome da pessoa mais nova e da mais velha, a quantidade de
# pessoas maiores de idade e a quantidade de pessoas do sexo feminino.

# Define listas para armazenar as informações das pessoas
nomes = []
idades = []
sexos = []

# Solicita as informações das 10 pessoas
print("Digite o nome, idade e sexo (M/F) de 10 pessoas:")
for i in range(10):
    nome = input(f"Nome da pessoa {i+1}: ")
    idade = int(input(f"Idade da pessoa {i+1}: "))
    sexo = input(f"Sexo da pessoa {i+1} (M/F): ").strip().upper()

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

# Determina
