# Faça um programa que armazene em vetores o nome, a média e a situação de um grupo de 10 alunos. Ao final mostre o nome de cada aluno com sua respectiva situação.

# Define listas para armazenar as informações dos alunos
nomes = []
medias = []
situacoes = []

# Solicita as informações dos 10 alunos
print("Digite o nome e a média dos 10 alunos:")
for i in range(10):
    nome = input(f"Nome do aluno {i+1}: ")
    media = float(input(f"Média do aluno {i+1}: "))
    nomes.append(nome)
    medias.append(media)
    
    # Define a situação do aluno (Aprovado/Reprovado)
    if media >= 6.0:
        situacoes.append("Aprovado")
    else:
        situacoes.append("Reprovado")

# Exibe o nome de cada aluno com a sua respectiva situação
print("\nNome e situação dos alunos:")
for i in range(10):
    print(f"Aluno: {nomes[i]}, Média: {medias[i]}, Situação: {situacoes[i]}")

