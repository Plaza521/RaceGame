import pygame as pg
# Game settings
WIDTH  = 1000
HEIGHT = 800
H_WIDTH  = WIDTH//2
H_HEIGHT = HEIGHT//2
FPS    = 30

# Colors
WHITE    = (255,255,255)
BLACK    = (0  ,0  ,0  )
RED      = (220,0  ,0  )
GREEN    = (0  ,220,0  )
BLUE     = (0  ,0  ,220)
GRAY     = (192,192,192)
DARKGRAY = (110,110,110)
PURPLE   = (120,0  ,120)
SKYBLUE  = (0  ,186,255)
YELLOW   = (220,220,0  )
SANDY    = (244,164,96 )

# Car settings
FORWARD = pg.K_w
BACK    = pg.K_s
LEFT    = pg.K_a
RIGHT   = pg.K_d
SPEED   = 1
SPD_T   = 0.05

# Textures
EMPTY  = pg.image.load('img/0.bmp')
FILLED = pg.image.load('img/1.bmp')
LLO    = pg.image.load('img/2.bmp')
ULO    = pg.image.load('img/3.bmp')
URO    = pg.image.load('img/4.bmp')
LRO    = pg.image.load('img/5.bmp')
LLI    = pg.image.load('img/6.bmp')
ULI    = pg.image.load('img/7.bmp')
URI    = pg.image.load('img/8.bmp')
LRI    = pg.image.load('img/9.bmp')


# Map settings
SIZE_OF_BLOCK = 40
HALF_OF_BLOCK = SIZE_OF_BLOCK / 2
QUAD_OF_BLOCK = SIZE_OF_BLOCK / 4