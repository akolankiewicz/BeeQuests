salario = float(input())
if salario <= 400.00:
    a = salario*1.15
    b = a - salario
    print(f"Novo salario: {a:.2f}")
    print(f"Reajuste ganho: {b:.2f}")
    print("Em percentual: 15 %")
if 400.01<=salario<=800.00:
    c = salario*1.12
    d = c - salario
    print(f"Novo salario: {c:.2f}")
    print(f"Reajuste ganho: {d:.2f}")
    print("Em percentual: 12 %")
if 800.01<=salario<=1200.00:
    e = salario*1.1
    f = e - salario
    print(f"Novo salario: {e:.2f}")
    print(f"Reajuste ganho: {f:.2f}")
    print("Em percentual: 10 %")
if 1200.01<=salario<=2000.00:
    g = salario*1.07
    h = g - salario
    print(f"Novo salario: {g:.2f}")
    print(f"Reajuste ganho: {h:.2f}")
    print("Em percentual: 7 %")
if salario>2000.00:
    i = salario*1.04
    j = i - salario 
    print(f"Novo salario: {i:.2f}")
    print(f"Reajuste ganho: {j:.2f}")
    print("Em percentual: 4 %")

