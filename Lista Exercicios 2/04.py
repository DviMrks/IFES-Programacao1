Hora = int(input("Que horas são? (apenas a hora, sem minutos) "))

if 0 <= Hora < 5 :
    print("Vai dormir")
elif 5 <= Hora < 12 :
    print("Bom dia")
elif 12 <= Hora < 18 :
    print("Boa tarde")
elif 18 <= Hora < 24 :
    print("Boa noite")
else :
    print("Hora inválida")
