idade = int(input("Inserir a idade do paciente: "))
peso = float(input("Inserir o peso do paciente: "))

if idade >= 12:
    if peso >= 60:
        dosagem = 1000
    if peso < 60:
        dosagem = 875
elif idade < 12: 
    if 5 < peso <= 9:
        dosagem = 125
    elif peso <= 16:
        dosagem = 250
    elif peso <= 24:
        dosagem = 375
    elif peso <= 30:
        dosagem = 500
    else:
        dosagem = 750

gotas = (dosagem / 500) * 20
print("Para o paciente de %s anos e de peso %.2f Kg, será necessário %i gotas" %(idade, peso, gotas))