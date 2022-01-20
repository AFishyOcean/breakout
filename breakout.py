import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball

#timing
time = pygame.time.Clock()
# Constants that will be used in the program
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
PADDLE_Y_OFFSET = 30
BRICKS_PER_ROW = 10
BRICKS_PER_COLUMN = 2
BRICK_SEP = 4  # The space between each brick
BRICK_Y_OFFSET = 70
BRICK_WIDTH = int((APPLICATION_WIDTH - (BRICKS_PER_ROW * BRICK_SEP)) / BRICKS_PER_ROW)
BRICK_HEIGHT = 8
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
RADIUS_OF_BALL = 10
NUM_TURNS = 3

# Sets up the colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colours = [RED, ORANGE, YELLOW, GREEN, CYAN]

pygame.init()
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill(BLACK)

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)
x_pos = BRICK_SEP
bricks_col = pygame.sprite.Group()
for colour in range(len(colours)):
    selected_colour = colours[colour]
    y_pos = BRICK_Y_OFFSET
    y_pos = y_pos + (BRICK_SEP * 2 + BRICK_HEIGHT * 2) * colour
    for c in range(BRICKS_PER_COLUMN):
        y_pos = y_pos + (BRICK_SEP + BRICK_HEIGHT) * c
        for r in range(BRICKS_PER_ROW):
            b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, selected_colour)
            bricks_col.add(b)
            b.rect.x = x_pos + ((BRICK_WIDTH + BRICK_SEP) * r)
            b.rect.y = y_pos
            mainsurface.blit(b.image, b.rect)
# paddle code
paddle_col = pygame.sprite.Group()
p = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
p.rect.x = APPLICATION_WIDTH / 2
p.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
paddle_col.add(p)
mainsurface.blit(p.image, p.rect)
# ball code
ba = ball.Ball(WHITE, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
ba.rect.x = APPLICATION_WIDTH / 2
ba.rect.y = APPLICATION_HEIGHT / 2
mainsurface.blit(ba.image, ba.rect)

while True:
    mainsurface.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            p.move(pygame.mouse.get_pos())
    for r in bricks_col:
        mainsurface.blit(r.image, r.rect)
    ba.move()
    mainsurface.blit(p.image, p.rect)
    mainsurface.blit(ba.image, ba.rect)
    ba.collide_bricks(bricks_col)
    ba.collide_paddle(paddle_col)
    pygame.display.update()
    time.tick(60)
