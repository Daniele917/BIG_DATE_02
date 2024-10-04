
# Função para encontrar o maior número entre três inteiros
def maior_numero(n1, n2, n3):
    return max(n1, n2, n3)

# Coletando os números inteiros do usuário
n1 = int(input("Digite o primeiro número (n1): "))
n2 = int(input("Digite o segundo número (n2): "))
n3 = int(input("Digite o terceiro número (n3): "))

# Encontrando o maior número
maior = maior_numero(n1, n2, n3)

# Exibindo o resultado
print(f"O maior número entre {n1}, {n2} e {n3} é: {maior}")
