#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Nome: ")

while len(nome) < 3:
  print("nome inválido")
  nome = input("Seu nome: ")
else:
  nome == True

idade = int(input("Idade: "))

while (idade < 0) or (idade > 150):
  print("idade inválida!")
  idade = int(input("Sua idade real: "))
else:
  idade == True

salario = float(input("Salário: "))

while (salario < 0.0):
  print("inválido!")
  salario = float(input("salário: "))
else:
  salario == True


sexo = str(input("Sexo: F ou M "))

while (sexo.lower() != "f".lower()) and (sexo.lower() != "m".lower()):
  print("Responda com F ou M")  
  sexo = input("sexo: ")
else:  sexo == True

estadoCivil = str(input("Estado civil: (s),(c),(v),(d) "))

while (estadoCivil.lower() != "s".lower()) and (estadoCivil.lower() != "c".lower()) and (estadoCivil.lower() != "d".lower()) and (estadoCivil.lower() != "v".lower()):
  print("responda corretamente!")
  estadoCivil = input("estado civil: ")
else:
  estadoCivil == True

print("CADASTRO REALIZADO!!!")