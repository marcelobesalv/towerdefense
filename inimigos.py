import pygame

class inimigo(pygame.sprite.Sprite): #sprite da mais funcionalidade ao inimigo
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def update(self):
        self.mover

    def mover(self): #funcao de mover
        self.rect.x += 1
