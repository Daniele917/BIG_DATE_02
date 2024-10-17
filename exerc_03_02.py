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

# Dados fornecidos
roubos = pd.Series([100, 90, 80, 120, 110, 90, 70])
furtos = pd.Series([80, 60, 70, 60, 100, 50, 30])
recuperacao = pd.Series([70, 50, 90, 80, 100, 70, 50])

# Cálculo da quantidade diária de roubos + furtos de automóveis
quantidade_diaria_roubos_furtos = roubos + furtos

# Cálculo da taxa de recuperação diária (recuperação / roubo)
taxa_recuperacao_diaria = (recuperacao / roubos) * 100

# Substituir valores NaN por 0 (caso algum roubo seja zero)
taxa_recuperacao_diaria = taxa_recuperacao_diaria.fillna(0)

# Exibindo os resultados
print("Quantidade diária de roubos + furtos de automóveis:")
for i, quantidade in enumerate(quantidade_diaria_roubos_furtos, start=1):
    print(f"Dia {i}: {quantidade}")

print("\nTaxa de recuperação de automóveis diária:")
for i, taxa in enumerate(taxa_recuperacao_diaria, start=1):
    print(f"Dia {i}: {taxa:.2f}%")
