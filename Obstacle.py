import pygame


class Obstacle:
    _rect: pygame.Rect
    _color: (int, int, int)

    def __init__(self, x, y, width, height):
        assert isinstance(x, int) and isinstance(y, int) and isinstance(width, int) and isinstance(height, int)
        self._rect = pygame.Rect(x, y, width, height)
        self._color = (255, 0, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, self._color, self._rect)
