# Main screen and game loop config settings
import player
import objects
import math

TILEPOWER = 3
NUMXTILES = 16
NUMYTILES = 16
TILESIZE = objects.PixelSize(player.HEROSIZE.w+math.pow(player.HEROSIZE.w,1./TILEPOWER), player.HEROSIZE.h+math.pow(player.HEROSIZE.h,1./TILEPOWER))
SCREENSIZE = objects.PixelSize(int(TILESIZE.w*NUMXTILES), int(TILESIZE.h*NUMYTILES))
COLOUR_WHITE = objects.rgb(255,255,255)
COLOUR_BLACK = objects.rgb(0,0,0)
TITLE = "Flatland 2D" 
MAXFPS = 150
SPRITEPATH = "data/sprites"
