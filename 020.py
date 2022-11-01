#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e 
# limitando o fatorial a números inteiros positivos e menores que 16.

from math import prod

n =1

while n > 0 and n < 16: 
  n = int(input("numero: "))
  lista1 = []

  for i in range(n,0,-1):
    lista1.append(i)
  print(lista1)

  resultado = prod(lista1)
  print("fatorial do número escolhido é: ", resultado)
