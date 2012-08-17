import os
import pygame
import config.main as cfg
import config.player as cfgPlayer
import config.tiles as cfgTiles
import config.objects as objects

class Player(object):
    def __init__(self):
        self.orig_surf = pygame.image.load(os.path.join(cfg.SPRITEPATH,cfgPlayer.HEROIMAGE))
        self.surf = self.orig_surf
        self.rect = self.surf.get_rect()
        self.rect.topleft = (cfgTiles.CENTERTILE.x+cfgTiles.PLAYERSPACE, cfgTiles.CENTERTILE.y+cfgTiles.PLAYERSPACE)
        self.prev_move = 0
        self.current_pos = objects.Coord(0,0)
        self.target_pos = objects.Coord(0,0)

        self.current_angle = 0.
        self.target_angle = 0.

    def Move(self,keydown):
        if keydown == self.prev_move:
            pass
        elif keydown == pygame.K_DOWN:
            self.target_angle = -90.
            self.surf = pygame.transform.rotate( self.orig_surf,self.target_angle )
            self.prev_move = keydown
        elif keydown == pygame.K_RIGHT:
            self.target_angle = 0.
            self.surf = self.orig_surf
            self.prev_move = keydown
        elif keydown == pygame.K_LEFT:
            self.target_angle = 180.
            self.surf = pygame.transform.rotate( self.orig_surf, self.target_angle )
            self.prev_move = keydown
        elif keydown == pygame.K_UP:
            self.target_angle = 90.
            self.surf = pygame.transform.rotate( self.orig_surf, self.target_angle )
            self.prev_move = keydown
        else:
            print "Unknown direction passed:",keydown
        self.current_angle = self.target_angle

