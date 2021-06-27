import sys
import math
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, Rect

WIDTH, HEIGHT = (600, 800)

class Block:
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) + 270

    def move(self):
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)


def tick():
    """
    Per Frame Handling
    """

    global BLOCKS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                PADDLE.rect.centerx -= 10
            elif event.key == K_RIGHT:
                PADDLE.rect.centery += 10

    if BALL.rect.centery < 1000:
        BALL.move()

    prevlen = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]

    if len(BLOCKS) != prevlen:
        BALL.dir *= -1

    if PADDLE.rect.colliderect(BALL.rect):
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) \
                / PADDLE.rect.width * 80

    if BALL.rect.centerx < 0 or BALL.rect.centerx > WIDTH:
        BALL.dir = 180 - BALL.dir

    if BALL.rect.centery < 0:
        BALL.dir = -BALL.dir
        BALL.speed = 15

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE = Block((242, 242, 0), Rect(300, 700, 100, 30))
BALL = Block((242, 242, 0), Rect(300, 400, 20, 20), 10)

def main():
    myfont = pygame.font.SysFont(None, 80)
    msg_renderer = lambda msg: myfont.render(msg, True, (255, 255, 0))
    fps = 30
    colors = [
        (255, 0, 0),
        (255, 165, 0),
        (242, 242, 0),
        (0, 128, 0),
        (128, 0, 128),
        (0, 0, 250)
    ]

    for ypos, color in enumerate(colors, start=0):
        for xpos in range(0, 5):
            BLOCKS.append(Block(color,
                                Rect(xpos * 100 + 60,
                                     ypos * 50 + 40,
                                     80, 30))
                         )

    while True:
        tick()

        SURFACE.fill((0, 0, 0))
        BALL.draw()
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(msg_renderer("Cleared"), (200, 400))
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            SURFACE.blit(msg_renderer("Game Over"), (150, 400))

        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == "__main__":
    main()