import os
import pygame
import config.main as cfg
import config.player as cfgPlayer
import config.tiles as cfgTiles
import config.objects as objects

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.orig_surf = pygame.image.load(os.path.join(cfg.SPRITEPATH,cfgPlayer.HEROIMAGE))
        self.image = self.orig_surf
        self.rect = self.image.get_rect()
        self.rect.topleft = (cfgTiles.CENTERTILE.x+cfgTiles.PLAYERSPACE, cfgTiles.CENTERTILE.y+cfgTiles.PLAYERSPACE)
        self.prev_move = 0
        self.current_pos = objects.Coord(0,0)
        self.target_pos = objects.Coord(0,0)

        self.current_angle = 0
        self.target_angle = 0

    def Move(self,keydown):
        if keydown == self.prev_move:
            pass
        elif keydown == pygame.K_DOWN:
            self.target_angle = 270
            self.prev_move = keydown
        elif keydown == pygame.K_RIGHT:
            self.target_angle = 0
            self.prev_move = keydown
        elif keydown == pygame.K_LEFT:
            self.target_angle = 180
            self.prev_move = keydown
        elif keydown == pygame.K_UP:
            self.target_angle = 90
            self.prev_move = keydown
        else:
            print "Unknown direction passed:",keydown
#        self.current_angle = self.target_angle
    
    def update(self):
        if self.target_angle is not self.current_angle:
            if self.target_angle<self.current_angle:
                self.current_angle -= cfgPlayer.ROTATESPEED
            elif self.target_angle>self.current_angle:
                self.current_angle += cfgPlayer.ROTATESPEED
        else: pass
        self.image = pygame.transform.rotate( self.orig_surf, self.current_angle )

