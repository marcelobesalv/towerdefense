from func import *
import pygame
from inimigos import *
import sys
from torretas import *


# pygame setup
pygame.init()
pygame.display.set_caption('loonbs')
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 74)
fonte_pequena = pygame.font.Font(None, 37)
running = True
clear = False

#Imagens do mapa
bgImg = pygame.image.load('imagens/monkeymeadow.jpg')
bgImg = pygame.transform.scale(bgImg, (1280, 720))
game_display = pygame.display.set_mode((1280, 720))

menuImg = pygame.image.load('imagens/loonbs.jpg')
menuImg = pygame.transform.scale(menuImg, (1280, 720))
game_display = pygame.display.set_mode((1280, 720))

#criando torretas
def cria_torreta(posicao_mouse):
    if posicao_valida(posicao_mouse):
        torre = Torres(img3, posicao_mouse)
        grupo_torres.add(torre)
        print ('sim', posicao_mouse)
    else:
        print('nao')

    
#Criação de grupos EM GERAL
grupo_inimigos = pygame.sprite.Group() # Criação de grupos de inimigos (necessário, visto que haverá diferentes tipos de inimigos)
grupo_torres = pygame.sprite.Group()

# Criação de waypoints (direções e posições para serem implementadas no mapa)
waypoints = [
    (0, 300), (635, 300), (635, 135), (420, 135), (420, 580),
    (210, 580), (210, 420), (810, 420), (810, 245), (960, 245),
    (960, 525), (570, 525), (570, 720)
]

# Importa as imagens
img1 = pygame.image.load('imagens/balon.png').convert_alpha()  # Imagem do inimigo 1
img2 = pygame.image.load('imagens/balon2.png').convert_alpha()  # Imagem do inimigo 2
img3 = pygame.image.load('imagens/inimigo1.teste.png').convert_alpha()
imagem_pqn = pygame.transform.scale(img1, (70, 70))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#TESTE DE CRIACAO DE ALGUMAS FUNCOES

# Limite de proximidade da trajetória e de outras torres
proximidade_limite_trajetoria = 50  # Distância mínima dos waypoints
proximidade_limite_torres = 70  # Distância mínima entre torres

def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def posicao_valida(posicao):
    # Verifica a proximidade com a trajetória
    for waypoint in waypoints:
        if distancia(posicao, waypoint) < proximidade_limite_trajetoria:
            return False
    
    # Verifica a proximidade com outras torres
    for torre in grupo_torres:
        if distancia(posicao, torre.rect.center) < proximidade_limite_torres:
            return False

    return True

# Função para o menu principal
def main_menu():
    while True:
        game_display.blit(menuImg, (0, 0))

        mx, my = pygame.mouse.get_pos()

        # Botões
        button_play = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
        border1 = pygame.Rect(screen_width // 2 - 105, screen_height // 2 + 45, 210, 60)
        button_quit = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 150, 200, 50)
        border2 = pygame.Rect(screen_width // 2 - 105, screen_height // 2 + 145, 210, 60)

        if button_play.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                jogo()  # Chama a função do jogo
        if button_quit.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

        corBor = (0,0,0)
        corBot = (199, 127, 12)
        corTxt = (255, 255, 255)
        pygame.draw.rect(screen, corBor, border1)
        pygame.draw.rect(screen, corBor, border2)
        pygame.draw.rect(screen, corBot, button_play)
        pygame.draw.rect(screen, corBot, button_quit)

        draw_text('Jogar', fonte_pequena, corTxt, screen, screen_width // 2, screen_height // 2 + 75)
        draw_text('Sair', fonte_pequena, corTxt, screen, screen_width // 2, screen_height // 2 + 175)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# Função principal do jogo
def jogo():
    enemy1 = inimigo(waypoints, imagem_pqn)  # Configura o inimigo, trajetória e imagem
    enemy2 = inimigo(waypoints, img2)
    grupo_inimigos.add(enemy1)
    grupo_inimigos.add(enemy2)  # Adiciona o inimigo ao grupo

    running = True
    while running:
        clock.tick(60)
        #Funcao de sair do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #CLICAR para colocar a torreta
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posicao_mouse = pygame.mouse.get_pos()
                if posicao_mouse[0] < screen_width and posicao_mouse[1] < screen_height:
                    cria_torreta(posicao_mouse) #clica torreta

        # Renderização
        game_display.blit(bgImg, (0, 0))
        pygame.draw.lines(screen, 'grey0', False, waypoints)

        # Update dos grupos e desenho dos inimigos
        grupo_inimigos.update()
        grupo_inimigos.draw(screen)
        grupo_torres.update (screen)
        grupo_torres.draw(screen)
        for enemy in grupo_inimigos:
            enemy.mover()

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Iniciar o menu
main_menu()