import pygame
from pygame.math import Vector2

class inimigo(pygame.sprite.Sprite): #sprite da mais funcionalidade ao inimigo
    def __init__(self, waypoints, image):
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.speed = 2
        self.target_waypoint = 1
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect() 
        self.rect.center = self.pos

    def update(self):
        self.mover

    def mover(self): #funcao de mover
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos

        #calculando a distancia
        distancia = self.movement.length()
        #checando  se a distancai é maior doq a velocidade do inimigo
        if distancia >= self.speed:
            self.pos += self.movement.normalize() * self.speed
        else:
            if distancia != 0:
                self.pos += self.movement.normalize() * distancia
            self.target_waypoint + 1 
        self.rect.center = self.pos

