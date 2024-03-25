import socket
import time 
import json
import threading

class Cliente:
    def __init__(self, config):
        self.ip = input("Qual o IP do servidor? Pressione Enter para o local: ")
        self.porta_s = int(input("Qual a porta do servidor? "))
        self.mensagem = input("Escolha a mensagem: ")
        self.quantidade2 = input("A quantidade de vezes a ser enviada? ")
        self.quantidade= int(self.quantidade2)
        self.opcao = input("Enviar de forma sequencial ou paralela? (s/p): ")
        if self.ip == '':
            self.ip = '127.0.0.1'
        self.config = config

    
    def enviar_n(self):
        #Enviar ao servidor o número de mensagens para o servidor se preparar
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytes(self.quantidade2, "utf-8"), (self.ip, self.porta_s))
        s.close()

    def enviar(self,mensagem):
        #Envio de mensagens com o delay
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytes(self.mensagem, "utf-8"), (self.ip, self.porta_s))
        # 6 - delay
        s.close()

    def ACK(self):
        ack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ack.bind((self.ip, 9000))
        ACK, _ = ack.recvfrom(1024)
        print("RECEBI DO SERVIDOR: ", ACK.decode("utf-8"))
        ack.close()
    
    def sequencial(self):
        self.ACK()
        for _ in range(self.quantidade+1):
            self.enviar("Mensagem")
        print("--- MENSAGENS ENVIADAS SEQUENCIALMENTE ---")

    def paralelo(self):
        self.ACK()
        #Abrir a lista das threads com a função de enviar o argumento (mensagem)
        threads = []
        for _ in range(self.quantidade+1):
            t = threading.Thread(target=self.enviar, args=(self.mensagem,))
            threads.append(t)
            t.start()
        for t in threads:
            #Com a lista completa, é iterado sobre cada item da lista
            #garantindo que a o programa não continue até a ultima ação
            t.join()
        print("--- MENSAGENS ENVIADAS PARALELAMENTE ---")

cliente = Cliente("config.json")
cliente.enviar_n()
if cliente.opcao == "s":
    cliente.sequencial()
elif cliente.opcao == "p":
    cliente.paralelo()
else:
    print("Modo de envio inválido.")