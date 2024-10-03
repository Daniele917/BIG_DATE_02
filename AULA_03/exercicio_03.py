# Informe o sexo (feminino ou masculino) e depois exiba o peso ideal com base nisso :

h = float(input("Informe a altura: "))
sexo = input("Informe o sexo (M para masculino, F para feminino): ")

if sexo == 'M':
    m = (72.7 * h) - 58
    print(f"O peso ideal para homens é {m:.2f} kg")
elif sexo == 'F':
    f = (62.1 * h) - 44.7
    print(f"O peso ideal para mulheres é {f:.2f} kg")
else:
    print("Sexo inválido. Informe 'M' para masculino ou 'F' para feminino.")
