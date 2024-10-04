
# Função para verificar se a pessoa pode doar sangue
def pode_doar_sangue(idade, peso, horas_dormidas):
    if 16 <= idade <= 69 and peso > 50 and horas_dormidas >= 6:
        return True
    return False

# Coletando informações do usuário
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso em kg: "))
horas_dormidas = float(input("Quantas horas você dormiu nas últimas 24 horas? "))

# Verificando se a pessoa pode doar sangue
if pode_doar_sangue(idade, peso, horas_dormidas):
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue.")
