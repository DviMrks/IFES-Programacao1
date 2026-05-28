import math

tamanhoM2 = float(input("Gentileza, inserir o tamanho em Metros Quadrados da área a ser pintada: "))

litros = tamanhoM2 / 3

print("Você vai prescisar de %.2f litros de tinta para %.2f metros quadrados" %(litros,tamanhoM2))

latas = math.ceil(litros / 18)
valor = latas * 80

print("Para essa quantidade, você vai utilizar %i lata(s) no valor total de %i" %(latas,valor))



