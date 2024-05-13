#teste
#teste2
from func import *
import pygame
# pygame setup
pygame.init()
pygame.display.set_caption('loonbs')
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
running = True

screen.fill((90,170,20))
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                coloca_torre(screen,(pygame.Vector2(50,50)))
    

    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()