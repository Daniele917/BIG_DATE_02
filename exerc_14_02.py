import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

# Endereço dos dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')
df_lesoes = df_ocorrencias[['cisp', 'lesao_corp_dolosa']]
df_lesoes = df_lesoes.groupby(['cisp']).sum(['lesao_corp_dolosa']).reset_index()

# Exibindo a base de dados de lesões corporais dolosas
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesoes.head())

# Criando o array das lesões corporais dolosas
array_lesoes = np.array(df_lesoes["lesao_corp_dolosa"])

# Obtendo a média das lesões corporais dolosas
media_lesoes = np.mean(array_lesoes)

# Obtendo a mediana das lesões corporais dolosas
mediana_lesoes = np.median(array_lesoes)

# Obtendo a distância entre a média e a mediana das lesões corporais dolosas
distancia_lesoes = abs((media_lesoes - mediana_lesoes) / mediana_lesoes) * 100

# Obtendo o máximo e o mínimo das lesões corporais dolosas
maximo_lesoes = np.max(array_lesoes)
minimo_lesoes = np.min(array_lesoes)

# Obtendo a amplitude das lesões corporais dolosas
amplitude_lesoes = maximo_lesoes - minimo_lesoes

# Obtendo os Quartis das lesões corporais dolosas
q1_lesoes = np.quantile(array_lesoes, 0.25, method='weibull')
q2_lesoes = np.quantile(array_lesoes, 0.50, method='weibull')
q3_lesoes = np.quantile(array_lesoes, 0.75, method='weibull')
iqr_lesoes = q3_lesoes - q1_lesoes

# Identificando os outliers superiores e inferiores das lesões corporais dolosas
limite_superior_lesoes = q3_lesoes + (1.5 * iqr_lesoes)
limite_inferior_lesoes = q1_lesoes - (1.5 * iqr_lesoes)

# Filtrando o DataFrame das lesões corporais dolosas
df_outliers_superiores = df_lesoes[df_lesoes['lesao_corp_dolosa'] > limite_superior_lesoes]
df_outliers_inferiores = df_lesoes[df_lesoes['lesao_corp_dolosa'] < limite_inferior_lesoes]

# Obtendo as medidas de dispersão das lesões corporais dolosas
variancia_lesoes = np.var(array_lesoes)
distancia_var_lesoes = variancia_lesoes / (media_lesoes ** 2)
desvio_padrao_lesoes = np.std(array_lesoes)
coeficiente_var_lesoes = desvio_padrao_lesoes / media_lesoes

# Exibindo os dados sobre as lesões corporais dolosas
print("\nOBTENDO INFORMAÇÕES SOBRE AS LESÕES CORPORAIS DOLOSAS")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das lesões corporais dolosas é {media_lesoes:.0f}")
print(f"A mediana das lesões corporais dolosas é {mediana_lesoes:.0f}")
print(f"A distância entre a média e a mediana das lesões é {distancia_lesoes:.2f} %")
print(f"O menor valor das lesões corporais dolosas é {minimo_lesoes:.0f}")
print(f"O maior valor das lesões corporais dolosas é {maximo_lesoes:.0f}")
print(f"A amplitude dos valores das lesões corporais dolosas é {amplitude_lesoes:.0f}")
print(f"O valor do q1 - 25% das lesões é {q1_lesoes:.0f}")
print(f"O valor do q2 - 50% das lesões é {q2_lesoes:.0f}")
print(f"O valor do q3 - 75% das lesões é {q3_lesoes:.0f}")
print(f"O valor do iqr = q3 - q1 das lesões é {iqr_lesoes:.0f}")
print(f"O limite inferior das lesões é {limite_inferior_lesoes:.0f}")
print(f"O limite superior das lesões é {limite_superior_lesoes:.0f}")
print(f"A variância das lesões é {variancia_lesoes:.0f}")
print(f"A distância da variância X média das lesões é {distancia_var_lesoes:.0f}")
print(f"O desvio padrão das lesões é {desvio_padrao_lesoes:.0f}")
print(f"O coeficiente de variação das lesões é {coeficiente_var_lesoes:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_outliers_superiores)

# Visualizando os dados sobre as lesões corporais dolosas
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2, 2, figsize=(16, 7))
plt.suptitle('Análise dos Dados sobre Lesões Corporais Dolosas', fontsize=20)

# Posição 01: BoxPlot das Lesões Corporais Dolosas
plt.subplot(2, 2, 1)
plt.title('BoxPlot das Lesões Corporais Dolosas')
plt.boxplot(array_lesoes, vert=False, showmeans=True,
            boxprops=dict(color='salmon'),
            medianprops=dict(color='purple'))

# Posição 02: Histograma das Lesões Corporais Dolosas
plt.subplot(2, 2, 2)
plt.title('Histograma das Lesões Corporais Dolosas')
plt.hist(array_lesoes, bins=100, edgecolor='black', color='yellow')

# Posição 03: Ranking das Delegacias com Outliers Superiores
plt.subplot(2, 2, 3)
df_outliers_superiores_order = df_outliers_superiores.sort_values(by='lesao_corp_dolosa', ascending=True)
plt.title('Ranking das Delegacias com Outliers Superiores')
plt.barh(df_outliers_superiores_order['cisp'].astype(str),
         df_outliers_superiores_order['lesao_corp_dolosa'],
         color='purple')

# Posição 04: Medidas Descritivas das Lesões Corporais Dolosas
plt.subplot(2, 2, 4)
plt.title('Medidas Descritivas das Lesões Corporais Dolosas')
plt.axis('off')
plt.text(0.1, 0.9, f'Média das Lesões Dolosas: {media_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.8, f'Mediana das Lesões Dolosas: {mediana_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.7, f'Distância entre Média e Mediana das Lesões: {distancia_lesoes:.2f}%', fontsize=12)
plt.text(0.1, 0.6, f'Maior valor das Lesões: {maximo_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.5, f'Menor valor das Lesões: {minimo_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.4, f'Distância entre a Variância e Média das Lesões: {distancia_var_lesoes:.2f}', fontsize=12)
plt.text(0.1, 0.3, f'Coeficiente de variação das Lesões: {coeficiente_var_lesoes:.2f}', fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()
