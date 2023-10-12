import pygame
from Obstacle import Obstacle


class DeathZone(Obstacle):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self._color = (255, 0, 0)

