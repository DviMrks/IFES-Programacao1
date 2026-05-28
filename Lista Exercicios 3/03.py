nome = str(input("Digite o nome do usuário: "))
senha = str(input("Digite a senha: "))

while senha == nome or len(senha) < 6 :
    print("ERRO, senha igual o nome do usuário ou senha tem menos de 6 caracteres.")
    nome = str(input("Digite o nome do usuário novamente: "))
    senha = str(input("Digite a senha novamente: "))

print("O nome do usuário é %s e a senha é %s" %(nome,senha))