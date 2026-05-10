import random

print("GamePlay")

usuario = input("Digite seu nome de usuário: ")
senha_correta = 6813
tentativas = 3

print(f"Olá {usuario}, você tem {tentativas} tentativas para acessar o sistema." )

while tentativas > 0:
   senha = int(input("Digite a senha: "))

   if senha == senha_correta: 
       print(f"Seja bem-vindo,", usuario,"!")
       break                    
   else: 
       tentativas -= 1
    
       if tentativas > 0:
         print(f"Senha incorreta! Tentativas restantes {tentativas}")
       else:
         print ("Acesso bloqueado!")

if tentativas > 0:                 
    numero_secreto = random.randint(1, 100)

    while True:

     palpite = int(input("Digite um número entre 1 e 100: "))

     if palpite == numero_secreto:
      print ("Você acertou! 🎉")

      jogar = 's'
      
      jogar = input("Quer jogar novamente? (s/n): ").lower()
      if jogar == 's':
         print ("Iniciando partida...")         


      if jogar != 's':
         print ("Fim de jogo.")
         break
        
     if palpite > numero_secreto:
      print ("Muito alto!")
 
     if palpite < numero_secreto:
      print ("Muito baixo!")


       

     



