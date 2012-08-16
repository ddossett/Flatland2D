import os
import pygame
import config.main as cfg
import config.tiles as cfgTiles

class Map(object):
    def __init__(self):
        self.levelmap = []
        self.required_surfaces = {}
    
    def LoadSurfaces(self):
        for key in self.required_surfaces.keys():
            del required_surfaces[key]
        all_surfaces = {}
        for tilekey in cfgTiles.TILEDICT.keys():
            image_file = cfgTiles.TILEDICT[tilekey]
            tile_surface = pygame.image.load(os.path.join(cfg.TILEPATH,image_file))
            tile_surface = pygame.transform.scale( tile_surface, cfgTiles.TILESIZE )
            all_surfaces[tilekey] = tile_surface
        for tilekey_row in self.levelmap:
            for tilekey in tilekey_row:
                if not self.required_surfaces.has_key(tilekey):
                    self.required_surfaces[tilekey] = all_surfaces[tilekey]
