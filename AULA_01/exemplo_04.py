# Calcular a idade de uma pessoa a partir do ano de nascimento


import datetime
ano_atual = datetime.date.today()
nome = input("Informe se nome:")
ano_nasc = int(input("Informe ano de nascimento:"))
ano_atual = int(input("Informe o ano atual:"))
idade = ano_atual - ano_nasc
print("Sr(a) ", nome, "a sua idade é: ",idade," anos.")
