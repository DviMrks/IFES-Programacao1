aluno = str(input("Digite o nome do aluno: "))
N1 = float(input("Digite a primeira nota (de 0 a 10) "))
N2 = float(input("Digite a segunda nota (de 0 a 10) "))
N3 = float(input("Digite a terceita nota (de 0 a 10) "))

while N1 < 0 or N1 > 10:
    N1 = float(input("Digite a primeira nota VALIDA (de 0 a 10) "))

while N2 < 0 or N2 > 10: 
    N2 = float(input("Digite a segunda nota VALIDA (de 0 a 10) "))

while N3 < 0 or N3 > 10: 
    N3 = float(input("Digite a terceita nota VALIDA (de 0 a 10) "))

media = (N1 + N2 + N3) / 3

if media >= 7:
    print("APROVADO")
elif media < 6:
    print("REPROVADO")
else :
    print("PROVA FINAL")

if N1 > N2 > N3 :
    print("%.2F, %.2F, %.2F" %(N1,N2,N3))
elif N1 > N3 > N2 :
    print("%.2f,%.2f,%.2f" %(N1,N3,N2))
elif N2 > N3 > N1 :
    print("%.2F, %.2F, %.2F" %(N2,N3,N1))
elif N2 > N1 > N3 :
    print("%.2F, %.2F, %.2F" %(N2,N1,N3))
elif N3 > N2 > N1 :
    print("%.2f, %.2f, %.2f" %(N3,N2,N1))
elif N3 > N1 > N2 :
    print("%.2f, %.2f, %.2f" %(N3,N1,N2))
else : 
    print("deu erro viu")




