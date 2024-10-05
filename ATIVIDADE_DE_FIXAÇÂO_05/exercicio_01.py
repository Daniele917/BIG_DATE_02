# Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e
# se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor
# não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo
# segundo valor.

# Solicita o primeiro valor
valor1 = float(input("Informe o primeiro valor: "))

# Inicializa o segundo valor como zero
valor2 = 0

# Laço para garantir que o segundo valor não seja zero
while valor2 == 0:
    valor2 = float(input("Informe o segundo valor (não pode ser zero): "))  # Solicita o segundo valor

# Realiza a divisão e exibe o resultado
resultado = valor1 / valor2
print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado}")
