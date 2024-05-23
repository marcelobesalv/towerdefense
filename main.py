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

comprar_torre1Img = pygame.image.load('imagens/madeirafundo (1).png')
comprar_torre1Img = pygame.transform.scale(comprar_torre1Img, (200, 50))

comprar_torre2Img = pygame.image.load('imagens/madeirafundo (2).png')
comprar_torre2Img = pygame.transform.scale(comprar_torre2Img, (200, 50))

comprar_torre3Img = pygame.image.load('imagens/madeirafundo (3).png')
comprar_torre3Img = pygame.transform.scale(comprar_torre3Img, (200, 50))

#criando botoes
torreta_botao1 = Botao(screen_jogo_width + 30, 120,comprar_torre1Img)
torreta_botao2 = Botao(screen_jogo_width + 30, 180,comprar_torre2Img)
torreta_botao3 = Botao(screen_jogo_width + 30, 240, comprar_torre3Img)


def gameover():
    gameover = pygame.transform.scale(pygame.image.load('imagens/gameover.png'),(1600,900))

    game_display.blit(gameover,(0,0))
    draw_text(f'Nivel atingido:{world.level-1}',fonte_pequena,(255,255,255),screen,800,800)
#criando torretas
def cria_torreta(posicao_mouse, tipo_torre):
    r = 0

    if tipo_torre is not None and posicao_valida(posicao_mouse):
        if tipo_torre == 1:
            if world.money >= 100:
                world.money -= 100
                imagem_torre = [nishi,nishiat]
                r = 400
            else:
                imagem_torre = None
        elif tipo_torre == 2:
            if world.money >= 200:
                world.money -= 200
                imagem_torre = [zeca,zecaat]
                r = 250
            else:
                imagem_torre = None
        elif tipo_torre == 3:
            if world.money >= 400:
                world.money -= 400
                imagem_torre = [shrek,shrekat]
                r = 150
            else:
                imagem_torre = None
        else:
            imagem_torre = None
        
        if imagem_torre:
            torre = Torres(imagem_torre, posicao_mouse, tipo_torre,r)
            grupo_torres.add(torre)
            print('Torre colocada em:', posicao_mouse)
        else:
            print('Tipo de torre desconhecido:', tipo_torre)
    else:
     print('Posição inválida para torre:', posicao_mouse)

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
    1: pygame.transform.scale(pygame.image.load('imagens/balon.png').convert_alpha(),(70,70)),  # Imagem do inimigo 1
    2: pygame.transform.scale(pygame.image.load('imagens/balon2.png').convert_alpha(),(70,70)),  # Imagem do inimigo 2
    3: pygame.transform.scale(pygame.image.load('imagens/balon3.png').convert_alpha(),(70,90)),  # Imagem do inimigo 3
    4: pygame.transform.scale(pygame.image.load('imagens/balon4.png').convert_alpha(),(70,90)),  # Imagem do inimigo 4
    5: pygame.transform.scale(pygame.image.load('imagens/ngbloon.png').convert_alpha(),(110,110)),  # Imagem do inimigo 5
    6: pygame.transform.scale(pygame.image.load('imagens/bolon.png').convert_alpha(),(180,210))  # Imagem do inimigo 6

}

# img1 = pygame.image.load('imagens/balon.png').convert_alpha()  # Imagem do inimigo 1
# img2 = pygame.image.load('imagens/balon2.png').convert_alpha()  # Imagem do inimigo 2
img3 = pygame.image.load('imagens/inimigo1.teste.png').convert_alpha()
img4 = pygame.image.load('imagens/ngbloon.png').convert_alpha()  # Exemplo de imagem para torre 2
img5 = pygame.image.load('imagens/comprartorre1.png').convert_alpha()# Exemplo de imagem para torre 3
nishi = pygame.transform.scale(pygame.image.load('imagens/nishi.png').convert_alpha(),(200,200))
nishiat = pygame.transform.scale(pygame.image.load('imagens/nishiasf.png').convert_alpha(),(200,200))
zeca = pygame.transform.scale(pygame.image.load('imagens/zecau.png').convert_alpha(),(200,200))
zecaat = pygame.transform.scale(pygame.image.load('imagens/zecausf.png').convert_alpha(),(200,200))
shrek = pygame.image.load('imagens/shreksbsf.png').convert_alpha()
shrekat = pygame.image.load('imagens/shrekbsf.png').convert_alpha()
# imagem_pqn = pygame.transform.scale(img1, (70, 70))

def infinte():
    dic = {1:random.randint(0,10),2:random.randint(5,30),3:random.randint(0,10),4:random.randint(0,10),5:random.randint(0,10),6:random.randint(5,30)}
    waves.append(dic)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#TESTE DE CRIACAO DE ALGUMAS FUNCOES
def draw_hud(world, score):
    draw_text(f'Vida: {world.health}', fonte_pequena, (255, 255, 255), screen, screen_jogo_width - 100, 40)
    draw_text(f'Dinheiro: {world.money}', fonte_pequena, (255, 255, 255), screen, screen_jogo_width - 100, 80)
    draw_text(f'Nível: {world.level}', fonte_pequena, (255, 255, 255), screen, screen_jogo_width- 100,120)
    draw_text(f'------------------------' , fonte_pequena, (255, 255, 255), screen, screen_jogo_width- 100,135)
    draw_text(f'Custo: 100', fonte_pequena, (227, 213, 11), screen, screen_jogo_width - 85, 150) 
    draw_text(f'Custo: 200', fonte_pequena, (227, 213, 11), screen, screen_jogo_width - 85, 205)
    draw_text(f'Custo: 400', fonte_pequena, (227, 213, 11), screen, screen_jogo_width - 85, 270)
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
    torre_selecionada = None

    iniciarLvl = False
    score = 0
    tempo_inicial = pygame.time.get_ticks()



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
                    cria_torreta(posicao_mouse, torre_selecionada)
                    torre_selecionada = None #clica torreta
                else:
                    print("Nenhuma torre selecionada")

        # Renderização
        if iniciarLvl == False:
            button_start = pygame.Rect(screen_width // 2 + 510, screen_height // 2 + 300, 200, 50)
            pygame.draw.rect(screen, (255,255,255), button_start)
            screen.blit(buttonImg, button_start)
            draw_text('Iniciar', fonte_pequena, (255,255,255), screen, screen_width // 2+610, screen_height // 2 + 325)
            mx, my = pygame.mouse.get_pos()
            if button_start.collidepoint((mx, my)):
                if pygame.mouse.get_pressed()[0]:
                    iniciarLvl = True  # comeca round
        else:
            if pygame.time.get_ticks() - ultimoBloon > spawnCd:
                if world.spawnados < len(world.listaBloon):
                    tipo = world.listaBloon[world.spawnados]
                    enemy = inimigo(tipo, waypoints, dicInimigos)
                    grupo_inimigos.add(enemy)
                    world.spawnados += 1
                    ultimoBloon = pygame.time.get_ticks()
        
        if world.levelCompleto() == True:
            iniciarLvl = False
            world.level += 1
            ultimoBloon = pygame.time.get_ticks()
            world.spawnados = 0
            world.kills = 0
            world.passou = 0
            world.listaBloon = []
            world.spawnar()
            inimigo.scale()
            

        game_display.blit(bgImg, (0, 0))
        
        tempo_atual = pygame.time.get_ticks()
        score = (tempo_atual - tempo_inicial) // 1000 * 10

        draw_hud(world,score)
        #tentativa de draw dos botoes
        #colcar torreta
        if torreta_botao1.draw(screen):
            print('testando')
            torre_selecionada = 1
        if torreta_botao2.draw(screen):
            print('testando2')
            torre_selecionada = 2
        if torreta_botao3.draw(screen):
            print('testando3')
            torre_selecionada = 3
        if world.health <= 0:
            gameover()
        # Update dos grupos e desenho dos inimigos
        infinte()
        grupo_inimigos.update(world)
        grupo_inimigos.draw(screen)
        grupo_torres.update (grupo_inimigos)
        grupo_torres.draw(screen)
        for enemy in grupo_inimigos:
            enemy.mover()
            print(enemy.health)
            
        pygame.display.flip()
        pygame.display.update()

    pygame.quit()
    sys.exit()

# Iniciar o menu
main_menu()
