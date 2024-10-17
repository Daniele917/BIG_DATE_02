# Versão do Professor-( exerc_03_01.py):
# O Ministro da Saúde, entrou em contato com você e te solicitou um auxílio, para obter as seguintes informações
# sobre os dados da vacinação da covid nos últimos quatro anos:
#- O total e a média de pessoas vacinadas no período.
#- O total e a média da população do Brasil.
#- A taxa de vacinação anual, dos últimos 4 anos, sabendo que para se chegar a esse número, deve-se dividir a quantidade
# de vacinados pela quantidade da população.
# Ele te enviou os seguintes dados:
# ● População Vacinada: 30000000, 25000000, 10000000, 5000000
# ● População Total: 213317639, 214477744, 215574303, 216687971
# E pediu para apresentar na tela o resultado das informações solicitadas.
###
import pandas as pd


def formatar(valor):
    return "{:.2f}%".format(valor)
vacinas = pd.Series([30000000, 25000000, 10000000, 5000000])
populacao = pd.Series([213317639, 214477744, 215574303, 216687971])
tx_vacinacao = ((vacinas / populacao) * 100).apply(formatar)
print("\n-----Dados da Vacinação-----")
print(f"Total de Vacinados{vacinas.sum()}")
print(f"Média de Vacinados{vacinas.mean():.0f}")
print("\n-------Dados da População-----")
print(f"Total da População{populacao.sum()}")
print(f"Média da População{populacao.mean():.0f}")
print("\n------Taxa de Vacinação--------")
print(f"{tx_vacinacao}")