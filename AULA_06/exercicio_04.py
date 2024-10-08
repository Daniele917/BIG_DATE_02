# Eu quero a menor média , maior média , media da , varietação da média para menor, mostre as médias e ordem crescente : 


# Inicializa listas para armazenar nomes e médias
nomes = []
medias = []

# Loop para coletar nomes e médias dos estudantes
resp = "S"
while resp.upper() == "S":
    nomes.append(input("Informe o nome do estudante: "))
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar (S/N)? ").strip().upper()

# Exibe os nomes e as médias inseridas
print("\nNomes dos estudantes:", nomes)
print("Médias dos estudantes:", medias)

# Calcula a menor média, maior média, média da turma e a variação para o menor valor
menor_media = min(medias)
maior_media = max(medias)
media_turma = sum(medias) / len(medias)
variacao_para_menor = media_turma - menor_media

# Determina o nome do estudante com a menor e maior média
indice_menor_media = medias.index(menor_media)
indice_maior_media = medias.index(maior_media)
nome_menor_media = nomes[indice_menor_media]
nome_maior_media = nomes[indice_maior_media]

# Ordena as médias em ordem crescente
medias_ordenadas = sorted(medias)

# Exibe os resultados calculados
print("\nResultados:")
print(f"Menor média: {menor_media} (Estudante: {nome_menor_media})")
print(f"Maior média: {maior_media} (Estudante: {nome_maior_media})")
print(f"Média da turma: {media_turma:.2f}")
print(f"Variação da média da turma para a menor média: {variacao_para_menor:.2f}")
print(f"Médias em ordem crescente: {medias_ordenadas}")
