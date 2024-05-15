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
torres = {'bola': [], 'quadrado': [], 'triangulo': []} #{tipo: [(x, y), (x2, y2), ...]}
clear = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: #bota torre bola
                torres['bola'].append((50, 50))
                print('bolas', torres['bola'])
            if event.key == pygame.K_q: #remove ultima torre bola
                torres['bola'] = torres['bola'][:-1]
                print('bolas', torres['bola'])   

            if event.key == pygame.K_2: #bota torre quadrado
                torres['quadrado'].append((100, 0))
                print('quadrados', torres['quadrado'])
            if event.key == pygame.K_w: #remove ultima torre quadrado
                torres['quadrado'] = torres['quadrado'][:-1]
                print('quadrados', torres['quadrado'])

            if event.key == pygame.K_1: #bota torre bola
                torres['bola'].append((50, 50))
                print('bolas', torres['bola'])
            if event.key == pygame.K_q: #remove ultima torre bola
                torres['bola'] = torres['bola'][:-1]
                print('bolas', torres['bola'])            
    #----------------------------------------render------------------------------------------------------
    screen.fill((90,170,20))
    coloca_torre(screen, torres)
 
    


    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()