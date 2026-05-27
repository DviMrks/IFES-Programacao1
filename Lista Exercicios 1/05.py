nome = str(input("Digite o nome do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
preco = int(input("Digite o preço do produto: "))
desconto = int(input("Digite a porcentagem de desconto: "))

descontoPorcentagem = (desconto / 100)

valorDesconto = descontoPorcentagem * preco
valorAPagar = (valorDesconto - preco) * quantidade

print("Para o produto %s o valor do desconto vai ser %f e o valor a pagar por todos os produtos vai ser %f" %(nome, valorDesconto, valorAPagar))