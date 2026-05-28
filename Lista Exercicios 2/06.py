tipoCombustivel = str(input("Digite o tipo de combustível ('G' para Gasolina e 'A' para alcool): "))

while tipoCombustivel != "G" and tipoCombustivel != "A":
    tipoCombustivel = str(input("Digite o tipo de combustível ('G' para Gasolina e 'A' para alcool): "))

litro = float(input("Digite quantos litros de combustível foram utilizados: "))


if tipoCombustivel == "A":
    if litro <= 20:
        valor = litro * 3.20
        valorFinal = valor - (valor * 0.03)
    elif litro > 20:
        valor = litro * 3.20
        valorFinal = valor - (valor * 0.05)
    print("O valor do seu combustível (Alcool) deu %.2F R$" %valorFinal)

if tipoCombustivel == "G":
    if litro <= 20:
        valor = litro * 3.90
        valorFinal = valor - (valor * 0.04)
    elif litro > 20:
        valor = litro * 3.90
        valorFinal = valor - (valor * 0.06)
    print("O valor do seu combustível (Gasolina) deu %.2F R$" %valorFinal)

    
