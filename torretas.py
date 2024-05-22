import pygame

class Torres(pygame.sprite.Sprite):
    def __init__(self, image, pos, tipo_torre):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.tipo_torre = tipo_torre