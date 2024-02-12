# Login do Sistema
email_cadastrado = "seu_email@exemple.com"
senha_cadastrada = "senha_pessoal"

# Loop para verificação de acesso.

while True:
    # Solicita ao usuário que digite o e-mail e a senha
    email_usuario = input ("Digite seu email:")
    Senha_usuário = input("Digite sua senha:")

    # Verificando se o email e a senha estão corretos

    if email_usuario == email_cadastrado and Senha_usuário == senha_cadastrada:
        print ("Acesso permitido! Bem Vindo.")
        break # Sai do loop quando o acesso está correto
    else:
        print("Email ou senha incorretos. Tente novamente.")