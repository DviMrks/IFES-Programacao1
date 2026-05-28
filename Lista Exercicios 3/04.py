#Nome: maior que 3 caracteres; 
#Idade: entre 0 e 150; 
#Salário: maior que zero; 
#Sexo: 'f' ou 'm'; 
#Estado Civil: 's', 'c', 'v', 'd'; (maiúsculas e minúsculas)

nome = str(input("Digite o seu nome: "))
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
sexo = str(input("Digite o seu sexo (m/f) "))
estadoCivil = str(input("Digite o seu estado civil (S/C/V/D)"))

while len(nome) <= 3:
    print("Digitar nome com mais que 3 caracteres")
    nome = str(input("Digite o seu nome: "))

while idade < 0 or idade > 150:
    print("Gentileza, digitar idade correta")
    idade = int(input("Digite a sua idade: "))

while salario < 0:
    print("Gentileza, digitar salário valido")
    salario = float(input("Digite o seu salário: "))

while sexo != "f" and sexo != "m" :
    print("Gentileza, inserir sexo válido!")
    sexo = str(input("Digite o seu sexo (m/f) "))

while estadoCivil != "s" and estadoCivil != "S" and estadoCivil != "c" and estadoCivil != "C" and estadoCivil != "v" and estadoCivil != "V" and estadoCivil != "d" and estadoCivil != "D" :
    print("Gentileza, inserir valor válido!")
    estadoCivil = str(input("Digite o seu estado civil (S/C/V/D)"))

print("nome: %s" %nome),print("idade: %i" %idade),print("salário: %.2f" %salario), print("sexo: %s" %sexo), print("estado civi: %s" %estadoCivil)    