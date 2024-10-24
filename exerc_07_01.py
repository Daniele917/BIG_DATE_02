# Medidas de Tendência Central
# Para encontrar o meio dos dados, usa-se a seguinte fórmula:
# A Operadora gostaria de saber qual seria a mediana da renda de seus clientes e qual
# seria a mediana do valor que ela tem emprestado para eles.
# ANALISTA DE DADOS – BIG DATA SCIENCE
# Medidas de Tendência Central
# Moda
# É uma medida de posição para variáveis categóricas, “usada para identificar o que
# concentrados.
# está na moda”, ou seja, onde a maior quantidade de registros dos dados estão 
# Exemplo:
# Foi realizado uma pesquisa com 10 pessoas para saber a cor preferida delas, 6
# informaram a cor azul, 3 vermelha e 1 verde. A moda dessa variável “cor preferida” seria azul.
# A operadora quer saber onde está concentrado seus clientes em relação ao grupo de
# risco. Como a variável grupo de risco é categórica, então use-se a moda:
# ANALISTA DE DADOS – BIG DATA SCIENCE
# Medidas de Tendência Central
# Quantis
# São pontos que dividem uma distribuição de probabilidade em partições de tamanhos iguais.
# Eles podem ser quartis (sendo o 1o quartil correspondente a 25% dos dados, o
# segundo quartil correspondente a 50% dos dados – a mediana e o 3o quartil correspondente
# a 75% dos dados) ou percentis (dividem a amostra em 100 partes).
# A Operadora gostaria de saber qual seria a distribuição da renda de seus clientes e
# os valores que ela tem emprestado para eles.




import pandas as pd

# Exemplo de dados
dados = {
    'renda_clientes': [3000, 4500, 5000, 5500, 7000, 10000, 12000, 20000],
    'valor_emprestado': [500, 1500, 2000, 2500, 3000, 3500, 4000, 4500]
}

df = pd.DataFrame(dados)
# Média aritmética
media_renda = df['renda_clientes'].mean()
media_emprestado = df['valor_emprestado'].mean()

print(f"Média da renda dos clientes: {media_renda}")
print(f"Média do valor emprestado: {media_emprestado}")

# Mediana
mediana_renda = df['renda_clientes'].median()
mediana_emprestado = df['valor_emprestado'].median()

print(f"Mediana da renda dos clientes: {mediana_renda}")
print(f"Mediana do valor emprestado: {mediana_emprestado}")

# Moda (Exemplo para variável categórica)
grupo_risco = ['Alto', 'Médio', 'Alto', 'Baixo', 'Médio', 'Alto', 'Baixo', 'Médio']
df['grupo_risco'] = grupo_risco

# Moda
moda_grupo_risco = df['grupo_risco'].mode()[0]

print(f"Moda do grupo de risco: {moda_grupo_risco}")

# Quartis
quartis_renda = df['renda_clientes'].quantile([0.25, 0.5, 0.75])
quartis_emprestado = df['valor_emprestado'].quantile([0.25, 0.5, 0.75])

print(f"Quartis da renda dos clientes:\n{quartis_renda}")
print(f"Quartis do valor emprestado:\n{quartis_emprestado}")
