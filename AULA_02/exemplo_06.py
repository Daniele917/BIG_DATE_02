# Exercicio_01
# tendo um dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens:(72.7*h) - 58
# Para mulheres:(62.1*h) -44.7

h = float(input("Informe a altura"))
m = (72.7*h) - 58
f = (62.1*h) - 44.7
print(f"O peso ideal para os homens é {m:.2f} e o peso ideal para as mulheres é {f:.2f}")