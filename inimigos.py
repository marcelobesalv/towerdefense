import pygame

class inimigo(pygame.sprite.Sprite): #sprite da mais funcionalidade ao inimigo
    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = pos

    def mover(self): #funcao de mover
        self.rect.x += 1
#  TESTE TESTE TESTE TESTE TESTE TESTE
    def update(self): #funcao que eu ainda preciso testar
        target = self.pos[self.pos_index]
        if self.rect.topleft == target:
            self.pos_index += 1
            if self.pos_index >= len(self.pos):
                self.kill()
                return
        direction = pygame.Vector2(target) - pygame.Vector2(self.rect.topleft)
        if direction.length() > self.speed:
            direction.scale_to_length(self.speed)
        self.rect.topleft += direction

pos = [(100, 100), (200, 100), (300, 200), (400, 300), (500, 300)] #testando