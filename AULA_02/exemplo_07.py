# Exercicio_02
# Escreva um programa que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula: valorfinal = prestacao+(prestacao*(taxa/100)*tempo)

def calcular_valor_final(prestacao, taxa, tempo):
    valor_final = prestacao + (prestacao * (taxa / 100) * tempo)
    return valor_final

prestacao = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite a taxa de juros (em %): "))
tempo = float(input("Digite o tempo de atraso (em meses): "))

valor_final = calcular_valor_final(prestacao, taxa, tempo)

print(f"O valor final da prestação em atraso é: R$ {valor_final:.2f}")





