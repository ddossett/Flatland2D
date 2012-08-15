import pygame
import config.main as cfg
import config.objects as objects

class GameScreen(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(cfg.SCREENSIZE)
        pygame.display.set_caption(cfg.TITLE)

    def BlitMap(self,level):
        self.screen.fill(cfg.COLOUR_BLACK)
        for tilex in range(cfg.NUMXTILES):
            for tiley in range(cfg.NUMYTILES):
                tilekey = level.levelmap[tilex][tiley]
                tile_surface = level.required_surfaces[tilekey]
                tile_rect = pygame.Rect(0, 0, cfg.TILESIZE.w, cfg.TILESIZE.h)
                tile_rect.left = tilex*cfg.TILESIZE.w
                tile_rect.top = tiley*cfg.TILESIZE.h
                self.screen.blit(tile_surface,tile_rect)

    def BlitPlayer(self):
        pass

