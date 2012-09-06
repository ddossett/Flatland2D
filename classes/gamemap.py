import os
import Image
import pygame
import config.main as cfg
import config.tiles as cfgTiles
import config.objects as objects
import utils

class Map(object):
    def __init__(self):
        self.levelmap = []
        self.required_images = {}
        self.start_pos = objects.Coord(3.,3.)
    
    def LoadImages(self):
        """We fill in the required_images set with the resized tiles. Only
        tiles used in the level will be loaded, to save memory. This
        is then used by the MakeLevelImage() function to build a larger
        level image."""
        for key in self.required_images.keys():
            del self.required_images[key]
        all_images = {}
        for tilekey in cfgTiles.TILEDICT.keys():
            image_file = cfgTiles.TILEDICT[tilekey]
            tile_image = Image.open(os.path.join(cfg.TILEPATH,image_file))
            tile_image = tile_image.resize( cfgTiles.TILESIZE )
            all_images[tilekey] = tile_image
        for tilekey_row in self.levelmap:
            for tilekey in tilekey_row:
                if not self.required_images.has_key(tilekey):
                    self.required_images[tilekey] = all_images[tilekey]

    def MakeLevelImage(self):
        """To save time we create the base level background as a single
        image using the Image module. This can then be made into a single
        large surface and scrolled around. This saves time compared to 
        blitting each tile individually every frame"""
        
        self.LoadImages()
        # Set the size of the level image required and save memory for it
        numy = len(self.levelmap)
        numx = len(self.levelmap[0])
        self.levelImage = Image.new("RGBA", utils.MultiplyTuples( cfgTiles.TILESIZE, (numx,numy)) )

        for y,row in enumerate(self.levelmap):
            for x,tilekey in enumerate(row):
                tile_pos = (x*cfgTiles.TILESIZE.w, y*cfgTiles.TILESIZE.h, (x+1)*cfgTiles.TILESIZE.w, (y+1)*cfgTiles.TILESIZE.h)
                tile_image = self.required_images[tilekey]
                self.levelImage.paste( tile_image, tile_pos )
        self.levelImage.show()
 
