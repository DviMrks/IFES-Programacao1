nota = int(input("Digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    nota = int(input("Digite uma nota valida! entre 0 e 10: "))

print("A nota foi %.2f" %nota)