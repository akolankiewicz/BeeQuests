a = 1
while(a > 0):
   soma = 0
   a1, a2 = map(int, input().split())
   minimo = min(a1, a2)
   maximo = max(a1, a2)
   for i in range(minimo,maximo+1):
      soma += i
print(soma)