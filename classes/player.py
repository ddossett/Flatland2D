import os
import pygame
import config.main as cfg
import config.player as cfgPlayer
import config.tiles as cfgTiles

class Player(object):
    def __init__(self):
        self.orig_surf = pygame.image.load(os.path.join(cfg.SPRITEPATH,cfgPlayer.HEROIMAGE))
        self.surf = self.orig_surf
        self.rect = self.surf.get_rect()
        self.rect.topleft = (cfgTiles.CENTERTILE.x+cfgTiles.PLAYERSPACE, cfgTiles.CENTERTILE.y+cfgTiles.PLAYERSPACE)
        self.prev_move = 0

    def Move(self,keydown):
        if keydown == self.prev_move:
            pass
        elif keydown == pygame.K_DOWN:
            self.surf = pygame.transform.rotate( self.orig_surf, -90 )
            self.prev_move = keydown
        elif keydown == pygame.K_RIGHT:
            self.surf = self.orig_surf
            self.prev_move = keydown
        elif keydown == pygame.K_LEFT:
            self.surf = pygame.transform.rotate( self.orig_surf, 180 )
            self.prev_move = keydown
        elif keydown == pygame.K_UP:
            self.surf = pygame.transform.rotate( self.orig_surf, 90 )
            self.prev_move = keydown
        else:
            print "Unknown direction passed:",keydown

