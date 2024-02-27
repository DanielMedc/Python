import socket
from canal import Canal  

class Servidor:
    def __init__(self, canal):
        self.ip = '127.0.0.1'
        self.canal = canal

    def iniciar_servidor(self):
        print("Digite a porta do Servidor:")
        porta = int(input())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.ip, porta))
        msg, end = s.recvfrom(1024)
        while True:
            msg, end = s.recvfrom(1024)
            msg = self.canal.aplicar_propriedades(msg.decode("utf-8")) 
            contadores = canal.contadores()  
            print("Recebi", msg, "do cliente", end)
            print("Contadores:", contadores)

canal = Canal("config.json")  
servidor = Servidor(canal)
servidor.iniciar_servidor()
