import pygame
def coloca_torre(surf,d):
    for torre,lpos in d.items():
        if torre == 'bola':
            for pos in lpos:
                pygame.draw.circle(surf,(0,0,0),pos,50)
        if torre == 'quadrado':
            for pos in lpos:
                pygame.draw.rect(surf,(0,0,0), pygame.Rect(pos[0], pos[1], 100, 100))