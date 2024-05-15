import pygame
def coloca_torre(surf,d):
    for torre,lpos in d.items():
        if torre == 'bola':
            for pos in lpos:
                pygame.draw.circle(surf,(0,0,0),pos,50)
        if torre == 'quadrado':
            for pos in lpos:
                pygame.draw.rect(surf,(0,0,0), pygame.Rect(pos[0], pos[1], 100, 100))
        if torre == 'triangulo':
            for pos in lpos:
                pygame.draw.polygon(surf,(0,0,0), [pos, (pos[0]+50, pos[1]-100), (pos[0]+100, pos[1])])