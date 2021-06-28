import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400, 200))

def main():
    while True:
        SURFACE.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            
            pygame.display.update()


if __name__ == "__main__":
    main()
