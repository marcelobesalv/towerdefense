import pygame
from pygame.math import Vector2
from stats import *
from mundo import *

pygame.mixer.init()
popSound = pygame.mixer.Sound("audio/pop.wav")
world = mundo()

class inimigo(pygame.sprite.Sprite): #sprite da mais funcionalidade ao inimigo
    def __init__(self, tipo, waypoints, images):
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.health = statsBloon.get(tipo)['health']
        self.speed = statsBloon.get(tipo)['speed']
        self.target_waypoint = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = images.get(tipo)
        self.rect = self.image.get_rect() 
        self.rect.center = self.pos
        self.tipo = tipo

    def update(self, world):
        self.mover()
        self.checaVida(world)

    def mover(self): #funcao de mover
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            if self.tipo == 1:
                world.health -= 1
            elif self.tipo == 2:
                world.health -= 2
            elif self.tipo == 3:
                world.health -= 5
            elif self.tipo == 4:
                world.health -= 10
            elif self.tipo == 5:
                world.health -= 30
            elif self.tipo == 6:
                world.health -= 100
            self.kill()
            world.passou += 1
            print(world.passou)
            print('--------------------------------------------------------')
        #calculando a distancia
        distancia = self.movement.length()
        #checando  se a distancai é maior doq a velocidade do inimigo
        if distancia >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if distancia != 0:
                self.pos += self.movement.normalize() * distancia
            self.target_waypoint += 1 
        self.rect.center = self.pos

    def checaVida(self, world):
        if self.health <= 0:
            if self.tipo == 1:
                world.money += 10
            elif self.tipo == 2:
                world.money += 20
            elif self.tipo == 3:
                world.money += 30
            elif self.tipo == 4:
                world.money += 40
            elif self.tipo == 5:
                world.money += 80
            elif self.tipo == 6:
                world.money += 150
            world.kills += 1
            pygame.mixer.Sound.play(popSound)
            self.kill()