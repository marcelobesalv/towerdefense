import pygame


def coloca_torre(surf,d):
    for torre,lpos in d.items():
        if torre == 'bola':
            diametro = 100
            for pos in lpos:
                pygame.draw.circle(surf,(0,0,0),pos,diametro/2)
        if torre == 'quadrado':
            lado = 100
            for pos in lpos:
                pygame.draw.rect(surf,(0,0,0), pygame.Rect(pos[0]-lado/2, pos[1]-lado/2, lado, lado))
        if torre == 'triangulo':
            altura = 100
            lado = 2*altura/(3**(1/2))
            for pos in lpos:
                pygame.draw.polygon(surf,(0,0,0), [(pos[0]-lado/2, pos[1]+altura/3), (pos[0]+lado/2, pos[1]+altura/3), (pos[0], pos[1]-altura*2/3)])
