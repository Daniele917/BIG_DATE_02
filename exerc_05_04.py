# A Gerente de Recursos Humanos da sua empresa te passou o seguinte arquivo de dados
# funcionarios.csv com as seguintes informações: Nome, Idade, Sexo, Salário e Tempo de Empresa.
# A partir daí, ela disse que precisa criar um processo automatizado, onde seja possível responder (somente
# responder, nada mais) às seguintes perguntas:
# 1. Qual a média salarial?
# 2. Qual a média de idade?
# 3. Qual o maior e menor tempo de casa, bem como a diferença entre eles?
# 4. Qual a média de tempo de casa?
# 5. Qual o funcionário mais novo e mais velho, bem como a diferença de idade entre eles?
# 6. Qual o total de funcionários?
# 7. Qual o nome do funcionário com maior salário?
# 8.Qual o nome do funcionário com maior tempo de casa?

# Esse processo precisa ser automatizado, pois 1 vez por semana, ela precisará apresentar essas informações
# na reunião com a diretoria.



# Instalação das bibliotecas necessárias:
# pip install xlrd           # Para ler arquivos .xls (Excel antigos)
# pip install openpyxl        # Para ler e escrever arquivos .xlsx (Excel modernos)
import pandas as pd

# Importando a Base de Dados
endereco_dados = 'BASES\Funcionarios.csv'
# Criando o DataFrame 
df_funcionarios = pd.read_csv(endereco_dados, sep=',', encoding='iso-8859-1')

# Gerando os Dados Solicitados 
media_salario = df_funcionarios['Salário'].mean(axis=0)
media_idade = df_funcionarios['Idade'].mean(axis=0)
maior_tempo = df_funcionarios['Tempo'].max(axis=0)
menor_tempo = df_funcionarios['Tempo'].min(axis=0)
diferenca_tempo = maior_tempo - menor_tempo
media_tempo = df_funcionarios['Tempo'].mean(axis=0)
func_tempo_velho = df_funcionarios[df_funcionarios['Tempo'] == maior_tempo]['Nome']
func_tempo_novo = df_funcionarios[df_funcionarios['Tempo'] == menor_tempo]['Nome']

# Cálculo do maior e menor salário
maior_salario = df_funcionarios['Salário'].max(axis=0)
menor_salario = df_funcionarios['Salário'].min(axis=0)

# Extraindo os funcionários com maior e menor salário
func_maior_salario = df_funcionarios[df_funcionarios['Salário'] == maior_salario]['Nome']
func_menor_salario = df_funcionarios[df_funcionarios['Salário'] == menor_salario]['Nome']

qtd_func = df_funcionarios['Nome'].count()

# Exibindo os Dados do DataFrame 
print('\n---------- DADOS DOS FUNCIONÁRIOS -----------')
print(df_funcionarios.head())
print('\n----------- DADOS SOLICITADOS ------------')
print(f"O Salário médio da empresa é R$ {media_salario:.2f}")
print(f"A Média das idades dos funcionários é {media_idade:.0f} anos.")
print(f"O Maior tempo de empresa é {maior_tempo} anos.")
print(f"O Menor tempo de empresa é {menor_tempo} anos.")
print(f"A Diferença de tempo de empresa é {diferenca_tempo} anos.")
print(f"A Média de tempo de empresa é {media_tempo:.0f} anos.")
print(f"O(A) Funcionário(a) mais novo(a) na empresa é {func_tempo_novo.to_string(index=False)}")
print(f"O(A) Funcionário(a) mais antigo(a) na empresa é {func_tempo_velho.to_string(index=False)}")
print(f"O(A) Funcionário(a) com maior salário é {func_maior_salario.to_string(index=False)} com R$ {maior_salario:.2f}")
print(f"O(A) Funcionário(a) com menor salário é {func_menor_salario.to_string(index=False)} com R$ {menor_salario:.2f}")
print(f"A Quantidade de funcionários na empresa são {qtd_func}")

