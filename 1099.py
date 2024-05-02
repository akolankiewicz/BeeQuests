a = int(input())
while(a > 0):
   soma = 0
   a1, a2 = map(int, input().split())
   minimo = min(a1, a2)
   maximo = max(a1, a2)
   for i in range(minimo+1,maximo):
      if i % 2 != 0:
        soma += i
   a -= 1
   print(soma)
