# O Delegado responsável pela Delegacia de roubos e furtos de automóveis, entrou em contato com você e te

# solicitou um auxílio, para obter duas informações:
# - A quantidade de roubos de automóveis + furto de automóveis diária, dos últimos 7 dias.
# - A taxa de recuperação de automóveis diária, dos últimos 7 dias, sabendo que para se chegar a esse número, deve-se
# dividir a quantidade de recuperação de automóveis pela quantidade de roubo de automóveis.
# Ele te enviou os seguintes dados:
# ● Roubo de automóveis: 100,90,80,120,110,90,70
# ● Furto de automóveis: 80,60,70,60,100,50,30
# ● Recuperação de automóveis: 70,50,90,80,100,70,50
# E pediu para apresentar na tela o resultado das informações solicitadas.

###

import pandas as pd

# Criando uma função para formatar número
def formatar(valor):
    return "{:.2f}%".format(valor)

# Criando o Código
roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
recuperacao = pd.Series([70,50,90,80,100,70,50])
roubo_furto = roubo + furto
tx_recuperacao = ((recuperacao / roubo_furto) * 100).apply(formatar)
print("\n- Total Geral de Roubos -")
print(f"{roubo_furto.sum()}")
print("\n- Total de Roubos Diários -")
print(f"{roubo_furto}")
print("\n- Taxa de Recuperação Diária -")
print(f"{tx_recuperacao}")
