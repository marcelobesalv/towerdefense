#teste
#teste2
from func import *
import pygame
from inimigos import *

# pygame setup
pygame.init()
pygame.display.set_caption('loonbs')
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()
running = True
torres = {'bola': [], 'quadrado': [], 'triangulo': []} #{tipo: [(x, y), (x2, y2), ...]}
clear = False


# usarei para importar imagens dos inimogs !!! !!!!! ! !! AINDA PREICSO TESTAR
inimigo1_img = pygame.image.load('imagens/inimigo1.teste.png').convert_alpha()

#criação de grupos de inimigo (NECESSARIO, visto que tera diferentes tipos de inimigos)
inimigo_group = pygame.sprite.Group()
#tentativa de chamar inimigo
enemy = inimigo((200,300), inimigo1_img)
print (enemy)

while running:
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
    coloca_torre(screen, torres)
 
    


    pygame.display.flip()
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()