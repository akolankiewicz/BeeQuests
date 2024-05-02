entrada = float(input())
entradatratada = entrada.split()
x1 = entrada[0] #n1
x3 = entrada[2] #/
x5 = entrada[4] #d1
x7 = entrada[6] #sinal
x9 = entrada[8] #n2
x11 = entrada[10] #/
x13 = entrada[12] #d2

n1 = x1,x3,x5
n2 = x9,x11,x13
sinal = x7

if sinal == "+":
   resultado =  x1*x13 + x5*x9 
   res = resultado / x13*x5

   print(res)
    

