import socket
import time 
import json
import threading

class Cliente:
    def __init__(self, config):
        self.ip = input("Qual o IP do servidor? Pressione Enter para o local: ")
        self.porta_s = int(input("Qual a porta do servidor? "))
        self.mensagem = input("Escolha a mensagem: ")
        self.quantidade = int(input("A quantidade de vezes a ser enviada? "))
        self.opcao = input("Enviar de forma sequencial ou paralela? (s/p): ")
        if self.ip == '':
            self.ip = '127.0.0.1'
        self.config = config
        self.delay = self.carregar_delay()

    def carregar_delay(self):
        with open(self.config, 'r') as f:
            config = json.load(f)
        return config["delay"] / 1000

    def enviar(self, mensagem):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(bytes(self.mensagem, "utf-8"), (self.ip, self.porta_s))
        time.sleep(self.delay)
 

    def sequencial(self):
        for _ in range(self.quantidade+1):
            self.enviar("Mensagem de teste sequencial")

    def paralelo(self):
        threads = []
        for _ in range(self.quantidade+1):
            t = threading.Thread(target=self.enviar, args=(self.mensagem,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

cliente = Cliente("config.json")
if cliente.opcao == "s":
    cliente.sequencial()
elif cliente.opcao == "p":
    cliente.paralelo()
else:
    print("Modo de envio inválido.")
