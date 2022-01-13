import pygame, sys
from pygame.locals import *
import brick
import paddle

#timing
time = pygame.time.Clock()
# Constants that will be used in the program
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
PADDLE_Y_OFFSET = 30
BRICKS_PER_ROW = 10
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
GREEN =(0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
colours = [RED, ORANGE, YELLOW, GREEN, CYAN]

pygame.init()
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill((255, 255, 255))

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)
x_pos = BRICK_SEP
for colour in range (len(colours)):
    selected_colour = colours[colour]
    y_pos = BRICK_Y_OFFSET
    y_pos = y_pos + (BRICK_SEP * 2 + BRICK_HEIGHT * 2) * colour
    for c in range(2):
        y_pos = y_pos + (BRICK_SEP + BRICK_HEIGHT) * c
        for r in range(BRICKS_PER_ROW):
            b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, selected_colour)
            b.rect.x = x_pos + ((BRICK_WIDTH + BRICK_SEP) * r)
            b.rect.y = y_pos
            mainsurface.blit(b.image, b.rect)

p =


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==
    pygame.display.update()
    time.tick(60)
