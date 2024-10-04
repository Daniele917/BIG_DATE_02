# Faça um programa que leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A fórmula de conversão é: F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em Celsius;




# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

# Leitura da temperatura em Celsius
celsius = float(input("Digite a temperatura em graus Celsius: "))

# Conversão
fahrenheit = celsius_para_fahrenheit(celsius)

# Exibição do resultado
print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}")