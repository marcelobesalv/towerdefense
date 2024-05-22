import pygame
import math

class Torres(pygame.sprite.Sprite):
    def __init__(self, imagelist, pos, tipo_torre):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.animationlist = imagelist
        self.framei = 0
        self.updatetime = pygame.time.get_ticks()


        self.image = self.animationlist[self.framei]
        self.rect = self.image.get_rect(center=pos)
        self.tipo_torre = tipo_torre

        self.range = 500
        self.cooldown = 500
        self.target = None
        self.angle = 90
        self.imageRot = pygame.transform.rotate(self.image, self.angle)

        

    def escolheAlvo(self, grupo_inimigos):
        for i in grupo_inimigos:
            self.target = i
            print('alvo')

    def update(self, grupo_inimigos):
        if self.target:
            self.playanim()
        else:
            if pygame.time.get_ticks() - self.updatetime >= self.cooldown:               
                self.escolheAlvo(grupo_inimigos)

    def playanim(self):
        self.image = self.animationlist[self.framei]
        if pygame.time.get_ticks() - self.updatetime > 150:
            self.updatetime = pygame.time.get_ticks()
            self.framei +=1
            if self.framei >= len(self.animationlist):
                self.framei = 0
                self.target = None

