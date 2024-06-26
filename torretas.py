import pygame
import math


class Torres(pygame.sprite.Sprite):
    def __init__(self, imagelist, pos, tipo_torre,r):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

        self.animationlist = imagelist
        self.framei = 0
        self.updatetime = pygame.time.get_ticks()
        self.x = pos[0]
        self.y = pos[1]
        self.image = self.animationlist[self.framei]
        self.rect = self.image.get_rect(center=pos)
        self.tipo_torre = tipo_torre
        
        self.range = r
        self.cooldown = 550
        self.target = None
        self.angle = 180
        

        self.original_image = self.animationlist[self.framei]
        self.image = pygame.transform.rotate(self.original_image, self.angle)

    def escolheAlvo(self, grupo_inimigos):
        x_dist = 0
        y_dist = 0
        for i in grupo_inimigos:
            x_dist = i.pos[0] - self.x
            y_dist = i.pos[1] - self.y    
            dist = math.sqrt(x_dist**2+y_dist**2)
            if dist < self.range:
                if i.health > 0:
                    self.angle = math.degrees(math.atan2(-y_dist, x_dist))
                    self.target = i
                    if self.tipo_torre == 1:
                        self.target.health -= 1
                    elif self.tipo_torre == 2:
                        self.target.health -= 3
                    elif self.tipo_torre == 3:
                        self.target.health -= 5

    def update(self, grupo_inimigos):
        if self.target:
            self.playanim()
        else:
            if pygame.time.get_ticks() - self.updatetime >= self.cooldown:               
                self.escolheAlvo(grupo_inimigos)

    def playanim(self):
        self.original_image = self.animationlist[self.framei]
        self.image = pygame.transform.rotate(self.original_image, self.angle-90)
        
        if pygame.time.get_ticks() - self.updatetime > 150:
            self.updatetime = pygame.time.get_ticks()
            self.framei +=1
            if self.framei >= len(self.animationlist):
                self.framei = 0
                self.target = None

