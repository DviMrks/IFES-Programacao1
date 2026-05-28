atleta = str(input("Gentileza informar o nome do atleta: "))

nota1 = float(input("Inserir a primeira nota: "))
nota2 = float(input("Inserir a segunda nota: "))
nota3 = float(input("Inserir a terceita nota: "))
nota4 = float(input("Inserir a quarta nota: "))
nota5 = float(input("Inserir a quinta nota: "))

notas = [nota1, nota2, nota3, nota4, nota5]

print("A maior nota foi: %.2f e a menor nota foi: %.2f" %(max(notas), min(notas)))

notas.remove(min(notas))
notas.remove(max(notas))

media = sum(notas) / len(notas)

print("Para o atleta %s a média foi %.2f" %(atleta, media))


