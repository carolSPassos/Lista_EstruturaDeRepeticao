#Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e 
# o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

quantidade = int(input("quantos cds? "))
cd = 0
valor = []

while cd < quantidade:
  precoIndividual = float(input("qual o valor? "))
  valor.append(precoIndividual)
  cd += 1
precoTotal = sum(valor)
print(f'O preço a pagar por {quantidade} cds é de R${precoTotal}  ')
