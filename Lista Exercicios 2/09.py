codigo = int(input("Digite o código do produto: "))
qnt = int(input("Digite a quantidade do produto: "))

if 1 <= codigo <= 10 :
    preco = 10.00
    print("O valor desse produto é %.2f R$" %preco)
elif 11 <= codigo <= 20 :
    preco = 20.00
    print("O valor desse produto é %.2f R$" %preco)
elif 21 <= codigo <= 30 :
    preco = 30.00
    print("O valor desse produto é %.2f R$" %preco)
elif 31 <= codigo <= 40 :
    preco = 40.00
    print("O valor desse produto é %.2f R$" %preco)
else :
    print("O código inserido é inválido")

valorTotal = preco * qnt
print("O valor total é de %.2f" %valorTotal)

if valorTotal <= 250.00 :
    desconto = 0.05
    print("O desconto é de 5%")
elif 251 <= valorTotal <= 500.00 :
    desconto = 0.10
    print("O desconto é de 10%")
else :
    desconto = 0.15
    print("O desconto é de 15%")

valorFinal = valorTotal - (valorTotal * desconto)
print("O valor final, com desconto aplicado, fica em: %.2f R$" %valorFinal)


