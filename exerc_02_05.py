#O Delegado responsável pela Delegacia de roubos e furtos de automóveis, entrou em contato com você e te solicitou um auxílio, para obter duas informações:
#- A quantidade de roubos de automóveis + furto de automóveis diária, dos últimos 7 dias.
#- A taxa de recuperação de automóveis diária, dos últimos 7 dias, sabendo que para se chegar a esse número, deve-se dividir a quantidade de
#recuperação de automóveis pela quantidade de roubo de automóveis.
#Ele te enviou os seguintes dados:
#● Roubo de automóveis: 100,90,80,120,110,90,70
#● Furto de automóveis: 80,60,70,60,100,50,30
#● Recuperação de automóveis: 70,50,90,80,100,70,50
#E pediu para apresentar na tela o resultado das informações solicitadas.

import pandas as pd

# Dados fornecidos
roubo_automoveis = pd.Series([100, 90, 80, 120, 110, 90, 70])
furto_automoveis = pd.Series([80, 60, 70, 60, 100, 50, 30])
recuperacao_automoveis = pd.Series([70, 50, 90, 80, 100, 70, 50])

# 1. Cálculo da quantidade de roubos + furtos diários
quantidade_roubo_furto_diaria = roubo_automoveis + furto_automoveis

# 2. Cálculo da taxa de recuperação diária
# Evitar divisão por zero ao calcular a taxa de recuperação
taxa_recuperacao_diaria = recuperacao_automoveis / roubo_automoveis
taxa_recuperacao_diaria = taxa_recuperacao_diaria.fillna(0) * 100  # Multiplicando por 100 para obter em porcentagem

# Exibindo os resultados
print("Quantidade de roubos + furtos de automóveis diária (últimos 7 dias):")
print(quantidade_roubo_furto_diaria)

print("\nTaxa de recuperação de automóveis diária (últimos 7 dias):")
print(taxa_recuperacao_diaria)
