#Faça um programa que leia 5 números e informe a soma e a média dos números.

listaDeNumeros = []

for n in range(5):
  n = int(input("número: "))
  listaDeNumeros.append(n)

soma = sum(listaDeNumeros)
media = soma / (len(listaDeNumeros))

print("a soma da lista: ",soma, "E a média é: ", media)