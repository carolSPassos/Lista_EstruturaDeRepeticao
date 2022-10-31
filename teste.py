testes = []
n = 0
for n in range(5):
  for i in range(n,0,-1):
    n = int(input("as: "))
    testes.append(n)
n+=1
resultado = prod(testes)