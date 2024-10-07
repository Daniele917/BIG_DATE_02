# forneca codigo com nome e idade de 5 pessoas ,depois soma as idades e de a média da quantidade:

soma = 0
maior = 0
for i in range(5):
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    if idade > maior:
        maior = idade
    soma = soma + idade
media = soma / (i + 1)
print(f"A soma é {soma}")
print(f"A média é {media:.0f}")
print(f"A maior idade é {maior}")
