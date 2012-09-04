import os
import pygame
import config.main as cfg
import config.player as cfgPlayer
import config.tiles as cfgTiles
import config.objects as objects
import utils

class Player(pygame.sprite.Sprite):
    def __init__(self,level):
        pygame.sprite.Sprite.__init__(self)
        self.orig_surf = pygame.image.load(os.path.join(cfg.SPRITEPATH,cfgPlayer.HEROIMAGE))
        self.image = self.orig_surf
        self.rect = self.image.get_rect()
        self.rect.topleft = utils.AddToTuple( cfgTiles.CENTERTILE, cfgTiles.PLAYERSPACE )

        self.current_angle = 0
        self.target_angle = 0

        # Since starting angle is 0, player faces right when first drawn
        self.prev_move = pygame.K_RIGHT

        # Use the level starting position to set our current position
        self.current_pos = objects.Coord( *utils.ScaleTuple(level.start_pos,1.0) )
        self.target_pos = self.current_pos

    def Move(self,keydown,level):
            print "old hero.current_pos =",self.current_pos
            if keydown == pygame.K_DOWN:
                self.target_pos = objects.Coord( *utils.AddTuples(self.current_pos,(0.,1.)) )
            elif keydown == pygame.K_RIGHT:
                self.target_pos = objects.Coord( *utils.AddTuples(self.current_pos,(1.,0.)) )
            elif keydown == pygame.K_LEFT:
                self.target_pos = objects.Coord( *utils.AddTuples(self.current_pos,(-1.,0.)) )
            elif keydown == pygame.K_UP:
                self.target_pos = objects.Coord( *utils.AddTuples(self.current_pos,(0.,-1.)) )
            else: print "Unknown Direction Passed!"
            if level.levelmap[int(self.target_pos.x)][int(self.target_pos.y)] in cfgTiles.UNWALKABLE:
                self.target_pos = self.current_pos
            elif self.target_pos.x<0. or self.target_pos.y<0.: self.target_pos = self.current_pos
            self.prev_move = keydown

    def Rotate(self,keydown):
        if keydown == pygame.K_DOWN:
            self.target_angle = 270
        elif keydown == pygame.K_RIGHT:
            self.target_angle = 0
        elif keydown == pygame.K_LEFT:
            self.target_angle = 180
        elif keydown == pygame.K_UP:
            self.target_angle = 90
        self.prev_move = keydown
    
    def update(self):
        if self.target_angle != self.current_angle:
            if self.target_angle<self.current_angle:
                self.current_angle -= cfgPlayer.ROTATESPEED
            elif self.target_angle>self.current_angle:
                self.current_angle += cfgPlayer.ROTATESPEED
            self.image = pygame.transform.rotate( self.orig_surf, self.current_angle )
        elif self.target_pos != self.current_pos:
            neg_current_pos = utils.ScaleTuple(self.current_pos, -1.)
            move_vec = utils.ScaleTuple( utils.AddTuples( neg_current_pos, self.target_pos ), 0.5 )
            print "move_vec",move_vec
            if abs(move_vec[0])<0.005 and abs(move_vec[1])<0.005:
                self.current_pos = self.target_pos
            else:
                self.current_pos = objects.Coord( *utils.AddTuples( self.current_pos, move_vec ) )
        else: pass
