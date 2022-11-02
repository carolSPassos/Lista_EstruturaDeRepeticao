#Faça um programa que, dado um conjunto de N números, 
#determine o menor valor, o maior valor e a soma dos valores.
#from math import *
numeros = []
n = -1
while n != 0:
  n = int(input("numero e 0 para parar: "))
  numeros.append(n)
numeros.pop()
print(numeros)
menorValor = min(numeros,default=0)
maiorValor = max(numeros,default=0)
somaDosValores = sum(numeros)

print(f'menor valor = {menorValor} maior valor = {maiorValor} e soma dos valores {somaDosValores}')
