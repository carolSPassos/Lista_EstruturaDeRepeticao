#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
from math import prod
n = int(input("numero: "))

lista1 = []

for i in range(n,0,-1):
  lista1.append(i)
print(lista1)

resultado = prod(lista1)
print("fatorial do número escolhido é: ", resultado)