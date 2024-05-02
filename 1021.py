numero = float(input())

qntd100 = numero // 100
sobra76 = numero % 100
qntd50 = sobra76//50
sobra26 = sobra76 % 50
qntd20 = sobra26 // 20
sobra6 = sobra26 % 20 
qntd10 = sobra6 // 10
sobra262 = sobra6 % 10
qntd5 = sobra262 //5
sobra = sobra262 % 5
qntd2 = sobra // 2
sobra2 = sobra % 2



qntd1 = sobra2//1
sobraA = sobra2%1
qntd05 = sobraA//0.5
sobraB = sobraA%0.5
qntd025 = sobraB//0.25
sobraC = sobraB%0.25
qntd010 = sobraC//0.10
sobraD = sobraC%0.10
qntd005 = sobraD//0.05
sobraE = sobraD%0.05
qntd001 = sobraE*100





print("NOTAS:")
print(f"{qntd100:.0f} nota(s) de R$ 100.00")
print(f"{qntd50:.0f} nota(s) de R$ 50.00")
print(f"{qntd20:.0f} nota(s) de R$ 20.00")
print(f"{qntd10:.0f} nota(s) de R$ 10.00")
print(f"{qntd5:.0f} nota(s) de R$ 5.00")
print(f"{qntd2:.0f} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{qntd1:.0f} moeda(s) de R$ 1.00")
print(f"{qntd05:.0f} moeda(s) de R$ 0.50")
print(f"{qntd025:.0f} moeda(s) de R$ 0.25")
print(f"{qntd010:.0f} moeda(s) de R$ 0.10")
print(f"{qntd005:.0f} moeda(s) de R$ 0.05")
print(f"{qntd001:.0f} moeda(s) de R$ 0.01")
