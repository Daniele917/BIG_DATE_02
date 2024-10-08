# Segunda parte do exercicio_03.py:
nomes = []
medias = []
resp = "S"

while resp.upper() == "S":  # Ajuste para aceitar "s" ou "S"
    nomes.append(input("Informe o nome do estudante: ").strip())  # Ajuste na ortografia e adição do strip para remover espaços extras
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja Continuar (S/N)? ").strip().upper()  # Melhorado para aceitar "s" ou "S" e eliminar espaços extras

# Exibir o nome e a média de cada estudante
for i in range(len(medias)):
    print(f"{i + 1} - {nomes[i]} - {medias[i]}")  # Usando f-string para formatação e índice começando de 1

# Cálculo das estatísticas da turma
print(f"A média da turma é: {(sum(medias) / len(medias)):.1f}")
print(f"A maior média da turma é: {max(medias)}")
print(f"A menor média da turma é: {min(medias)}")
print(f"A amplitude média da turma é: {max(medias) - min(medias)}")

# Identificando o estudante com a maior nota
indice_maior_nota = medias.index(max(medias))
print(f"O estudante com a maior nota é: {nomes[indice_maior_nota]} com média {medias[indice_maior_nota]}")

# Ordenando e imprimindo as médias
medias.sort()
print("Médias ordenadas:", medias)

