# O Secretário de Segurança Pública do Rio de Janeiro, entrou em contato com você de forma urgente e te solicitou

# um auxílio, para obter algumas informações que serão apresentadas ao Governador do Estado:
#- O total e a média de roubos a pedestres no Estado do Rio de Janeiro no último semestre.
#- O total e a média da população no Estado do Rio de Janeiro.
#- O maior e o menor valor encontrado em relação aos roubos de pedestres.
#- O maior e o menor valor encontrado em relação a população.
#- O nome do município com maior e menor índice de roubos a pedestres.
#- O nome do município com maior e menor quantidade de pessoas.
#- A taxa de roubos a pedestres por município, sabendo que para se chegar a esse número, deve-se dividir a quantidade
# de roubos pela quantidade da população.
# Ele te enviou os seguintes dados:

dados_municipio = {
    'Municipio': [
        'Rio de Janeiro', 'Niterói', 'São Gonçalo', 'Duque de Caxias', 'Nova Iguacu',
        'Belford Roxo', 'São João de Meriti', 'Petrópolis', 'Volta Redonda', 'Campos dos Goytacazes'
    ],
    'Habitantes': [6775562, 515317, 1091737, 924624, 821128, 513118, 472906, 306678, 273988, 507548],
    'Roubos a Pedestres': [3500, 2500, 15000, 12000, 10000, 9000, 8500, 1000, 2000, 4000]
}
# E pediu para apresentar na tela o resultado das informações solicitadas.

#####

import pandas as pd

# Dados fornecidos
dados_municipio = {
    'Municipio': [
        'Rio de Janeiro', 'Niterói', 'São Gonçalo', 'Duque de Caxias', 'Nova Iguacu',
        'Belford Roxo', 'São João de Meriti', 'Petrópolis', 'Volta Redonda', 'Campos dos Goytacazes'
    ],
    'Habitantes': [6775562, 515317, 1091737, 924624, 821128, 513118, 472906, 306678, 273988, 507548],
    'Roubos a Pedestres': [3500, 2500, 15000, 12000, 10000, 9000, 8500, 1000, 2000, 4000]
}

# Criar um DataFrame
df = pd.DataFrame(dados_municipio)

# 1. Total e média de roubos a pedestres no último semestre
total_roubos = df['Roubos a Pedestres'].sum()
media_roubos = df['Roubos a Pedestres'].mean()
print("Total de roubos a pedestres:", total_roubos)
print("Média de roubos a pedestres:", media_roubos)

# 2. Total e média da população no Estado do Rio de Janeiro
total_populacao = df['Habitantes'].sum()
media_populacao = df['Habitantes'].mean()
print("\nTotal da população:", total_populacao)
print("Média da população:", media_populacao)

# 3. Maior e menor valor de roubos a pedestres
maior_roubo = df['Roubos a Pedestres'].max()
menor_roubo = df['Roubos a Pedestres'].min()
print("\nMaior quantidade de roubos a pedestres:", maior_roubo)
print("Menor quantidade de roubos a pedestres:", menor_roubo)

# 4. Maior e menor valor em relação à população
maior_populacao = df['Habitantes'].max()
menor_populacao = df['Habitantes'].min()
print("\nMaior população:", maior_populacao)
print("Menor população:", menor_populacao)

# 5. Nome do município com maior e menor índice de roubos a pedestres
municipio_maior_roubo = df.loc[df['Roubos a Pedestres'].idxmax(), 'Municipio']
municipio_menor_roubo = df.loc[df['Roubos a Pedestres'].idxmin(), 'Municipio']
print("\nMunicípio com maior índice de roubos a pedestres:", municipio_maior_roubo)
print("Município com menor índice de roubos a pedestres:", municipio_menor_roubo)

# 6. Nome do município com maior e menor quantidade de habitantes
municipio_maior_populacao = df.loc[df['Habitantes'].idxmax(), 'Municipio']
municipio_menor_populacao = df.loc[df['Habitantes'].idxmin(), 'Municipio']
print("\nMunicípio com maior população:", municipio_maior_populacao)
print("Município com menor população:", municipio_menor_populacao)

# 7. Taxa de roubos a pedestres por município
df['Taxa de Roubos'] = df['Roubos a Pedestres'] / df['Habitantes']
print("\nTaxa de roubos a pedestres por município:")
print(df[['Municipio', 'Taxa de Roubos']])
