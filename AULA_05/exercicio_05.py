# Escreva um programa que, dado 5 números inteiros calcule a soma deles e identifique o maior deles.




# Inicializa as variáveis para soma e maior número
soma = 0
maior_numero = float('-inf')  # Define um valor inicial muito baixo

# Solicita 5 números inteiros ao usuário
for i in range(5):
    numero = int(input(f"Informe o {i + 1}º número inteiro: "))  # Lê um número inteiro
    soma += numero  # Adiciona o número à soma

    # Verifica se o número atual é maior que o maior encontrado até agora
    if numero > maior_numero:
        maior_numero = numero  # Atualiza o maior número

# Exibe os resultados
print(f"A soma dos números é: {soma}")
print(f"O maior número é: {maior_numero}")
