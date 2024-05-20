#teste
#teste2
from func import *
import pygame
from inimigos import *

# pygame setup
pygame.init()
pygame.display.set_caption('loonbs')
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
torres = {'bola': [], 'quadrado': [], 'triangulo': []} #{tipo: [(x, y), (x2, y2), ...]}
clear = False

#criação de grupos de inimigo (NECESSARIO, visto que tera diferentes tipos de inimigos)
grupo_inimigos = pygame.sprite.Group()
#TENTATIVA DE CRIAÇÃO DE WAYPOINTS (DIREÇÕES E POSIÇÕES PARA SEREM IMPLEMENTADAS DEPOIS NO MAPA)
#CRIANDO TRACEJADO DO MAPA 
waypoints = [
    (50,250),
    (300,250),
    (300,100),
    (400,100),
    (400,600),
    (600,600),
    (800,600),
    (1000,200)
]
# usarei para importar imagens dos inimogs !!! !!!!! ! !! AINDA PREICSO TESTAR
img1 = pygame.image.load('imagens/inimigo1.teste.png').convert_alpha()
#tentativa de chamar inimigo
enemy = inimigo((waypoints), img1)
grupo_inimigos.add(enemy)
print (enemy)


pygame.display.flip()

while running:
    clock.tick (60)

    #update dos grupos
    grupo_inimigos.update()

    for enemy in grupo_inimigos:
        grupo_inimigos.draw(screen)
        enemy.mover()

    pygame.display.flip()
    pygame.display.update()


    mPos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: #bota torre bola
                torres['bola'].append(mPos)
                print('bolas', torres['bola'])
            if event.key == pygame.K_q: #remove ultima torre bola
                torres['bola'] = torres['bola'][:-1]
                print('bolas', torres['bola'])   

            if event.key == pygame.K_2: #bota torre quadrado
                torres['quadrado'].append(mPos)
                print('quadrados', torres['quadrado'])
            if event.key == pygame.K_w: #remove ultima torre quadrado
                torres['quadrado'] = torres['quadrado'][:-1]
                print('quadrados', torres['quadrado'])

            if event.key == pygame.K_3: #bota torre triangulo
                torres['triangulo'].append(mPos)
                print('triangulos', torres['triangulo'])
            if event.key == pygame.K_e: #remove ultima torre triangulo
                torres['triangulo'] = torres['triangulo'][:-1]
                print('triangulos', torres['triangulo'])  

    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||         
    #----------------------------------------RENDER------------------------------------------------------
    #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        
    screen.fill((90,170,20))

    pygame.draw.lines(screen, 'grey0', False, waypoints)

    coloca_torre(screen, torres)

pygame.quit()