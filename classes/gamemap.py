import os
import Image
import pygame
import config.main as cfg
import tuple_utils
import utils

class Map(object):
    def __init__(self):
        self.levelmap = []
        self.required_images = {}
        self.start_pos = cfg.Coord(10.,10.)
    
    def LoadImages(self):
        """We fill in the required_images set with the resized tiles. Only
        tiles used in the level will be loaded, to save memory. This
        is then used by the MakeLevelImage() function to build a larger
        level image."""
        for key in self.required_images.keys():
            del self.required_images[key]
        all_images = {}
        for tilekey in cfg.tiles["dict"].keys():
            image_file = cfg.tiles["dict"][tilekey]
            tile_image = Image.open(os.path.join(cfg.paths["tile"],image_file))
            tile_image = tile_image.resize( cfg.tiles["size"] )
            all_images[tilekey] = tile_image
        for tilekey_row in self.levelmap:
            for tilekey in tilekey_row:
                if not self.required_images.has_key(tilekey):
                    self.required_images[tilekey] = all_images[tilekey]

    def MakeBackgroundSurface(self):
        """To save time we create the base level background as a single
        image using the Image module. This can then be made into a single
        large surface and scrolled around. This saves time compared to 
        blitting each tile individually every frame"""
        
        self.LoadImages()
        # Set the size of the level image required and save memory for it
        numy = len(self.levelmap)
        numx = len(self.levelmap[0])
        self.levelImage = Image.new("RGBA", tuple_utils.MultiplyTuples( cfg.tiles["size"], (numx,numy)) )

        for y,row in enumerate(self.levelmap):
            for x,tilekey in enumerate(row):
                tile_pos = (x*cfg.tiles["size"].w, y*cfg.tiles["size"].h, (x+1)*cfg.tiles["size"].w, (y+1)*cfg.tiles["size"].h)
                tile_image = self.required_images[tilekey]
                self.levelImage.paste( tile_image, tile_pos )
        self.levelSurface = pygame.image.frombuffer( self.levelImage.tostring(), self.levelImage.size, self.levelImage.mode )
        self.rect = self.levelSurface.get_rect()
        self.rect.topleft = utils.PlayerPosToCamera(self.start_pos)
 
