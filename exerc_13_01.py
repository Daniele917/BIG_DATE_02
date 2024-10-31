import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
dados = pd.read_csv(endereco_dados, sep=';', encoding='iso-8859-1')

# Análise das ocorrências de CVLI
ocorrencias_cvli = dados.groupby('aisp')['cvli'].sum().reset_index()

# Criar a figura e os eixos para os subgráficos
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))

# 1. Gráfico de Boxplot para distribuição de CVLI
ax1.boxplot(dados['cvli'], patch_artist=True)
ax1.set_title('Distribuição de Ocorrências de CVLI')
ax1.set_ylabel('Número de Ocorrências de CVLI')
ax1.set_xticks([1])
ax1.set_xticklabels(['CVLI'])
ax1.grid(axis='y')

# Exibir medidas estatísticas
media_cvli = dados['cvli'].mean()
mediana_cvli = dados['cvli'].median()
quartis = dados['cvli'].quantile([0.25, 0.75])
print(f"Média de CVLI: {media_cvli:.2f}")
print(f"Mediana de CVLI: {mediana_cvli:.2f}")
print(f"Quartis de CVLI: 25%: {quartis[0.25]:.2f}, 75%: {quartis[0.75]:.2f}")

# 2. Gráfico de Barras para os bons com mais ocorrências de CVLI
top_bons = ocorrencias_cvli.nlargest(10, 'cvli')  # Selecionar os 10 BONS com mais ocorrências
ax2.bar(top_bons['aisp'], top_bons['cvli'], color='royalblue')
ax2.set_title('Top 10 BONS com Mais Ocorrências de CVLI')
ax2.set_xlabel('AISP')
ax2.set_ylabel('Número de Ocorrências de CVLI')
ax2.tick_params(axis='x', rotation=45)

# Ajustar layout
plt.tight_layout()
plt.show()
