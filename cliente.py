import socket
import threading

class Cliente:
    def __init__(self):
        self.ip = input("qual o ip do servidor? enter para o local ")
        self.porta_s = int(input("qual a porta do servidor? "))
        self.mensagem = input("Escolha a mensagem ")
        self.quantidade = int(input("a quantidade de vezes a ser enviada? "))
        self.opcao = input("Enviar de forma sequencial ou paralela? (s/p): ")
        if self.ip == '':
            self.ip = '127.0.0.1'
            

    def enviar(self, mensagem):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytes(self.mensagem,"utf-8"), (self.ip,self.porta_s))

    def sequencial(self):
        for _ in range(self.quantidade+1):
            mensagem = "Mensagem de teste seq"
            self.enviar(mensagem)

    def paralelo(self):
        threads = []
        for _ in range(self.quantidade):
            mensagem = "Mensagem de teste para"
            t = threading.Thread(target=self.enviar, args=(mensagem,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

cliente = Cliente()
if cliente.opcao == "s":
    cliente.sequencial()
elif cliente.opcao == "p":
    cliente.paralelo()
else:
    print("Modo de envio inválido.")
