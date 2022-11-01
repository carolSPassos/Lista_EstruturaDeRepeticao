#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

candidato1 = []
candidato2 = []
candidato3 = []
qtdvoto = []
eleitores = int(input("quantos eleitores? "))

while len(qtdvoto) != eleitores:
  voto = int(input("vota 1,2 ou 3: "))
  qtdvoto.append(voto)
  if voto == 1:
    candidato1.append(voto)
  elif voto == 2:
    candidato2.append(voto)
  elif voto == 3:
    candidato3.append(voto)
  else:
    print('invalido')

qtdDeVotos1 = len(candidato1)
qtdDeVotos2 = len(candidato2)
qtdDeVotos3 = len(candidato3)

print("Candidato 1:", qtdDeVotos1)
print("Candidato 2:", qtdDeVotos2)
print("Candidato 3:", qtdDeVotos3)