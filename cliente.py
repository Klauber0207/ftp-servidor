import Pyro4
import ftplib

HOSTNAME = "ftp.dlptest.com"
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)#conectando com servidor
ftp_server.encoding = "utf-8"

opcao = 0
while opcao != 4:
    print("---" * 20)
    print ("""
    1.Mostrar lista de arquivos
    2.Escolha um arquivo para baixar
    3.Escolha um arquivo para enviar
    4.sair
    """)
    
    opcao = int(input("Escolha uma opção: "))
      
    if opcao == 1:
      print("\n" + '\033[32m' + 'ARQUIVOS NO SERVIDOR: ' + '\033[0;0m' + '\033[42m' + HOSTNAME + '\033[0;0m'+ "\n") 
      ftp_server.dir() #obtem lista de diretórios no servidor
      
    elif opcao == 2:
      filename = input("\n" + "Escolha um arquivo: " )
      server = Pyro4.Proxy("PYRONAME:server")
      print(server.welcomeMessage(filename))
      with open(filename, "wb") as file:
        ftp_server.retrbinary(f"RETR {filename}", file.write) #baixa os arquivos do servidor ftp
        file = open(filename, "r") 
        print("\n" + "Conteúdo do arquivo: ", file.read())
        
    elif opcao == 3:
      filename = input("\n" + "Qual arquivo deseja enviar: ").strip()
      with open(filename, "rb") as file: 
        ftp_server.storbinary(f"STOR {filename}", file) #faz upload do arquivo
      
      print("Arquivo enviado ao servidor foi: " + filename)
      
    elif opcao == 4:
        ftp_server.quit() #fecha a conexão
        
    else:
        print("\n" + '\033[31m' + "Opção inválida. Tente novamente!" + '\033[0;0m' )
        print("\n" + '=-=' * 20)
        
      
ftp_server.quit()#fecha a conexão


