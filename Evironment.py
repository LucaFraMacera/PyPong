import pygame
from Ball import Ball
from Events import *

GRAY = (160, 160, 160)


class Environment:
    screen: pygame.Surface

    def __init__(self, width, height):
        assert isinstance(width, int) and isinstance(height, int)
        self.screen = pygame.display.set_mode([width, height])

    """
    This methods checks if the ball clips the screen
    It pushes 2 events in the pygame event list corresponding to oh the ball clips the environment
    """

    def size(self):
        return self.screen.get_size()

    def clips(self, ball):
        assert isinstance(ball, Ball)
        horizontal = ball._circle.left < 0 or ball._circle.x + ball._circle.width > self.screen.get_width()
        vertical = ball._circle.top < 0 or ball._circle.bottom > self.screen.get_height()
        if vertical:
            pygame.event.post(pygame.event.Event(VERTICAL_CLIP))
        if horizontal:
            pygame.event.post(pygame.event.Event(HORIZONTAL_CLIP))

    def draw(self):
        self.screen.fill(GRAY)

    def render(self, obj):
        obj.draw(self.screen)
