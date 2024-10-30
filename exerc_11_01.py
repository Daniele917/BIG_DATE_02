import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados de delegacia
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame df_delegacia
df_delegacia = pd.read_csv(endereco_dados, sep=';', encoding='ISO-8859-1')

# Limpando possíveis aspas nos nomes das colunas
df_delegacia.columns = df_delegacia.columns.str.replace('"', '').str.strip()

# Exibindo a base de dados
print('\n---- EXIBINDO A BASE DE DADOS -----')
print(df_delegacia.head())

# Verificando se a coluna de "roubo_veiculo" existe
if 'roubo_veiculo' not in df_delegacia.columns:
    raise ValueError("A coluna 'roubo_veiculo' não foi encontrada na base de dados.")

# Criando o array de roubos de veículos
array_roubos_veiculos = np.array(df_delegacia['roubo_veiculo'])

# Obtendo a média e mediana
media_roubo_veiculo = np.mean(array_roubos_veiculos)
mediana_roubo_veiculo = np.median(array_roubos_veiculos)

# Obtendo a distância entre a média e a mediana
distancia_roubo_veiculo = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo) * 100

# Obtendo o maior e o menor valor de roubos de veículos
maior_roubo_veiculo = np.max(array_roubos_veiculos)
menor_roubo_veiculo = np.min(array_roubos_veiculos)

# Obtendo a amplitude
amplitude_roubo_veiculo = maior_roubo_veiculo - menor_roubo_veiculo

# Obtendo os Quartis
q1_roubo_veiculo = np.quantile(array_roubos_veiculos, 0.25, method='weibull')
q2_roubo_veiculo = np.quantile(array_roubos_veiculos, 0.50, method='weibull')
q3_roubo_veiculo = np.quantile(array_roubos_veiculos, 0.75, method='weibull')
iqr_roubo_veiculo = q3_roubo_veiculo - q1_roubo_veiculo

# Identificando os outliers
limite_superior_roubo_veiculo = q3_roubo_veiculo + (1.5 * iqr_roubo_veiculo)
limite_inferior_roubo_veiculo = q1_roubo_veiculo - (1.5 * iqr_roubo_veiculo)

# Filtrando os outliers
outliers_superiores = df_delegacia[df_delegacia['roubo_veiculo'] > limite_superior_roubo_veiculo]
outliers_inferiores = df_delegacia[df_delegacia['roubo_veiculo'] < limite_inferior_roubo_veiculo]

# Obtendo as medidas de dispersão
variancia_roubo_veiculo = np.var(array_roubos_veiculos)
desvio_padrao_roubo_veiculo = np.std(array_roubos_veiculos)
coeficiente_var_roubo_veiculo = desvio_padrao_roubo_veiculo / media_roubo_veiculo

# Exibindo os dados sobre roubos de veículos
print('\nOBTENDO INFORMAÇÕES SOBRE ROUBO DE VEÍCULOS')
print('Medidas de Tendência Central')
print(f"\nA média dos roubos de veículos é {media_roubo_veiculo:.2f}")
print(f"A mediana dos roubos de veículos é {mediana_roubo_veiculo:.2f}")
print(f"A distância entre a média e a mediana dos roubos de veículos é {distancia_roubo_veiculo:.2f} %")
print(f"O maior valor de roubos de veículos é {maior_roubo_veiculo:.2f}")
print(f"O menor valor de roubos de veículos é {menor_roubo_veiculo:.2f}")
print(f"A amplitude dos roubos de veículos é {amplitude_roubo_veiculo:.2f}")
print(f"O valor do q1 - 25% de roubos de veículos é {q1_roubo_veiculo:.2f}")
print(f"O valor do q2 - 50% de roubos de veículos é {q2_roubo_veiculo:.2f}")
print(f"O valor do q3 - 75% de roubos de veículos é {q3_roubo_veiculo:.2f}")
print(f"O valor do iqr = q3 - q1 dos roubos de veículos é {iqr_roubo_veiculo:.2f}")
print(f"O limite inferior dos roubos de veículos é {limite_inferior_roubo_veiculo:.2f}")
print(f"O limite superior dos roubos de veículos é {limite_superior_roubo_veiculo:.2f}")
print(f"A variância dos roubos de veículos é {variancia_roubo_veiculo:.2f}")
print(f"O desvio padrão dos roubos de veículos é {desvio_padrao_roubo_veiculo:.2f}")
print(f"O coeficiente de variação dos roubos de veículos é {coeficiente_var_roubo_veiculo:.2f}")

# Verificando a existência de outliers inferiores
print('\n- Verificando a existência de outliers inferiores -')
if len(outliers_inferiores) == 0:
    print("Não existem outliers inferiores")
else:
    print(outliers_inferiores)

# Verificando a existência de outliers superiores
print('\n- Verificando a existência de outliers superiores -')
if len(outliers_superiores) == 0:
    print("Não existem outliers superiores")
else:
    print(outliers_superiores)

# Visualizando os dados
print('\nVISUALIZANDO OS DADOS...')
plt.figure(figsize=(12, 6))
plt.title('Distribuição dos Roubos de Veículos')
plt.hist(array_roubos_veiculos, bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(media_roubo_veiculo, color='red', linestyle='dashed', linewidth=2, label='Média')
plt.axvline(mediana_roubo_veiculo, color='green', linestyle='dashed', linewidth=2, label='Mediana')
plt.axvline(limite_superior_roubo_veiculo, color='orange', linestyle='dashed', linewidth=2, label='Limite Superior')
plt.axvline(limite_inferior_roubo_veiculo, color='orange', linestyle='dashed', linewidth=2, label='Limite Inferior')
plt.xlabel('Número de Roubos de Veículos')
plt.ylabel('Frequência')
plt.legend()
plt.grid()
plt.show()
