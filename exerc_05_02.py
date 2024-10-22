# pip install xlrd - biblioteca para manipular arquivos xlsx :
# pip install openpyxl - biblioteca para  manipular arquivos xlsx :
import pandas as pd
# Importando base de dados
endereco_dados = 'BASES\Financeira.csv'
# Criando o Dataframe
df_financeira= pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')
# Exibindo os Dados do Dataframe
print('-----Dados Financeiros------')
print(df_financeira.head())