
email = input("Digite o e-mail de acesso: ")
senha = input("Digite a senha de acesso: ")

if email == "teste@teste.com.br":
   print("email correto")
else: 
   print("usuário não cadastrado")
   
   if senha == "123456":
      print("Bem Vindo ao sistema da Fábrica")
      
   else:
      print("Senha incorreta")