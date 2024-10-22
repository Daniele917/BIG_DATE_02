# pip install xlrd - biblioteca para manipular arquivos xlsx :
# pip install openpyxl - biblioteca para  manipular arquivos xlsx :

import pandas as pd
# Importando base de dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
# Criando o Dataframe
df_ocorrencias = pd.read_csv(endereco_dados , sep=';',encoding='iso-8859-1')
# Exibindo os Dados do Dataframe
print('-----Obtendo Dados------')
print(df_ocorrencias.head())

df_roubo_veiculo = df_ocorrencias[['munic','roubo_veiculo']]
df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum (['roubo_veiculo']).reset_index()

print('\n-----Obtendo Dados Sobre Roubos De Veículos-----')
print(df_roubo_veiculo.head())

