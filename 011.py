#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("numero 1: "))
n2 = int(input("numero 2: "))

listaDada = []

if n1 > n2:
  for i in range(n2 + 1, n1, 1):
    listaDada.append(i)
else:
  for x in range(n1 + 1, n2,1):
    listaDada.append(x)

soma = sum(listaDada)

print(listaDada)
print("a soma é: ", soma)