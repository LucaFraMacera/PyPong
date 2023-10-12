import math
from Ball import Ball
import pygame
from Obstacle import Obstacle

RED = (255, 0, 0)


class BlockMap:
    _blocks: [Obstacle]
    _mapWidth: int
    _edgeSpace: int

    def __init__(self, screen, rows, cols):
        self._blocks = []
        self._edgeSpace = 0
        self._mapWidth = screen.get_width() - (2 * self._edgeSpace)
        blockHeight = int(screen.get_height()/(3*rows))
        width = math.ceil((self._mapWidth) / cols)
        for i in range(0, rows):
            space = self._edgeSpace
            while space <= self._mapWidth - self._edgeSpace:
                self._blocks.append(
                    Obstacle(
                        space, i * (blockHeight + 2) + 5, width, blockHeight
                    )
                )
                space += width + 2

    def draw(self, screen):
        for block in self._blocks:
            pygame.draw.rect(screen, RED, block._rect)

    def checkCollisions(self, ball: Ball):
        for block in self._blocks:
            if ball.clips(block):
                self._blocks.remove(block)
                break

    def isEmpty(self):
        return len(self._blocks) == 0
