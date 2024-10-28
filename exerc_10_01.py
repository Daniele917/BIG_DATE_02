import pandas as pd
import numpy as np

print('---- OBTENDO DADOS ----')

# Importando a base de dados financeira.csv
endereco_dados = 'BASES\Financeira.csv'

# Criando o DataFrame financeira
df_financeira = pd.read_csv(endereco_dados,sep=',',encoding='iso-8859-1')

# Exibindo a base de dados financeira
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_financeira.head())

# Criando o array da renda e do valor emprestado
# Os arrays são estruturas de dados que armazenam uma coleção de dados e computacionalmente mais eficiente para cálculos estatísticos. Faz parte da biblioteca numpy.
array_financeira_renda = np.array(df_financeira["Renda"])
array_financeira_Vlr_emprestado = np.array(df_financeira["Vlr_emprestado"])

# Obtendo a média da renda e do valor emprestado
# Se a média for maior que 25% em relação a mediana, a distribuição será assimétrica, podendo existir outliers. Caso contrário a distribuição será simétrica.
media_renda = np.mean(array_financeira_renda)
media_Vlr_emprestado = np.mean(array_financeira_Vlr_emprestado)

# Obtendo a mediana da renda e do valor emprestado
mediana_renda = np.median(array_financeira_renda)
mediana_Vlr_emprestado = np.median(array_financeira_Vlr_emprestado)

# Obtendo a distância da renda e do valor emprestado
distancia_renda = abs((media_renda - mediana_renda) / mediana_renda) * 100
distancia_Vlr_emprestado = abs((media_Vlr_emprestado - mediana_Vlr_emprestado) / mediana_Vlr_emprestado) * 100

# Obtendo o maior e o menor valor da renda e do valor emprestado
maior_renda = np.max(array_financeira_renda)
maior_Vlr_emprestado = np.max(array_financeira_Vlr_emprestado)
menor_renda = np.min(array_financeira_renda)
menor_Vlr_emprestado = np.min(array_financeira_Vlr_emprestado)

# Obtendo a amplitude da renda e do valor emprestado
amplitude_renda = maior_renda - menor_renda
amplitude_Vlr_emprestado = maior_Vlr_emprestado - menor_Vlr_emprestado

# Obtendo os Quartis da renda e do valor emprestado - Método weibull
q1_renda = np.quantile(array_financeira_renda, 0.25, method='weibull')
q2_renda = np.quantile(array_financeira_renda, 0.50, method='weibull')
q3_renda = np.quantile(array_financeira_renda, 0.75, method='weibull')
iqr_renda = q3_renda - q1_renda

q1_Vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.25, method='weibull')
q2_Vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.50, method='weibull')
q3_Vlr_emprestado = np.quantile(array_financeira_Vlr_emprestado, 0.75, method='weibull')
iqr_Vlr_emprestado = q3_Vlr_emprestado - q1_Vlr_emprestado

# Identificando os outliers superiores e inferiores da renda e do valor emprestado
limite_superior_renda = q3_renda + (1.5 * iqr_renda)
limite_inferior_renda = q1_renda - (1.5 * iqr_renda)

limite_superior_Vlr_emprestado = q3_Vlr_emprestado + (1.5 * iqr_Vlr_emprestado)
limite_inferior_Vlr_emprestado = q1_Vlr_emprestado - (1.5 * iqr_Vlr_emprestado)

# Filtrando o DataFrame financeira
df_financeira_renda_outliers_superiores = df_financeira[df_financeira['Renda'] > limite_superior_renda]
df_financeira_renda_outliers_inferiores = df_financeira[df_financeira['Renda'] < limite_inferior_renda]

df_financeira_Vlr_emprestado_outliers_superiores = df_financeira[df_financeira['Vlr_emprestado'] > limite_superior_Vlr_emprestado]
df_financeira_Vlr_emprestado_outliers_inferiores = df_financeira[df_financeira['Vlr_emprestado'] < limite_inferior_Vlr_emprestado]

# Obtendo as medidas de dispersão da renda e do valor emprestado
variancia_renda = np.var(array_financeira_renda)
distancia_var_renda = variancia_renda / (media_renda**2)
desvio_padrao_renda = np.std(array_financeira_renda)
coeficiente_var_renda = desvio_padrao_renda / media_renda

# Obtendo as medidas de dispersão do valor emprestado
variancia_Vlr_emprestado = np.var(array_financeira_Vlr_emprestado)
distancia_var_Vlr_emprestado = variancia_Vlr_emprestado / (media_Vlr_emprestado**2)
desvio_padrao_Vlr_emprestado = np.std(array_financeira_Vlr_emprestado)
coeficiente_var_Vlr_emprestado = desvio_padrao_Vlr_emprestado / media_Vlr_emprestado

# Exibindo os dados sobre a renda
print('\nOBTENDO INFORMAÇÕES SOBRE RENDA')
print('Medidas de Tendência Central')
print(f"\nA média das rendas dos clientes é R$ {media_renda:.2f}")
print(f"A mediana das rendas dos clientes é R$ {mediana_renda:.2f}")
print(f"A distância entre a média e a mediana das rendas dos clientes é  {distancia_renda:.2f} %")
print(f"O maior valor das rendas dos clientes é R$ {maior_renda:.2f}")
print(f"O menor valor das rendas dos clientes é R$ {menor_renda:.2f}")
print(f"A amplitude das rendas dos clientes é R$ {amplitude_renda:.2f}")
print(f"O valor do q1 - 25% da renda é R$ {q1_renda:.2f}")
print(f"O valor do q2 - 50% da renda é R$ {q2_renda:.2f}")
print(f"O valor do q3 - 75% da renda é R$ {q3_renda:.2f}")
print(f"O valor do iqr = q3 - q1 da renda é R$ {iqr_renda:.2f}")
print(f"O limite inferior da renda é R$ {limite_inferior_renda:.2f}")
print(f"O limite superior da renda é R$ {limite_superior_renda:.2f}")

print(f"A variância das rendas dos clientes é R$ {variancia_renda:.2f}")
print(f"A distância da variância x rendas dos clientes é R$ {distancia_var_renda:.2f}")
print(f"O desvio padrão das rendas dos clientes é R$ {desvio_padrao_renda:.2f}")
print(f"O coeficiente de variação das rendas dos clientes é R$ {coeficiente_var_renda:.2f}")

print(f"O limite superior do valor emprestado é R$ {limite_superior_Vlr_emprestado:.2f}")
print(f"A variância dos valores emprestados é R$ {variancia_Vlr_emprestado:.2f}")
print(f"A distância da variância x valor emprestado é R$ {distancia_Vlr_emprestado:.2f}")
print(f"O desvio padrão dos valores emprestados é R$ {desvio_padrao_Vlr_emprestado:.2f}")
print(f"O coeficiente de variação dos valores emprestados é R$ {coeficiente_var_Vlr_emprestado:.2f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_financeira_renda_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_renda_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_financeira_renda_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_renda_outliers_superiores)

# Exibindo os dados sobre o valor emprestado
print('\nOBTENDO INFORMAÇÕES SOBRE EMPRÉSTIMO')
print('Medidas de Tendência Central')
print(f"\nA média dos empréstimos dos clientes é R$ {media_Vlr_emprestado:.2f}")
print(f"A mediana dos empréstimos dos clientes é R$ {mediana_Vlr_emprestado:.2f}")
print(f"A distância entre a média e a mediana dos empréstimos dos clientes é {distancia_Vlr_emprestado:.2f} %")
print(f"O maior valor dos empréstimos dos clientes é R$ {maior_Vlr_emprestado:.2f}")
print(f"O menor valor dos empréstimos dos clientes é R$ {menor_Vlr_emprestado:.2f}")
print(f"A amplitude dos empréstimos dos clientes é R$ {amplitude_Vlr_emprestado:.2f}")
print(f"O valor do q1 - 25% do empréstimo é R$ {q1_Vlr_emprestado:.2f}")
print(f"O valor do q2 - 50% da empréstimo é R$ {q2_Vlr_emprestado:.2f}")
print(f"O valor do q3 - 75% da empréstimo é R$ {q3_Vlr_emprestado:.2f}")
print(f"O valor do iqr = q3 - q1 da empréstimo é R$ {iqr_Vlr_emprestado:.2f}")
print(f"O limite inferior da empréstimo é R$ {limite_inferior_Vlr_emprestado:.2f}")
print(f"O limite superior da empréstimo é R$ {limite_superior_Vlr_emprestado:.2f}")
print('\n- Verificando a existência de outliers inferiores -')
if len(df_financeira_Vlr_emprestado_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_financeira_Vlr_emprestado_outliers_inferiores)
print('\n- Verificando a existência de outliers superiores -')
if len(df_financeira_Vlr_emprestado_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_financeira_Vlr_emprestado_outliers_superiores)



