i = 0
contador = 0
while i < 6:
  num = float(input())
  if num > 0:
    contador = contador + 1
  i = i + 1
print(f"{contador} valores positivos")