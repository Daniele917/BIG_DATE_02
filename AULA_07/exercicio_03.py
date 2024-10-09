# Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a

# qual coletaram os seguintes dados referentes a cada habitante para serem analisados:

# - sexo (masculino e feminino)
# - cor dos olhos (azuis, verdes ou castanhos)
# - cor dos cabelos (louros, castanhos, pretos)
# - idade
# Faça um programa que determine e escreva:
# a) a maior e a menor idade dos habitantes, assim como a média das idades;
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;


habitantes = []  # Lista para armazenar os dados dos habitantes


print("Digite os dados dos habitantes. Digite 'sair' para encerrar.")  # Coleta de dados

while True:
    sexo = input("Sexo (masculino/feminino): ").strip().lower()
    if sexo == 'sair':
        break
    
    olhos = input("Cor dos olhos (azuis/verdes/castanhos): ").strip().lower()
    cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ").strip().lower()
    
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida, por favor insira um número inteiro.")
        continue
    
     
    habitantes.append({     # Adiciona os dados do habitante na lista
        "sexo": sexo,
        "olhos": olhos,
        "cabelos": cabelos,
        "idade": idade
    })


if habitantes:  # Verifica se a lista de habitantes tem elementos
    
    idades = [hab["idade"] for hab in habitantes]   # a) Encontrar maior, menor idade e calcular a média das idades
    maior_idade = max(idades)
    menor_idade = min(idades)
    media_idades = sum(idades) / len(idades)

    
    mulheres_18_35 = sum(1 for hab in habitantes if hab["sexo"] == "feminino" and 18 <= hab["idade"] <= 35)  # b) Contar mulheres com idade entre 18 e 35 anos, inclusive

    
    olhos_verdes_cabelos_louros = sum(1 for hab in habitantes if hab["olhos"] == "verdes" and hab["cabelos"] == "louros")  #  c)Contar indivíduos com olhos verdes e cabelos louros

    
    print(f"\nA maior idade é: {maior_idade} anos")   # Resultados
    print(f"A menor idade é: {menor_idade} anos")
    print(f"A média das idades é: {media_idades:.2f} anos")
    print(f"\nQuantidade de mulheres com idade entre 18 e 35 anos: {mulheres_18_35}")
    print(f"Quantidade de indivíduos com olhos verdes e cabelos louros: {olhos_verdes_cabelos_louros}")
else:
    print("\nNenhum dado foi registrado.")
