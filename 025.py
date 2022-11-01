#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia 
# entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada

idades = []
idade = 0

while idade != '150':
  print("para sair digite '150'")
  idade = int(input("idade: "))
  idades.append(idade)
  print(idades)
  if idade == 150:
    idades.pop()    
    break
somaDasIdades = sum(idades)
qtdDePessoas = len(idades)
mediaDasIdades = (somaDasIdades / qtdDePessoas)

if (mediaDasIdades >= 0) and (mediaDasIdades <= 25):
   print("turma jovem, média de idade de:",mediaDasIdades)
elif (mediaDasIdades >= 26) and (mediaDasIdades <= 60):
  print("turma adulta, média de idade de:", mediaDasIdades)
else:
  print("turma idosa, média de idade de:", mediaDasIdades)