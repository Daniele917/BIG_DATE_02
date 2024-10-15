# Considere a distribuição a seguir relativa a notas de dois alunos de matemática durante determinado semestre:

# notas_aluno_a = [9.5, 9.0, 2.0, 6.0, 6.5, 3.0, 7.0, 2.0]
# notas_aluno_b = [5.0, 5.5, 4.5, 6.0, 5.5, 5.0, 4.5, 4.0]

# a) Calcule as notas médias de cada aluno.
# b) Qual aluno apresentou resultado mais homogêneo? Justifique.

# Código para cálculo das médias e análise de homogeneidade:
import statistics

# Notas dos alunos
notas_aluno_a = [9.5, 9.0, 2.0, 6.0, 6.5, 3.0, 7.0, 2.0]
notas_aluno_b = [5.0, 5.5, 4.5, 6.0, 5.5, 5.0, 4.5, 4.0]

# a) Cálculo das médias
media_a = statistics.mean(notas_aluno_a)
media_b = statistics.mean(notas_aluno_b)

# b) Cálculo do desvio padrão (homogeneidade)
desvio_padrao_a = statistics.stdev(notas_aluno_a)
desvio_padrao_b = statistics.stdev(notas_aluno_b)

print(f"Média do Aluno A: {media_a}")
print(f"Média do Aluno B: {media_b}")
print(f"Desvio Padrão do Aluno A: {desvio_padrao_a}")
print(f"Desvio Padrão do Aluno B: {desvio_padrao_b}")

# Verifica qual aluno apresentou resultado mais homogêneo
if desvio_padrao_a < desvio_padrao_b:
    print("O Aluno A apresentou resultado mais homogêneo.")
else:
    print("O Aluno B apresentou resultado mais homogêneo.")

# a) Cálculo das notas médias de cada aluno:
 
import statistics

# Notas dos alunos
notas_aluno_a = [9.5, 9.0, 2.0, 6.0, 6.5, 3.0, 7.0, 2.0]
notas_aluno_b = [5.0, 5.5, 4.5, 6.0, 5.5, 5.0, 4.5, 4.0]

# Cálculo das médias
media_aluno_a = statistics.mean(notas_aluno_a)
media_aluno_b = statistics.mean(notas_aluno_b)

print(f"Média do Aluno A: {media_aluno_a}")
print(f"Média do Aluno B: {media_aluno_b}")

# b) Análise de homogeneidade (desvio padrão):

# Cálculo do desvio padrão de cada aluno
desvio_padrao_a = statistics.stdev(notas_aluno_a)
desvio_padrao_b = statistics.stdev(notas_aluno_b)

print(f"Desvio padrão do Aluno A: {desvio_padrao_a}")
print(f"Desvio padrão do Aluno B: {desvio_padrao_b}")

# Para resolver essa questão, vamos calcular as médias das notas dos dois alunos e comparar a dispersão dos resultados usando o desvio padrão. O aluno com o menor desvio padrão terá o desempenho mais homogêneo.

### a) Cálculo das notas médias de cada aluno:


import statistics

# Notas dos alunos
notas_aluno_a = [9.5, 9.0, 2.0, 6.0, 6.5, 3.0, 7.0, 2.0]
notas_aluno_b = [5.0, 5.5, 4.5, 6.0, 5.5, 5.0, 4.5, 4.0]

# Cálculo das médias
media_aluno_a = statistics.mean(notas_aluno_a)
media_aluno_b = statistics.mean(notas_aluno_b)

print(f"Média do Aluno A: {media_aluno_a}")
print(f"Média do Aluno B: {media_aluno_b}")


### b) Análise de homogeneidade (desvio padrão):


# Cálculo do desvio padrão de cada aluno
desvio_padrao_a = statistics.stdev(notas_aluno_a)
desvio_padrao_b = statistics.stdev(notas_aluno_b)

print(f"Desvio padrão do Aluno A: {desvio_padrao_a}")
print(f"Desvio padrão do Aluno B: {desvio_padrao_b}")


### Justificativa:

# O aluno com o **menor desvio padrão** possui notas mais próximas da média, ou seja, seu desempenho é mais homogêneo. 



# Resumo dos Resultados Esperados:
#- Aluno A**: Média tende a ser um pouco mais alta, mas notas mais dispersas.
#- Aluno B**: Média pode ser mais baixa, mas notas são mais consistentes, indicando um desvio padrão menor e, portanto, maior homogeneidade no desempenho.

    