import pygame
import config.main as cfg
import config.objects as objects
import config.tiles as cfgTiles

class GameScreen(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(cfg.SCREENSIZE)
        print cfg.SCREENSIZE
        pygame.display.set_caption(cfg.TITLE)

    def BlitMap(self,level):
        self.screen.fill(cfg.COLOUR_BLACK)
        for tilex in range(cfgTiles.NUMXTILES):
            for tiley in range(cfgTiles.NUMYTILES):
                tilekey = level.levelmap[tilex][tiley]
                tile_surface = level.required_surfaces[tilekey]
                tile_rect = pygame.Rect(0, 0, cfgTiles.TILESIZE.w, cfgTiles.TILESIZE.h)
                tile_rect.left = tilex*cfgTiles.TILESIZE.w
                tile_rect.top = tiley*cfgTiles.TILESIZE.h
                self.screen.blit(tile_surface,tile_rect)

    def BlitPlayer(self):
        pass

