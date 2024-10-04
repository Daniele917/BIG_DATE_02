# Escreva um programa que, leia dois valores para as variáveis A e B e efetue a troca dos valores de
# forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A.
# Apresente os valores trocados.

# Leitura dos valores para A e B
A = input("Informe o valor da variável A: ")
B = input("Informe o valor da variável B: ")

# Exibindo os valores antes da troca
print(f"\nAntes da troca: A = {A}, B = {B}")

# Troca dos valores
A, B = B, A

# Exibindo os valores após a troca
print(f"Após a troca: A = {A}, B = {B}")
