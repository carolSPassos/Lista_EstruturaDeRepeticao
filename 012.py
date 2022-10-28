#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual numero ele deseja ver a tabuada.

tabuada = int(input("numero: "))

for i in range(1,11,1):
  resultado = i * tabuada
  print(i,"x",tabuada,"=", resultado)
