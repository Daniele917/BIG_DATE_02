# Escreva um programa que, dados 2 números inteiros (n1 e n2), diga se eles são iguais ou diferentes.


def verificar_iguais(n1, n2):
    if n1 == n2:
        return "Iguais"
    else:
        return "Diferentes"


n1 = int(input("Digite o primeiro número (n1): "))
n2 = int(input("Digite o segundo número (n2): "))

resultado = verificar_iguais(n1, n2)

print(f"Os números {n1} e {n2} são: {resultado}.")
