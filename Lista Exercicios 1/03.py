dias = int(input("Diga a quantidade de dias: "))
horas = int(input("Diga a quantidade de horas: "))
minutos = int(input("Diga a quantidade de minutos: "))
segundos = int(input("Diga a quantidaed de segundos: "))

dias_seg = (dias * 86400)
horas_seg = (horas * 3600)
minutos_seg = (minutos * 60)

soma = (dias_seg + horas_seg + minutos_seg + segundos)

print("O segundo %f" %(soma))