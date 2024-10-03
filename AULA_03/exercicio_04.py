# Média do aluno parte 2:

nome = input("Informe o Nome do Estudante: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2) / 2
print(f"A média do(a) estudante {nome} é: {media:.2f}")

if media >= 70:
    print(f"{nome} , você está Aprovado , pois sua média foi")
elif media >= 30 :
    print(f"{nome} , você está em Recuperação , pois sua média foi")
else:
    print(f"{nome} , você está Reprovado , pois sua média foi")







