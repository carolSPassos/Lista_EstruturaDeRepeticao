#Faça um programa que calcule o mostre a média aritmética de N notas.

notas = []
nota = 0

while nota != 11:
  nota = float(input("Sua nota: "))
  print("fim das notas digite '11' ")
  notas.append(nota)
  if nota == 11:
    notas.pop()
soma = sum(notas)
tamanho = len(notas)
media = soma/tamanho
print(media)