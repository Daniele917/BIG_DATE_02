import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados de delegacia
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
df_delegacia = pd.read_csv(endereco_dados, sep=';', encoding='ISO-8859-1')

# Criando o DataFrame com as colunas 'cisp' e 'roubo_veiculo'
df_ocorrencias = df_delegacia[['cisp', 'roubo_veiculo']]

# Agrupando por 'cisp' e somando os valores de 'roubo_veiculo'
df_roubo_veiculo = df_ocorrencias.groupby('cisp', as_index=False)['roubo_veiculo'].sum()

# Verificando as colunas do DataFrame
print("Colunas disponíveis:", df_delegacia.columns)

# Obtenha os dados de roubos de veículos e remova valores NaN se houver
roubos_veiculos = df_delegacia['roubo_veiculo'].dropna()

# Cálculo de medidas descritivas
media_roubos = roubos_veiculos.mean()
mediana_roubos = roubos_veiculos.median()
distancia_media_mediana = media_roubos - mediana_roubos
maior_roubos = roubos_veiculos.max()
menor_roubos = roubos_veiculos.min()
amplitude_roubos = maior_roubos - menor_roubos

# Cálculo dos quartis e IQR
q1_roubos = roubos_veiculos.quantile(0.25)
q2_roubos = mediana_roubos
q3_roubos = roubos_veiculos.quantile(0.75)
iqr_roubos = q3_roubos - q1_roubos

# Exibindo os dados sobre os roubos de veículos
print("\n--------- OBTENDO INFORMAÇÕES SOBRE OS ROUBOS DE VEÍCULOS -----------")
print(f"A média dos roubos de veículos é {media_roubos:.2f}")
print(f"A mediana dos roubos de veículos é {mediana_roubos:.2f}")
print(f"A distância entre a média e a mediana é {distancia_media_mediana:.2f}%")
print(f"O menor valor dos roubos de veículos é {menor_roubos:.2f}")
print(f"O maior valor dos roubos de veículos é {maior_roubos:.2f}")
print(f"A amplitude dos valores dos roubos de veículos é {amplitude_roubos:.2f}")
print(f"O valor do Q1 - 25% dos roubos de veículos é {q1_roubos:.2f}")
print(f"O valor do Q2 - 50% (Mediana) dos roubos de veículos é {q2_roubos:.2f}")
print(f"O valor do Q3 - 75% dos roubos de veículos é {q3_roubos:.2f}")
print(f"O valor do IQR (Q3 - Q1) dos roubos de veículos é {iqr_roubos:.2f}")

# Criando gráficos
plt.figure(figsize=(12, 8))

# Gráfico 1: Boxplot para visualizar a distribuição dos roubos de veículos
plt.subplot(2, 1, 1)
plt.boxplot(roubos_veiculos, vert=False, showmeans=True, patch_artist=True)
plt.title('Distribuição dos Roubos de Veículos')
plt.xlabel('Número de Roubos de Veículos')

# Gráfico 2: Exibição das principais medidas descritivas
plt.subplot(2, 1, 2)
estatisticas = ['Média', 'Mediana', 'Menor', 'Maior', 'Q1', 'Q3', 'IQR']
valores = [media_roubos, mediana_roubos, menor_roubos, maior_roubos, q1_roubos, q3_roubos, iqr_roubos]
plt.bar(estatisticas, valores, color='skyblue')
plt.title('Estatísticas dos Roubos de Veículos')
plt.ylabel('Valores')

plt.tight_layout()
plt.show()
