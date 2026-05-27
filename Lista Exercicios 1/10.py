cigarrosDias = int(input("Quantos cigarros você fuma por dia? "))
cigarrosAnos = int(input("A quantos anos você fuma? "))

cigarrosMin_dias = cigarrosDias * 10
cigarrosAnos_dias = cigarrosAnos * 365

cigarrosTotal_Min = cigarrosAnos_dias * cigarrosMin_dias

cigarrosTotal_Dias = cigarrosTotal_Min/1440

print("O total de dias que você perdeu fumando foi de: %f" %(cigarrosTotal_Dias))


