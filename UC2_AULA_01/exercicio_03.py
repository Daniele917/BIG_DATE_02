# Um estudante fez algumas provas em seu curso e obteve as notas 13, 34,
# 45, 26, 19, 27, 50, 63, 81, 76, 52, 86, 92 e 98. Determine a sua média. Essa medida é
# ideal para representar o seu desempenho? Justifique sua resposta.

import statistics

# Notas do estudante
notas = [13, 34, 45, 26, 19, 27, 50, 63, 81, 76, 52, 86, 92, 98]

# Cálculo da média
media = statistics.mean(notas)

print(f"Média das notas: {media}")


# A média das notas pode não refletir bem o desempenho do estudante devido à grande variação (de 13 a 98). A mediana é uma medida mais precisa em casos com valores extremos
