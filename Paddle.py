import math

import pygame
from Obstacle import Obstacle


class Paddle(Obstacle):
    _dx: int

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._color = (0, 255, 0)
        self._dx = 10

    def checkMovement(self, screen):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if self._rect.x > 0:
                self._rect.x -= self._dx
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if self._rect.x <= screen.get_width() - self._rect.width:
                self._rect.x += self._dx

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)
