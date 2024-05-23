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

        self.kills = 0
        self.passou = 0

    def spawnar(self):
        inimigos = waves[self.level-1]
        for tipo in inimigos:
            numSpawn = inimigos[tipo]
            for i in range(numSpawn):
                self.listaBloon.append(tipo)
        random.shuffle(self.listaBloon)
        print(self.listaBloon)


    def levelCompleto(self):
        
        if (self.kills + self.passou) >= len(self.listaBloon):
            print('level concluido')
            return True
    
        