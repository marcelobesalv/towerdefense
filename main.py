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
torres = {} #{tipo: [(x, y), (x2, y2), ...]}
torres['bola'] = []
clear = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #bota torre bola
                torres['bola'].append((50, 50))
            if event.key == pygame.K_BACKSPACE: #remove ultima torre bola
                print(torres['bola'])               
                torres['bola'] = torres['bola'][:-1]
                print(torres['bola'])               
    #----------------------------------------render------------------------------------------------------
    screen.fill((90,170,20))
    coloca_torre(screen, torres)
 
    


    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()