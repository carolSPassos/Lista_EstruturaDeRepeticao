#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
# Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o 
# total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. 
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.

while True:
    print("---------- LOJA TABAJARA -----------")
    n = 1
    total = 0

    while True:
      preco = float(input(f'Produto: R$ {n} '))
      n += 1
      total += preco
      if preco == 0:
        print(total)
        break
    pagou = float(input("quanto pagou? "))
    troco = pagou - total
    falta = total - pagou
    if pagou > total:
      print(f'Seu troco é:R$ {troco} ')
    elif pagou < total:
      print(f'Falta pagar R$ {falta} ')
    else:
      print("Obrigada!")    