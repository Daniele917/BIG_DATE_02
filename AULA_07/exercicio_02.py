# O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um
# programa que armazene em um vetor um conjunto indeterminado de temperaturas, ao final
# informe a menor, a maior e a média das temperaturas.


temperaturas = []  # Lista para armazenar as temperaturas


print("Digite as temperaturas registradas. Digite 'sair' para encerrar.")  # Entrada de dados: enquanto o usuário não digitar "sair", as temperaturas são adicionadas à lista.

while True:
    entrada = input("Temperatura: ")
    if entrada.lower() == 'sair':
        break
    try:
        temperatura = float(entrada)
        temperaturas.append(temperatura)
    except ValueError:
        print("Por favor, digite um número válido ou 'sair' para encerrar.")


if temperaturas:  # Verifica se a lista de temperaturas tem elementos
    
    menor_temperatura = min(temperaturas)  # Cálculos
    maior_temperatura = max(temperaturas)
    media_temperatura = sum(temperaturas) / len(temperaturas)

    
    print(f"\nMenor temperatura: {menor_temperatura:.2f}°C")   # Resultados
    print(f"Maior temperatura: {maior_temperatura:.2f}°C")
    print(f"Média das temperaturas: {media_temperatura:.2f}°C")
else:
    print("\nNenhuma temperatura foi registrada.")
