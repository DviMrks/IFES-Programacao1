salario = int(input("Diga o seu salário atual: "))
aumento = int(input("Diga a porcentagem do aumento: "))

aumentoPorcentagem = aumento / 100

valorAumento = aumentoPorcentagem * salario
novoSalario = valorAumento + salario

print("O valor do aumento foi de: %f e o novo salário é de %f" %(valorAumento, novoSalario))