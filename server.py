import socket
from canal import Canal  

class Servidor:
    def __init__(self, canal):
        self.ip = '127.0.0.1'
        self.canal = canal
        self.porta = int(input("Digite a porta do Servidor:"))

    def iniciar_servidor(self):
        # 2 - Cria o socket do servidor
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.ip, self.porta))
        
        while True:
            ack = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # 1 - recebe a primeira mensagem como uma "flag" de quantas mensagens virão
            n, end = s.recvfrom(1024)
            i = 0
            ack.sendto(bytes("ACK", "utf-8"), (self.ip, 9000))
            n= int(n.decode("utf-8"))
            while i< n:
                i = i +1
                # 9 - corta o segmento do bytes > 1024
                msg, end = s.recvfrom(1024)
                #Aplicar propriedades do Canal
                msg = self.canal.aplicar_propriedades(msg.decode("utf-8"))  
                print("Recebi", msg, "do cliente", end)
            _, end = s.recvfrom(1024)
            # 3 - Mostrar integridade
            contadores = canal.contadores()  
            print("Contadores:", contadores)
            print("--- FIM DAS MENSAGENS DO CLIENTE ---")
            #Resetar os contadores de mensagens para o proximo cliente
            canal.zerar()

canal = Canal("config.json")  
servidor = Servidor(canal)
servidor.iniciar_servidor()