# 2- Escreva um programa que calcule a velocidade média de um veículo com base na distância percorrida e no tempo em que uma viagem foi realizada.




# Função para calcular a velocidade média
def calcular_velocidade_media(distancia, tempo):
    if tempo == 0:
        return 0  # Evitar divisão por zero
    velocidade_media = distancia / tempo
    return velocidade_media

# Leitura da distância percorrida (em km)
distancia = float(input("Digite a distância percorrida em quilômetros: "))

# Leitura do tempo gasto (em horas)
tempo = float(input("Digite o tempo gasto em horas: "))

# Cálculo da velocidade média
velocidade_media = calcular_velocidade_media(distancia, tempo)

# Exibição do resultado
print(f"A velocidade média do veículo é: {velocidade_media:.2f} km/h")