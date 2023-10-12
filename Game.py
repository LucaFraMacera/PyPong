import pygame

from DeathZone import DeathZone
from Ball import Ball
from BlockMap import BlockMap
from Paddle import Paddle
from Events import *
from Evironment import Environment
from Status import Status


class Game:
    _status: Status
    _ball: Ball
    _paddle: Paddle
    _deathZone: DeathZone
    _env: Environment
    _map: BlockMap

    def __init__(self):
        width, height = 700, 700
        paddleWidth = int(width / 5)
        paddleHeight = 10
        self._status = Status.RUNNING
        self._env = Environment(width, height)
        self._deathZone = DeathZone(0, height - 2, width, 2)
        self._paddle = Paddle(int((width - paddleWidth) / 2), height - 30, paddleWidth, paddleHeight)
        self._map = BlockMap(self._env.screen, 50, 50)
        self._ball = Ball(int(width / 2), int(height / 2))

    def tick(self):
        if self._map.isEmpty():
            self._status = Status.WIN
        self._env.draw()
        self._env.render(self._ball)
        self._env.render(self._map)
        self._env.render(self._deathZone)
        self._env.render(self._paddle)
        self._paddle.checkMovement(self._env.screen)
        self._ball.move()
        self._env.clips(self._ball)
        if self._ball.clips(self._deathZone):
            self._status = Status.LOSE
        self._map.checkCollisions(self._ball)
        self._ball.clips(self._paddle)
        for event in pygame.event.get():
            if event.type == PADDLE_HIT:
                self._ball.bounce(self._paddle)
            elif event.type == VERTICAL_CLIP:
                self._ball.changeVerticalMovement()
            elif event.type == HORIZONTAL_CLIP:
                self._ball.changeHorizontalMovement()
            if event.type == pygame.QUIT:
                self._status = Status.EXIT

    def isRunning(self):
        return self._status == Status.RUNNING

    def getStatus(self):
        return self._status
