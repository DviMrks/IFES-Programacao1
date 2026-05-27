
N = int(input("Digite um numero inteiro menor que zero para fazer a fatoração dele: "))
contador = 1
fatorial = 1

while N < 0 :
    print("Número digitado é menor que 0")
    N = int(input("Digite um numero inteiro novamente: "))

while contador <= N :
    fatorial = fatorial * contador
    contador = contador + 1

print("O fatorial do número %i é %i" %(N,fatorial))
    
