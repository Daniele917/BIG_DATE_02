# Construa um programa que calcule e mostre a tabuada de um número inteiro fornecido pelo usuário.



# Solicita um número inteiro ao usuário
numero = int(input("Informe um número inteiro para calcular a tabuada: "))  

# Exibe a tabuada do número
print(f"\nTabuada de {numero}:")

# Laço para calcular e mostrar a tabuada
for i in range(1, 11):  # De 1 a 10
    resultado = numero * i  # Calcula o resultado da multiplicação
    print(f"{numero} x {i} = {resultado}")  # Exibe a multiplicação
