# Faça um programa que leia duas séries com 10 números inteiros cada e ao final mostre a soma, a subtração, a multiplicação e a divisão entre elas.
# (feito pelo professor- exerc_02_03.py):
import pandas as pd
num_01 = pd.Series([100,50,40,30,80,10,15,70,50,50])
num_02 = pd.Series([80,10,90,50,90,100,150,40,10, 50])
print(num_01 + num_02)
print(num_01 - num_02)
print(num_01 * num_02)
print(num_01 / num_02)


