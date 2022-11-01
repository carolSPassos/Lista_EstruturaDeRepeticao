n = int(input("numero: "))

if n <= 1:
  print("Inválido!")
elif n == 2:
  print("É primo")
elif n % 2 ==0:
  print("não é primo!")
else:
  for i in range(3,n,2):
    if (n % 1 == 0) and (n % n ==0):
      print("é primo")
    break

