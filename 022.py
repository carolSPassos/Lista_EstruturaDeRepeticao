#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
n = int(input("numero: "))

if n <= 1:
  print("Inválido!")
elif n == 2:
  print("É primo")
elif n % 2 ==0:
  print("não é primo!")
  for i in range (1,n,1):
    if n % i == 0:
      print("multipo de: ", i)
      i += 1
else:
  for i in range(3,n,2):

    if (n % 1 == 0) and (n % n ==0):
      print("é primo")
    break