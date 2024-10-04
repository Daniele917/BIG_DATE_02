# Com base nos dados obtidos no programa anterior e sabendo que o veículo usado consome 12 Km/l,construa um programa que determine a quantidade de combustível gasto nessa viagem.


# Função para calcular a quantidade de combustível gasto
def calcular_combustivel_gasto(distancia, consumo):
    combustivel_gasto = distancia / consumo
    return combustivel_gasto

# Leitura da distância percorrida (em km)
distancia = float(input("Digite a distância percorrida em quilômetros: "))

# Consumo do veículo (km/l)
consumo = 12  # km/l

# Cálculo da quantidade de combustível gasto
combustivel_gasto = calcular_combustivel_gasto(distancia, consumo)

# Exibição do resultado
print(f"A quantidade de combustível gasto na viagem é: {combustivel_gasto:.2f} litros")