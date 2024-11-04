import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

# Carregando os dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

# Somando homicídios dolosos por delegacia
df_hom_doloso = df_ocorrencias[['cisp', 'hom_doloso']]
df_hom_doloso = df_hom_doloso.groupby(['cisp']).sum().reset_index()

# Somando homicídios dolosos e culposos por delegacia
df_hom_doloso_culposo = df_ocorrencias[['cisp', 'hom_doloso', 'hom_culposo']]
df_hom_doloso_culposo = df_hom_doloso_culposo.groupby(['cisp']).sum().reset_index()

# Exibindo uma amostra da base de dados
print('\n---- EXIBINDO A BASE DE DADOS ----')
print(df_hom_doloso.head())

# Criando um array para homicídios dolosos
array_hom_doloso = np.array(df_hom_doloso["hom_doloso"])

# Obtendo média e mediana
media_hom_doloso = np.mean(array_hom_doloso)
mediana_hom_doloso = np.median(array_hom_doloso)

# Calculando distância percentual entre média e mediana
distancia_hom_doloso = abs((media_hom_doloso - mediana_hom_doloso) / mediana_hom_doloso) * 100

# Obtendo valores máximo, mínimo e amplitude
maximo_hom_doloso = np.max(array_hom_doloso)
minimo_hom_doloso = np.min(array_hom_doloso)
amplitude_hom_doloso = maximo_hom_doloso - minimo_hom_doloso

# Obtendo quartis e IQR
q1_hom_doloso = np.quantile(array_hom_doloso, 0.25, method='weibull')
q2_hom_doloso = np.quantile(array_hom_doloso, 0.50, method='weibull')
q3_hom_doloso = np.quantile(array_hom_doloso, 0.75, method='weibull')
iqr_hom_doloso = q3_hom_doloso - q1_hom_doloso

# Identificando outliers
limite_superior_hom_doloso = q3_hom_doloso + (1.5 * iqr_hom_doloso)
limite_inferior_hom_doloso = q1_hom_doloso - (1.5 * iqr_hom_doloso)
df_hom_doloso_outliers_superiores = df_hom_doloso[df_hom_doloso['hom_doloso'] > limite_superior_hom_doloso]
df_hom_doloso_outliers_inferiores = df_hom_doloso[df_hom_doloso['hom_doloso'] < limite_inferior_hom_doloso]

# Medidas de dispersão
variancia_hom_doloso = np.var(array_hom_doloso)
distancia_var_hom_doloso = variancia_hom_doloso / (media_hom_doloso**2)
desvio_padrao_hom_doloso = np.std(array_hom_doloso)
coeficiente_var_hom_doloso = desvio_padrao_hom_doloso / media_hom_doloso

# Correlação entre homicídios dolosos e culposos
correlacao_hom = np.corrcoef(df_hom_doloso_culposo['hom_doloso'], df_hom_doloso_culposo['hom_culposo'])[0, 1]

# Exibindo as informações
print("\n--------- INFORMAÇÕES SOBRE OS HOMICÍDIOS DOLOSOS -----------")
print("---------------------------------------------------------------------")
print(f"A média dos homicídios dolosos é {media_hom_doloso:.0f}")
print(f"A mediana dos homicídios dolosos é {mediana_hom_doloso:.0f}")
print(f"A distância entre a média e a mediana é {distancia_hom_doloso:.2f}%")
print(f"O menor valor é {minimo_hom_doloso:.0f}")
print(f"O maior valor é {maximo_hom_doloso:.0f}")
print(f"A amplitude é {amplitude_hom_doloso:.0f}")
print(f"O valor do q1 (25%) é {q1_hom_doloso:.0f}")
print(f"O valor do q2 (50%) é {q2_hom_doloso:.0f}")
print(f"O valor do q3 (75%) é {q3_hom_doloso:.0f}")
print(f"O IQR é {iqr_hom_doloso:.0f}")
print(f"O limite inferior é {limite_inferior_hom_doloso:.0f}")
print(f"O limite superior é {limite_superior_hom_doloso:.0f}")
print(f"A variância é {variancia_hom_doloso:.0f}")
print(f"O desvio padrão é {desvio_padrao_hom_doloso:.0f}")
print(f"O coeficiente de variação é {coeficiente_var_hom_doloso:.2f}")
print(f"A correlação entre homicídios dolosos e culposos é {correlacao_hom:.2f}")

print('\n- Outliers inferiores -')
if len(df_hom_doloso_outliers_inferiores) == 0:
    print("Não existem outliers inferiores.")
else:
    print(df_hom_doloso_outliers_inferiores)

print('\n- Outliers superiores -')
if len(df_hom_doloso_outliers_superiores) == 0:
    print("Não existem outliers superiores.")
else:
    print(df_hom_doloso_outliers_superiores)

# Visualizando os dados
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2, 2, figsize=(16, 7))
plt.suptitle('Análise dos Dados sobre Homicídios Dolosos')

# posição 01: BoxPlot
plt.subplot(2, 2, 1)
plt.title('BoxPlot dos Homicídios Dolosos')
plt.boxplot(array_hom_doloso, vert=False, showmeans=True,
            boxprops=dict(color='pink'), medianprops=dict(color='blue'),
            whiskerprops=dict(color='blue'), capprops=dict(color='red'),
            meanprops=dict(marker='o', markerfacecolor='purple', markersize=10),
            flierprops=dict(marker='o', markerfacecolor='yellow', markersize=5, alpha=0.5))

# posição 02: Dispersão entre dolosos e culposos
plt.subplot(2, 2, 2)
plt.title('Comparativo Homicídios Dolosos e Culposos')
plt.scatter(df_hom_doloso_culposo['hom_doloso'], df_hom_doloso_culposo['hom_culposo'], color='purple', edgecolor='black', s=150)
plt.xlabel('Homicídio Doloso')
plt.ylabel('Homicídio Culposo')

# posição 03: Ranking das Delegacias
plt.subplot(2, 2, 3)
df_hom_doloso_outliers_superiores_order = df_hom_doloso_outliers_superiores.sort_values(by='hom_doloso', ascending=True)
plt.title('Ranking das Delegacias')
plt.barh(df_hom_doloso_outliers_superiores_order['cisp'].astype(str), df_hom_doloso_outliers_superiores_order['hom_doloso'], color='black')

# posição 04: Medidas Descritivas
plt.subplot(2, 2, 4)
plt.title('Medidas Descritivas dos Homicídios Dolosos')
plt.axis('off')
plt.text(0.1, 0.9, f'Média: {media_hom_doloso:.0f}', fontsize=12)
plt.text(0.1, 0.8, f'Mediana: {mediana_hom_doloso:.0f}', fontsize=12)
plt.text(0.1, 0.7, f'Distância Média-Mediana: {distancia_hom_doloso:.2f}%', fontsize=12)
plt.text(0.1, 0.6, f'Maior valor: {maximo_hom_doloso:.0f}', fontsize=12)
plt.text(0.1, 0.5, f'Menor valor: {minimo_hom_doloso:.0f}', fontsize=12)
plt.text(0.1, 0.4, f'Variância X Média: {distancia_var_hom_doloso:.2f}', fontsize=12)
plt.text(0.1, 0.3, f'Coeficiente de variação: {coeficiente_var_hom_doloso:.2f}', fontsize=12)
plt.text(0.1, 0.2, f'Correlação: {correlacao_hom:.2f}', fontsize=12)

plt.show()
