# pip install xlrd - biblioteca para manipular arquivos xlsx :
# pip install openpyxl - biblioteca para  manipular arquivos xlsx :
import pandas as pd
# Importando base de dados
endereco_dados = 'BASES\ENEM_2020_2023.xlsx'
# Criando o Dataframe
df_enem = pd.read_excel(endereco_dados)
# Exibindo os Dados do Dataframe
print('-----Base de Dados Enem 2020 A 2023------')
print(df_enem.head())
