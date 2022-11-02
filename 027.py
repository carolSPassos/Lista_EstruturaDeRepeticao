#Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e 
#a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos

qtdTurmas = int(input("quantas turmas? "))
turmas = []
alunos = 0

while len(turmas) != qtdTurmas:
  alunos = int(input("quantos alunos? "))
  if alunos <= 40:
   turmas.append(alunos)
  else:
    print("o maximo é 40")

print(turmas)

soma = sum(turmas)
mediaDeAlunos = soma / qtdTurmas
print("média de alunos é: %.2f" %mediaDeAlunos)
