#  # Inicializa a soma e acumula os valores informados pelo usuário em um laço que se repete 5 vezes.

soma = 0
for i in range(5):
    valor = int(input("Informe um Valor:"))
    soma = soma + valor
print(f" A soma é {soma}")  # # Exibe a soma total dos valores inseridos.