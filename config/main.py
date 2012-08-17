# Main screen and game loop config settings
import math
import pygame
import config.player as player
import config.objects as objects
import config.tiles as tiles

SCREENSIZE = objects.PixelSize(tiles.TILESIZE.w*tiles.NUMXTILES, tiles.TILESIZE.h*tiles.NUMYTILES)
COLOUR_WHITE = objects.rgb(255,255,255)
COLOUR_BLACK = objects.rgb(0,0,0)
TITLE = "Flatland 2D" 
MAXFPS = 100
SPRITEPATH = "data/sprites"
TILEPATH = "data/map"
LEVELPATH = "data/map"
MOVECMDS = {pygame.K_UP,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_LEFT}
MOVETIME = 250
