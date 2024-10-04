# Crie um programa que divida o n1 pelo n2:

try:
    n1 = int(input("Informe o primeiro valor:"))
    n2 = int(input("Informe o segundo valor:"))
except ValueError:
   print("Verifique a entrada de dados:")
else:
    try:
      result = n1 / n2
    except ZeroDivisionError:
        print(" Não é posssivel dividir por zero.")
    else:
        print(result)



