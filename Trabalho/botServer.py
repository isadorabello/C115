from socket import *

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
# atribui a porta ao socket criado
serverSocket.bind(("", serverPort))
# aceita conexoes
# com no maximo um cliente na fil
serverSocket.listen(1)

connectionSocket, addr = serverSocket.accept()
escolha = connectionSocket.recv(1024).decode()
msgCliente = "Olá, insira o numero do telefone:"
connectionSocket.send(msgCliente.encode())

while True:
    # recebe a mensagem do cliente em bytes
    telefone = connectionSocket.recv(1024)
    # envio tbm deve ser em bytes
    msgCliente = "Para fatura digite 2, saldo de dados 3, cancelamento 4 e 5 para encerrar a chamada"
    connectionSocket.send(msgCliente.encode())
    escolha = connectionSocket.recv(1024).decode()
    if escolha == "2":
        msgCliente = "A fatura com vencimento em set/2022  ́e de R$220, 00"
        connectionSocket.send(msgCliente.encode())
    elif escolha == "3":
        msgCliente = "Você esta com 52,5 em saldo para ligações e 400mb internet"
        connectionSocket.send(msgCliente.encode())
    elif escolha == "4":
        msgCliente = "Para mais informações de cancelamento ligue para 0800-4965"
        connectionSocket.send(msgCliente.encode())
    else:
        connectionSocket.close()
