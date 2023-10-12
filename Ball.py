import math
import random
from Events import *
import pygame
from Paddle import Paddle

BLUE = (0, 0, 255)


class Ball:
    _circle: pygame.Rect
    _r: int  # radius of the ball
    _dx: int
    _dy: int

    def __init__(self, x, y):
        assert isinstance(x, int) and isinstance(y, int)
        self._r = 10
        self._circle = pygame.Rect(x, y, self._r, self._r)
        self._dx = 0
        self._dy = 5

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self._circle, 60, self._r)

    def move(self):
        self._circle.x += self._dx
        self._circle.y += self._dy
    """
    This method decides the velocity of the ball after it clips the pad. If the ball touches the pad near the center 
    it bounces more vertically. If it touches near the edges then it bounces more horizontally
    """
    def bounce(self, paddle):
        if self._dy < 0:
            return
        if self._dx == 0:
            self._dx = 5 if random.randint(0, 1) == 1 else -5
        bouncePotition = self._circle.centerx - paddle._rect.centerx
        core = math.floor(paddle._rect.width / 5)
        print(core)
        if abs(bouncePotition) <= core:
            self._dx = int(self._dx / abs(self._dx) * 5)
            self._dy = -10
            return
        else:
            self._dx = int(self._dx / abs(self._dx) * 10)
            self._dy = -5

    """
    This function flips the horizontal direction of the agent. 
    """

    def changeHorizontalMovement(self):
        self._dx = -self._dx

    """
    This function flips the vertical direction of the agent. 
    """

    def changeVerticalMovement(self):
        self._dy = -self._dy

    """
    Just like the method in the Environment class, this checks if the ball is touching an obstacle.
    It returns a bool that indicates that the ball has clipped an object and pushes in the pygame event list
    the corresponding event to be managed.
    """
    def clips(self, obstacle):
        vertical = (obstacle._rect.y <= self._circle.y + self._r) and (
                    obstacle._rect.y + obstacle._rect.height >= self._circle.y - self._r) and (
                           obstacle._rect.x <= self._circle.x <= obstacle._rect.x + obstacle._rect.width)
        horizontal = (obstacle._rect.x <= self._circle.x + self._r) and (
                    obstacle._rect.x + obstacle._rect.width >= self._circle.x - self._r) and (
                             obstacle._rect.y <= self._circle.y <= obstacle._rect.y + obstacle._rect.height)
        if vertical:
            if isinstance(obstacle,Paddle):
                pygame.event.post(pygame.event.Event(PADDLE_HIT))
            else:
                pygame.event.post(pygame.event.Event(VERTICAL_CLIP))
        elif horizontal:
            pygame.event.post(pygame.event.Event(HORIZONTAL_CLIP))
        return vertical or horizontal
