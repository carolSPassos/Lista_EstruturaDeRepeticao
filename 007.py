#Faça um programa que leia 5 números e informe o maior número.


numerosDitos = []
for n in range(5):
  n = int(input("um numero: "))   
  numerosDitos.append(n)
print(numerosDitos)
print("maior número é: ", max(numerosDitos))