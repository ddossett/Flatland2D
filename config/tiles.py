# Defining the image files and special characters for the level tiles
import config.player as player
import config.objects as objects

NUMXTILES = 17
NUMYTILES = 17
PLAYERSPACE = 2
TILESIZE = objects.PixelSize(player.HEROSIZE.w+PLAYERSPACE,player.HEROSIZE.h+PLAYERSPACE)
CENTERTILE = objects.PixelPos(TILESIZE.w*(NUMXTILES-1)/2,TILESIZE.h*(NUMYTILES)/2)
TILEDICT = {}
TILEDICT["g"] = "tile-grass.png"
TILEDICT["d"] = "tile-dirt.png"
