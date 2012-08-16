# Defining the image files and special characters for the level tiles
import config.player as player
import config.objects as objects

NUMXTILES = 15
NUMYTILES = 15
PLAYERSPACE = 5
TILESIZE = objects.PixelSize(player.HEROSIZE.w+(2*PLAYERSPACE),player.HEROSIZE.h+(2*PLAYERSPACE))
CENTERTILE = objects.PixelPos(TILESIZE.w*(NUMXTILES-1)/2,TILESIZE.h*(NUMYTILES-1)/2)
TILEDICT = {}
TILEDICT["v"] = "tile-grass.png"
TILEDICT["#"] = "tile-dirt.png"
TILEDICT["~"] = "tile-water.png"
