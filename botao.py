import pygame

class Botao():
    def __init__(self, x, y, img):
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        acao = False
        posicao = pygame.mouse.get_pos()

        if self.rect.collidepoint(posicao):
            if pygame.mouse.get_pressed()[0] == 1:
                acao = True

        surface.blit(self.image, self.rect)

        return acao
