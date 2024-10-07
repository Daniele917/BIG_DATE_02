# Faça um programa que armazene em um vetor de 10 posições os votos de um candidato de acordo com a seguinte legenda:


# CANDIDATO NÚMERO
# João Pé das Couves 10
# Antônio Magalhães 30
# Marina Torres 50

# Ao final informe a quantidade de votos de cada candidato e o nome do vencedor.



# Definição dos candidatos e inicialização das contagens de votos
candidatos = {
    10: "João Pé das Couves",
    30: "Antônio Magalhães",
    50: "Marina Torres"
}

votos = {
    10: 0,
    30: 0,
    50: 0
}

# Solicita ao usuário os votos
print("Digite os votos dos 10 eleitores (10 para João Pé das Couves, 30 para Antônio Magalhães, 50 para Marina Torres):")
for i in range(10):
    while True:
        try:
            voto = int(input(f"Voto {i+1}: "))
            if voto in candidatos:
                votos[voto] += 1
                break
            else:
                print("Voto inválido! Por favor, vote 10, 30 ou 50.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

# Exibe a quantidade de votos de cada candidato
print("\nResultados da votação:")
for numero, candidato in candidatos.items():
    print(f"{candidato} recebeu {votos[numero]} votos.")

# Determina o candidato vencedor
vencedor = max(votos, key=votos.get)
print(f"\nO vencedor é: {candidatos[vencedor]} com {votos[vencedor]} votos.")
