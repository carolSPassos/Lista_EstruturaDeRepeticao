#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
#mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Seu nome: ")
senha = input("senha: ")

if senha != nome:
    print("cadastro realizado!")
while senha == nome:
  print("Senha inválida!")
  senha = input("nova senha: ")
  