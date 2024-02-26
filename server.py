import socket

class ServidorUDP:
    def __init__(self):
        self.ip = '127.0.0.1'

    def iniciar_servidor(self):
        print("Digite a porta do Servidor:")
        porta = int(input())
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.ip, porta))
        msg, end = s.recvfrom(1024)
        s.sendto(bytes("ACK","utf-8"), (end))
        while True:
            msg, end = s.recvfrom(1024)
            print("Recebi", msg, "do cliente", end)
            
servidor = ServidorUDP()
servidor.iniciar_servidor()
