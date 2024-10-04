# Faça um programa que solicite o nome e as três notas de um estudante. Calcule a média desse estudante e ao final informe a sua condição de acordo com a descrição abaixo:

#• APROVADO – Média >= 75.
# • RECUPERAÇÃO – Média entre 75 e 40.
#• REPROVADO – Média <= 40.

# Entrada de dados
nome = input("Informe o nome do estudante: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Determinação da condição
if media >= 75:
    condicao = "APROVADO"
elif media >= 40:
    condicao = "RECUPERAÇÃO"
else:
    condicao = "REPROVADO"

# Exibição dos resultados
print(f"\nNome: {nome}")
print(f"Média: {media:.2f}")
print(f"Condição: {condicao}")