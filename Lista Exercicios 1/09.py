Km = int(input("Quantos KM percorridos tem o carro? "))
diasAluguel = int(input("Quantos dias durou o aluguel do carro? "))

calculoKm = Km * 0.15
calculoDias = diasAluguel * 60

calculoTotal = calculoKm + calculoDias

print("A quantidade a ser paga deve ser de: %f R$" %(calculoTotal))

