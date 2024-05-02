x=0
for i in range(1,101):
    numero = int(input())
    if numero > x:
        maior = numero
        posicao = i 
        x = numero
print(maior)
print(posicao)