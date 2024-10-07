# Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule
# a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes
# condições:

# - Se a média for maior igual a 70 -> ATENDIDO
# - Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# - Se a média for menor que 30 -> NÃO ATENDIDO

# Define o número de alunos
num_alunos = 10

# Lista para armazenar os resultados
resultados = []

# Solicita as notas de cada aluno
for i in range(num_alunos):
    print(f"\nAluno {i + 1}:")
    nota1 = float(input("Informe a primeira nota: "))  # Solicita a primeira nota
    nota2 = float(input("Informe a segunda nota: "))  # Solicita a segunda nota
    media = (nota1 + nota2) / 2  # Calcula a média

    # Determina a situação de acordo com a média
    if media >= 70:
        situacao = "ATENDIDO"
    elif media >= 30:
        situacao = "PARCIALMENTE ATENDIDO"
    else:
        situacao = "NÃO ATENDIDO"
    
    # Armazena o resultado
    resultados.append((i + 1, media, situacao))

# Exibe os resultados
print("\nResultados dos Alunos:")
for aluno, media, situacao in resultados:
    print(f"Aluno {aluno}: Média = {media:.2f}, Situação: {situacao}")
