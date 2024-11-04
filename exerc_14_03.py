import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('\n---- OBTENDO DADOS ----')

endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame ocorrencias
df_ocorrencias = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

# Ajuste do formato da data para incluir o caractere 'm' entre ano e mês
df_ocorrencias['Ano'] = pd.to_datetime(df_ocorrencias['mes_ano'], format='%Ym%m').dt.year
df_ocorrencias = df_ocorrencias[df_ocorrencias['Ano'].isin([2022, 2023, 2024])]

# Supondo que 'lesao_corp_dolosa' e 'lesao_corp_culposa' são as colunas de interesse
# Agrupando por DP
df_lesoes = df_ocorrencias.groupby(['cisp']).agg({
    'lesao_corp_dolosa': 'sum',
    'lesao_corp_culposa': 'sum'
}).reset_index()

# Exibindo a base de dados ocorrencia
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_lesoes.head())

# Criando o array de lesões corporais dolosas
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

# Obtendo os Quartis das lesões corporais dolosas - Método Weibull
q1_lesoes = np.quantile(array_lesoes, 0.25, method='weibull')
q2_lesoes = np.quantile(array_lesoes, 0.50, method='weibull')
q3_lesoes = np.quantile(array_lesoes, 0.75, method='weibull')
iqr_lesoes = q3_lesoes - q1_lesoes

# Identificando os outliers superiores e inferiores das lesões corporais dolosas
limite_superior_lesoes = q3_lesoes + (1.5 * iqr_lesoes)
limite_inferior_lesoes = q1_lesoes - (1.5 * iqr_lesoes)

# Filtrando o DataFrame de lesões corporais dolosas
df_lesoes_outliers_superiores = df_lesoes[df_lesoes['lesao_corp_dolosa'] > limite_superior_lesoes]
df_lesoes_outliers_inferiores = df_lesoes[df_lesoes['lesao_corp_dolosa'] < limite_inferior_lesoes]

# Exibindo os dados sobre lesões corporais dolosas
print("\nOBTENDO INFORMAÇÕES SOBRE AS LESÕES CORPORAIS DOLOSAS")
print("---------------------------------------------------------------------")
print('------------------ Medidas de Tendência Central ---------------------')
print("---------------------------------------------------------------------")
print(f"A média das lesões corporais dolosas é {media_lesoes:.0f}")
print(f"A mediana das lesões corporais dolosas é {mediana_lesoes:.0f}")
print(f"A distância entre a média e a mediana das lesões corporais dolosas é {distancia_lesoes:.2f} %")
print(f"O menor valor das lesões corporais dolosas é {minimo_lesoes:.0f}")
print(f"O maior valor das lesões corporais dolosas é {maximo_lesoes:.0f}")
print(f"A amplitude dos valores das lesões corporais dolosas é {amplitude_lesoes:.0f}")
print(f"O valor do q1 - 25% das lesões corporais dolosas é {q1_lesoes:.0f}")
print(f"O valor do q2 - 50% das lesões corporais dolosas é {q2_lesoes:.0f}")
print(f"O valor do q3 - 75% das lesões corporais dolosas é {q3_lesoes:.0f}")
print(f"O valor do iqr = q3 - q1 das lesões corporais dolosas é {iqr_lesoes:.0f}")
print(f"O limite inferior das lesões corporais dolosas é {limite_inferior_lesoes:.0f}")
print(f"O limite superior das lesões corporais dolosas é {limite_superior_lesoes:.0f}")

print('\n- Verificando a existência de outliers inferiores -')
if len(df_lesoes_outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(df_lesoes_outliers_inferiores)

print('\n- Verificando a existência de outliers superiores -')
if len(df_lesoes_outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(df_lesoes_outliers_superiores)

# Visualizando os dados sobre lesões corporais dolosas
print('\nVISUALIZANDO OS DADOS...')
plt.subplots(2, 2, figsize=(16, 7))
plt.suptitle('Análise dos Dados sobre Lesões Corporais Dolosas', fontsize=20)

# Posição 01: BoxPlot das Lesões Corporais Dolosas
plt.subplot(3, 2, 1)
plt.title('BoxPlot das Lesões Corporais Dolosas')
plt.boxplot(array_lesoes, vert=False, showmeans=True, 
            boxprops=dict(color='salmon'), 
            medianprops=dict(color='purple'))

# Posição 02: Histograma das Lesões Corporais Dolosas
plt.subplot(3, 2, 2)
plt.title('Histograma das Lesões Corporais Dolosas')
plt.hist(array_lesoes, bins=100, edgecolor='black', color='yellow')

# Posição 03: Ranking das DPs com Outliers Superiores
plt.subplot(2, 2, 3)
df_lesoes_outliers_superiores_order = df_lesoes_outliers_superiores.sort_values(by='lesao_corp_dolosa', ascending=True)
plt.title('Ranking das DPs com Outliers Superiores')
plt.barh(df_lesoes_outliers_superiores_order['cisp'].astype(str), 
         df_lesoes_outliers_superiores_order['lesao_corp_dolosa'], 
         color='purple')

# Posição 04: Medidas Descritivas das Lesões Corporais Dolosas
plt.subplot(2, 2, 4)
plt.title('Medidas Descritivas das Lesões Corporais Dolosas')
plt.axis('off')
plt.text(0.1, 0.9, f'Média das Lesões: {media_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.8, f'Mediana das Lesões: {mediana_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.7, f'Distância entre Média e Mediana: {distancia_lesoes:.2f}%', fontsize=12)
plt.text(0.1, 0.6, f'Maior valor das Lesões: {maximo_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.5, f'Menor valor das Lesões: {minimo_lesoes:.0f}', fontsize=12)
plt.text(0.1, 0.4, f'IQR das Lesões: {iqr_lesoes:.2f}', fontsize=12)

# Exibindo o Painel
plt.tight_layout()
plt.show()

# Respostas às perguntas
print(f'\n1. A média confiável por DP é: {media_lesoes:.0f}')
correlacao = df_lesoes['lesao_corp_dolosa'].corr(df_lesoes['lesao_corp_culposa'])
print(f'2. Correlação entre lesões dolosas e culposas: {correlacao:.2f}')
print(f'3. Quantidade mínima de registros nas DPs com menores ocorrências: {minimo_lesoes:.0f}')
print(f'4. Quantidade mínima de registros nas DPs com mais ocorrências: {maximo_lesoes:.0f}')