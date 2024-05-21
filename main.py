from func import *
import pygame
from inimigos import *
import sys


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
torres = {'bola': [], 'quadrado': [], 'triangulo': []}  # {tipo: [(x, y), (x2, y2), ...]}
clear = False

bgImg = pygame.image.load('imagens/monkeymeadow.jpg')
bgImg = pygame.transform.scale(bgImg, (1280, 720))
game_display = pygame.display.set_mode((1280, 720))

# Criação de grupos de inimigos (necessário, visto que haverá diferentes tipos de inimigos)
grupo_inimigos = pygame.sprite.Group()
# Criação de waypoints (direções e posições para serem implementadas no mapa)
waypoints = [
    (0, 300), (635, 300), (635, 135), (420, 135), (420, 580),
    (210, 580), (210, 420), (810, 420), (810, 245), (960, 245),
    (960, 525), (570, 525), (570, 720)
]

# Importa as imagens
img1 = pygame.image.load('imagens/balon.png').convert_alpha()  # Imagem do inimigo 1
img2 = pygame.image.load('imagens/balon2.png').convert_alpha()  # Imagem do inimigo 2
imagem_pqn = pygame.transform.scale(img1, (70, 70))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Função para o menu principal
def main_menu():
    while True:
        screen.fill((255, 255, 255))
        draw_text('Loonbs', fonte, (0, 0, 0), screen, screen_width // 2, screen_height // 4)

        mx, my = pygame.mouse.get_pos()

        # Botões
        button_play = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 50)
        button_quit = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)

        if button_play.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                jogo()  # Chama a função do jogo
        if button_quit.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (0, 0, 0), button_play)
        pygame.draw.rect(screen, (0, 0, 0), button_quit)

        draw_text('Jogar', fonte_pequena, (255, 255, 255), screen, screen_width // 2, screen_height // 2 - 25)
        draw_text('Sair', fonte_pequena, (255, 255, 255), screen, screen_width // 2, screen_height // 2 + 75)

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
    print(enemy1)

    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                mPos = pygame.mouse.get_pos()
                if event.key == pygame.K_1:  # Bota torre bola
                    torres['bola'].append(mPos)
                    print('bolas', torres['bola'])
                if event.key == pygame.K_q:  # Remove última torre bola
                    torres['bola'] = torres['bola'][:-1]
                    print('bolas', torres['bola'])

                if event.key == pygame.K_2:  # Bota torre quadrado
                    torres['quadrado'].append(mPos)
                    print('quadrados', torres['quadrado'])
                if event.key == pygame.K_w:  # Remove última torre quadrado
                    torres['quadrado'] = torres['quadrado'][:-1]
                    print('quadrados', torres['quadrado'])

                if event.key == pygame.K_3:  # Bota torre triângulo
                    torres['triangulo'].append(mPos)
                    print('triangulos', torres['triangulo'])
                if event.key == pygame.K_e:  # Remove última torre triângulo
                    torres['triangulo'] = torres['triangulo'][:-1]
                    print('triangulos', torres['triangulo'])

        # Renderização
        game_display.blit(bgImg, (0, 0))
        pygame.draw.lines(screen, 'grey0', False, waypoints)
        coloca_torre(screen, torres)

        # Update dos grupos e desenho dos inimigos
        grupo_inimigos.update()
        grupo_inimigos.draw(screen)
        for enemy in grupo_inimigos:
            enemy.mover()

        pygame.display.flip()
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Iniciar o menu
main_menu()