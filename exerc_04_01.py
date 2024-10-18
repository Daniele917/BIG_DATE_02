# - O Gerente de uma importante loja no ramo do varejo, em contato com forma e te

# ) Empregado um auxílio, para obter algumas informações:
#- Gerar um relatório com todos os dados da tabela.
#- O total e uma média de vendas.
#- Uma média das idades, assim como um maior e menor idade.
#- O nome do nome do vendedor com e maior menor quantidade de vendas no. período
#- A quantidade de vendas por sexo. dad0s_vendedores ? ?
 #   'Nome': ['Ana','Bruno','Carlos','Diana ','Eduardo','Fernanda','Gustavo','Helena',Juliana],
  #  'Sexo': [F, M, M, F, F, F,M, F, F,F,F],,
   # 'Idade':[28,34,45,30,40,29,38,31,27,33],
    #'Qtd_vendas':[120,150,110,95,130,140,105,105,1100,135] pediu-so - Para, n.o, na tela, o apresentar das informações,
# Ele te invejo os dados seguintes:

import pandas as pd

# Dados fornecidos
dados_vendedores = {
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena', 'Igor', 'Juliana'],
    'Sexo': ['F', 'M', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Idade': [28, 34, 45, 30, 40, 29, 38, 31, 27, 33],
    'Qtd_vendas': [120, 150, 110, 95, 130, 140, 105, 125, 100, 135]
}

# Criar um DataFrame
df = pd.DataFrame(dados_vendedores)

# 1. Relatório com todos os dados da tabela
print("Relatório completo dos dados:")
print(df)

# 2. Total e média de vendas
total_vendas = df['Qtd_vendas'].sum()
media_vendas = df['Qtd_vendas'].mean()
print("\nTotal de vendas:", total_vendas)
print("Média de vendas:", media_vendas)

# 3. Média das idades, maior e menor idade
media_idade = df['Idade'].mean()
maior_idade = df['Idade'].max()
menor_idade = df['Idade'].min()
print("\nMédia das idades:", media_idade)
print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)

# 4. Nome do vendedor com maior e menor quantidade de vendas no período
vendedor_mais_vendas = df.loc[df['Qtd_vendas'].idxmax(), 'Nome']
vendedor_menos_vendas = df.loc[df['Qtd_vendas'].idxmin(), 'Nome']
print("\nVendedor com maior quantidade de vendas:", vendedor_mais_vendas)
print("Vendedor com menor quantidade de vendas:", vendedor_menos_vendas)

# 5. Quantidade de vendas por sexo
vendas_por_sexo = df.groupby('Sexo')['Qtd_vendas'].sum()
print("\nQuantidade de vendas por sexo:")
print(vendas_por_sexo)
