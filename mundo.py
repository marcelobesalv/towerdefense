from stats import *
import random
import jogador as j

class mundo():
    def __init__(self):
        self.level = 1
        self.listaBloon = []
        self.spawnados = 0

        self.health = j.VIDA
        self.money = j.DINHEIRO

    def spawnar(self):
        inimigos = waves[self.level-1]
        for tipo in inimigos:
            numSpawn = inimigos[tipo]
            for i in range(numSpawn):
                self.listaBloon.append(tipo)
        random.shuffle(self.listaBloon)
        print(self.listaBloon)