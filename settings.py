import pygame as pg
# Game settings
WIDTH  = 800
HEIGHT = 600
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
SPD_T   = 0.1

# Textures
FILLED = pg.image.load('img/1.bmp')
LL     = pg.image.load('img/2.bmp')
UL     = pg.image.load('img/3.bmp')
UR     = pg.image.load('img/4.bmp')
LR     = pg.image.load('img/5.bmp')
EMPTY  = pg.image.load('img/6.bmp')


# Map settings
SIZE_OF_BLOCK = 40

# 800x600 with SOB=40 -  20x15 blocks