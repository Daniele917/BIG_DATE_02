# pip install xlrd - biblioteca para manipular arquivos xlsx :
# pip install openpyxl - biblioteca para  manipular arquivos xlsx :
import pandas as pd
# Importando base de dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
# Criando o Dataframe
df_ocorrencias = pd.read_csv(endereco_dados , sep=';',encoding='iso-8859-1')
# Exibindo os Dados do Dataframe
print('-----Ocorrencias------')
print(df_ocorrencias.head())