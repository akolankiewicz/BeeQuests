tempo = int(input())

minutos = tempo/60
horas = minutos/60

#556 segundos
#9min e 16s
#3675
#1h 1min e 15s
horas = tempo//3600
x = tempo % 3600
min = x//60
sobra = x%60


print(f"{horas}:{min}:{sobra}")


 