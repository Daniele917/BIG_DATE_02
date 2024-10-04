# Escreva um programa que, tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule e mostre seu peso ideal, utilizando as seguintes fórmulas:
# para sexo masculino: peso ideal = (72.7 * altura) - 58
# para sexo feminino: peso ideal = (62.1 * altura) - 44.7

nome = input("Informe o nome: ")
altura = float(input("Informe a altura (em metros): "))
sexo = input("Informe o sexo (M para masculino, F para feminino): ").upper()

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    sexo_str = "Masculino"
    print(f"{nome}, sexo: {sexo_str}, sua altura: {altura:.2f} m, seu peso ideal é {peso_ideal:.2f} kg.")
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    sexo_str = "Feminino"
    print(f"{nome}, sexo: {sexo_str}, sua altura: {altura:.2f} m, seu peso ideal é {peso_ideal:.2f} kg.")
else:
    print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")