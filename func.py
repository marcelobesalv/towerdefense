import pygame
def coloca_torre(surf,d):
    for torre,lpos in d.items():
        for pos in lpos:
            pygame.draw.circle(surf,(0,0,0),pos,50)


