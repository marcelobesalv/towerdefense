import pygame

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

    def update(self):
        self.playanim()
    def playanim(self):
        self.image = self.animationlist[self.framei]
        if pygame.time.get_ticks() - self.updatetime > 150:
            self.updatetime = pygame.time.get_ticks()
            self.framei +=1
            if self.framei >= len(self.animationlist):
                self.framei = 0
