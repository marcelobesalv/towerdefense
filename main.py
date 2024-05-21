from func import *
import pygame
from inimigos import *
import sys
from torretas import *
from botao import *
from mundo import*

# pygame setup
pygame.init()
pygame.display.set_caption('loonbs')
screen_width = 1600
screen_height = 900
screen_jogo_width = 1280
painel_lateral = 320

ultimoBloon = pygame.time.get_ticks()
spawnCd = 500
world = mundo()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 74)
fonte_pequena = pygame.font.Font(None, 37)
running = True
clear = False

#Imagens do mapa
bgImg = pygame.image.load('imagens/monkeymeadow.jpg')
bgImg = pygame.transform.scale(bgImg, (screen_jogo_width, screen_height))


menuImg = pygame.image.load('imagens/loonbs.jpg')
menuImg = pygame.transform.scale(menuImg, (screen_width, screen_height))
game_display = pygame.display.set_mode((screen_width, screen_height))

buttonImg = pygame.image.load('imagens/madeira.jpg')
buttonImg = pygame.transform.scale(buttonImg, (200, 50))

comprar_torreImg = pygame.image.load('imagens/comprartorre1.png')
comprar_torreImg = pygame.transform.scale(comprar_torreImg, (200, 50))

#criando botoes
torreta_botao = Botao(screen_jogo_width + 30, 120,comprar_torreImg )
#cancelar_botao = Botao(screen_jogo_width + 50, 180, )


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
    (0, 375), (635, 375), (635, 175), (420, 175), (420, 720),
    (210, 720), (210, 525), (800, 525), (800, 300), (960, 300),
    (960, 650), (570, 650), (570, 900)
]

# Importa as imagens
dicInimigos = {
    1: pygame.image.load('imagens/balon.png').convert_alpha(),  # Imagem do inimigo 1
    2: pygame.image.load('imagens/balon2.png').convert_alpha(),  # Imagem do inimigo 2
    3: pygame.image.load('imagens/ngbloon.png').convert_alpha()  # Imagem do inimigo 3
    
}

# img1 = pygame.image.load('imagens/balon.png').convert_alpha()  # Imagem do inimigo 1
# img2 = pygame.image.load('imagens/balon2.png').convert_alpha()  # Imagem do inimigo 2
img3 = pygame.image.load('imagens/inimigo1.teste.png').convert_alpha()
# imagem_pqn = pygame.transform.scale(img1, (70, 70))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#TESTE DE CRIACAO DE ALGUMAS FUNCOES

# Limite de proximidade da trajetória e de outras torres
proximidade_limite_trajetoria = 25  # Distância mínima dos waypoints
proximidade_limite_torres = 50 # Distância mínima entre torres

def distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def distancia_ponto_linha(p, p1, p2):
    if p1 == p2:
        return distancia(p, p1)
    
    x0, y0 = p
    #coordenadas dos pontos da linha
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 == y2:
        return distancia(p, p1)
    
    # Calcula a distância do ponto à linha
    numerador = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denominador = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return numerador / denominador


def posicao_valida(posicao):
    # Verifica a proximidade com a trajetória
    for i in range(len(waypoints) - 1):
        if distancia_ponto_linha(posicao, waypoints[i], waypoints[i + 1]) < proximidade_limite_trajetoria:
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
        screen.blit(buttonImg, button_play)
        screen.blit(buttonImg, button_quit)

        draw_text('Jogar', fonte_pequena, corTxt, screen, screen_width // 2, screen_height // 2 + 75)
        draw_text('Sair', fonte_pequena, corTxt, screen, screen_width // 2, screen_height // 2 + 175)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


# Função principal do jogo
def jogo():
    global ultimoBloon
    world.spawnar()

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
                if posicao_mouse[0] < screen_jogo_width and posicao_mouse[1] < screen_height:
                    cria_torreta(posicao_mouse) #clica torreta

        # Renderização
        if pygame.time.get_ticks() - ultimoBloon > spawnCd:
            print(world.listaBloon)
            if world.spawnados < len(world.listaBloon):
                tipo = world.listaBloon[world.spawnados]
                enemy = inimigo(tipo, waypoints, dicInimigos)
                grupo_inimigos.add(enemy)
                world.spawnados += 1
                ultimoBloon = pygame.time.get_ticks()
            # else: 
            #     world.level += 1
            #     world.spawnar()

        game_display.blit(bgImg, (0, 0))
        pygame.draw.lines(screen, 'grey0', False, waypoints)


        #tentativa de draw dos botoes
        #colcar torreta
        if torreta_botao.draw(screen):
            print('testando')

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