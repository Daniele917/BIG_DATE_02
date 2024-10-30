import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('---- OBTENDO DADOS ----')

# Importando a base de dados de delegacia
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Criando o DataFrame df_delegacia
df_delegacia = pd.read_csv(endereco_dados, sep=';', encoding='ISO-8859-1')

# Verificando as colunas do DataFrame
print("Colunas disponíveis:", df_delegacia.columns)

# Exemplo de uso de uma coluna que representa tipos de crimes
# Aqui, estou considerando 'hom_doloso' como um exemplo de tipo de crime
tipos_crimes = ['hom_doloso', 'estupro', 'latrocinio']  # Coloque os tipos de crimes que você deseja analisar

# Obter as ocorrências para os tipos de crimes selecionados
ocorrencias = [df_delegacia[crime].sum() for crime in tipos_crimes]  # Soma as ocorrências para cada tipo de crime

# Verificando se as variáveis foram definidas corretamente
print("Tipos de Crimes:", tipos_crimes)
print("Ocorrências:", ocorrencias)

# Cálculo de medidas descritivas
media_ocorrencias = np.mean(ocorrencias)
mediana_ocorrencias = np.median(ocorrencias)
maior_ocorrencias = np.max(ocorrencias)
menor_ocorrencias = np.min(ocorrencias)
variancia_ocorrencias = np.var(ocorrencias)

# Previne divisão por zero ao calcular o coeficiente de variação
if media_ocorrencias != 0:
    coeficiente_var_ocorrencias = (np.std(ocorrencias) / media_ocorrencias) * 100
else:
    coeficiente_var_ocorrencias = np.nan  # Ou 0, dependendo do que preferir

# Criando gráfico de colunas
plt.figure(figsize=(12, 8))

# Posição 1: Gráfico de Ocorrências por Tipo de Crime
plt.subplot(2, 2, 1)
plt.bar(tipos_crimes, ocorrencias, color='skyblue')
plt.title('Ocorrências por Tipo de Crime')
plt.xlabel('Tipos de Crime')
plt.ylabel('Número de Ocorrências')
plt.xticks(rotation=45)

# Posição 2: Gráfico de Medidas Descritivas
plt.subplot(2, 2, 2)
plt.title('Medidas Descritivas das Ocorrências')
plt.axis('off')
plt.text(0.1, 0.9, f'Média de Ocorrências: {media_ocorrencias:.2f}', fontsize=12)
plt.text(0.1, 0.8, f'Mediana de Ocorrências: {mediana_ocorrencias:.2f}', fontsize=12)
plt.text(0.1, 0.7, f'Maior Número de Ocorrências: {maior_ocorrencias:.2f}', fontsize=12)
plt.text(0.1, 0.6, f'Menor Número de Ocorrências: {menor_ocorrencias:.2f}', fontsize=12)
plt.text(0.1, 0.5, f'Variância: {variancia_ocorrencias:.2f}', fontsize=12)
plt.text(0.1, 0.4, f'Coeficiente de Variação: {coeficiente_var_ocorrencias:.2f}%', fontsize=12)

# Ajuste do layout
plt.tight_layout()
plt.show()
