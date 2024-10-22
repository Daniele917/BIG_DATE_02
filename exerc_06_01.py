# Primeiro, instale as bibliotecas necessárias
# pip install xlrd           # Para ler arquivos .xls (Excel antigos)
# pip install openpyxl        # Para ler e escrever arquivos .xlsx (Excel modernos)

# Primeiro, instale as bibliotecas necessárias:
# pip install pandas

# exerc_05_03.py -( ATUALIZADO parte 1):

import pandas as pd

# Caminho do arquivo CSV (substitua com o caminho correto caso necessário)
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'

# Tentar carregar o arquivo CSV com tratamento de erro
try:
    # Carregar o arquivo CSV com separador e encoding corretos
    df_ocorrencias = pd.read_csv(endereco_dados , sep=';',encoding='iso-8859-1')

    # Exibir as primeiras linhas para verificar a estrutura dos dados
    print('-----Primeiras Linhas da Base de Dados------')
    print(df_ocorrencias.head())

    # Verificar se as colunas 'ano' e 'hom_doloso' existem na base
    if 'ano' in df_ocorrencias.columns and 'hom_doloso' in df_ocorrencias.columns:
        # Agrupar os dados por ano e somar os homicídios dolosos
        df_homicidios_ano = df_ocorrencias[['ano', 'hom_doloso']].groupby('ano').sum().reset_index()

        # Exibir os dados agregados de homicídios dolosos por ano
        print('\n-----Homicídios Dolosos por Ano-----')
        print(df_homicidios_ano)

        # Exibir as primeiras 5 linhas dos homicídios dolosos por ano
        print('\n-----Resumo dos Homicídios Dolosos por Ano-----')
        print(df_homicidios_ano.head())
    else:
        print("Erro: As colunas 'ano' e/ou 'hom_doloso' não foram encontradas na base de dados.")

except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho e tente novamente.")
except pd.errors.ParserError:
    print("Erro: Problema ao ler o arquivo CSV. Verifique o formato e o separador.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


