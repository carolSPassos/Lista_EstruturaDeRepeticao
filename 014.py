#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

quantidade = 10
numerosPedidos = []
numero = 0
while numero < quantidade:
  numero = int(input("Numero: "))
  numerosPedidos.append(numero)

print(numerosPedidos)

soma = sum(numerosPedidos)
pares=[]
impares=[]

for i in numerosPedidos:
  if i % 2 ==0:
    pares.append(i)
  else:
    impares.append(i)

print("Soma: ", soma)
print("pares: ", pares)
print("impares: ", impares)
