v1, v2, v3 = map(float,input().split())
if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
    soma = v1 + v2 + v3
    print("Perimetro =", soma)
else:
    x=v1 + v2
    y= v3*x 
    z=y/2
    print("Area =", z) 
