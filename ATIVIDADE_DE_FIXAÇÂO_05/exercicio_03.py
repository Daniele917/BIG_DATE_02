# Construa um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.


# Solicita um número inteiro ao usuário
numero = int(input("Informe um número inteiro para calcular o fatorial: "))

# Inicializa a variável para o fatorial
fatorial = 1

# Verifica se o número é negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
else:
    # Calcula o fatorial
    for i in range(1, numero + 1):
        fatorial *= i  # Multiplica o valor atual ao fatorial

    # Exibe o resultado
    print(f"O fatorial de {numero} é: {fatorial}")

