#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.

n = 1

while n <=20:
  print(n)
  n += 1

for x in range(21):
  if x > 0 and x < 21 :
    print(x, end = " ")
