#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
# A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

paisA = 80000
crescimentoA = 1.03
paisB = 200000
crescimentoB =  1.015
anos = 0

popAtual_a = paisA * crescimentoA
popAtual_b = paisB * crescimentoB

while popAtual_a < popAtual_b:
  popAtual_a *= crescimentoA
  popAtual_b *= crescimentoB
  anos += 1
else:
  print("população de A: %.2f" %popAtual_a)
  print("população de B: %.2f" %popAtual_b)
  print(anos, " anos")
