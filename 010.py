#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))

if n1 > n2:
  for i in range(n2 + 1, n1, 1):
    print(i)
else:
  for x in range(n1 + 1, n2,1):
    print(x)