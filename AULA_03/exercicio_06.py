# Utilizando a estrutura do programa anterior, some os dois valores se forem diferentes e multiplique-os se forem iguais.

def verificar_e_calcular(n1, n2):
    if n1 == n2:
        resultado = n1 * n2
        return "Iguais", resultado
    else:
        resultado = n1 + n2
        return "Diferentes", resultado

n1 = int(input("Digite o primeiro número (n1): "))
n2 = int(input("Digite o segundo número (n2): "))


resultado, valor_calculo = verificar_e_calcular(n1, n2)


print(f"Os números {n1} e {n2} são: {resultado}. O resultado do cálculo é: {valor_calculo}.")

