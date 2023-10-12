import pygame
from Game import Game
from Status import Status
if __name__ == "__main__":
    # Initialize pygame
    pygame.init()
    while True:
        game = Game()
        while game.isRunning():
            game.tick()
            # Update display and pause briefly
            pygame.display.flip()
            pygame.time.wait(25)
        if game.getStatus() == Status.EXIT:
            break
    pygame.quit()
