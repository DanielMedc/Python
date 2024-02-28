import json
import random

class Canal:
    def __init__(self, config):
        self.probabilidades = self.carregar_probabilidades(config)
        self.c_corromper = 0
        self.c_duplicar  = 0
        self.c_eliminar  = 0
        self.c_total     = 0

    def carregar_probabilidades(self, config):
        # 4 - Abrir arquivo json
        with open("config.json", 'r') as f:
            config = json.load(f)
        return config

    def aplicar_propriedades(self, mensagem):
        self.c_total += 1
        # 8 - Corromper 1 bit com probabilidade especificada no arquivo JSON
        if random.randint(0, 99) < int(self.probabilidades["probabilidade"]["corromper"]):
            # Escolhe aleatoriamente um índice dentro da mensagem
            indice = random.randint(0, len(mensagem) - 1)
            # Inverte o bit na posição escolhida
            mensagem = mensagem[:indice] + chr(ord(mensagem[indice]) ^ 1) + mensagem[indice+1:]
            self.c_corromper += 1
         # 7 - Duplicar mensagem com probabilidade especificada no arquivo JSON
        if random.randint(0,99) < int(self.probabilidades["probabilidade"]["duplicar"]):
            mensagem = mensagem + mensagem
            self.c_duplicar  += 1
         # 5 - Eliminar mensagem com probabilidade especificada no arquivo JSON
        if random.randint(0,99) < int(self.probabilidades["probabilidade"]["eliminar"]):
            mensagem = ""
            self.c_eliminar  += 1
        return mensagem
    
    def contadores(self):
        return{
            "Mensagens totais": self.c_total,
            "corrompidos": self.c_corromper,
            "duplicados": self.c_duplicar,
            "eliminados": self.c_eliminar
        }
    
    def zerar(self):
        self.c_corromper = 0
        self.c_duplicar  = 0
        self.c_eliminar  = 0
        self.c_total     = 0