# exerc_03_03.py em Dataframe:

import pandas as pd
vendedores = {
    'Nome':['Maria', 'João', 'Manoel'],
    'Vendas_01':[800,900,700],
    'Vendas_02':[700,500,500],
    'Vendas_03':[1000,1100,900],
    'Vendas_04':[900,1000,1200]
}
df_vendedores = pd.DataFrame(vendedores)
print(df_vendedores)