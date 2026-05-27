preco = int(input("Digite o valor do produto: "))
desconto = 0

if preco <= 100.00 :
    desconto = 0.03
if preco > 100.00 :
    desconto = 0.05

descontoAplicado = desconto * preco
precoFinal = preco - descontoAplicado

print("O produto no valor de %.2f R$ ao aplicar o desconto fica: %.2f R$" %(preco, precoFinal))