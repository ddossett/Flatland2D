import os
import pygame
import config.main as cfg
import utils
import tuple_utils

class Player(pygame.sprite.Sprite):
    def __init__(self,level):
        pygame.sprite.Sprite.__init__(self)
        self.orig_surf = pygame.image.load(os.path.join(cfg.paths["sprite"],cfg.player["image"]))
        self.image = self.orig_surf
        self.rect = self.image.get_rect()
        self.rect.topleft = tuple_utils.AddToTuple( cfg.tiles["centre"], cfg.player["space"] )

        self.current_angle = 0.
        self.target_angle = 0.
        self.rel_angle = 0.

        # Since starting angle is 0, player faces right when first drawn
        self.prev_move = pygame.K_RIGHT
        self.rotating = False

        # Use the level starting position to set our current position
        self.current_pos = cfg.Coord( *tuple_utils.ScaleTuple(level.start_pos,1.0) )
        self.target_pos = self.current_pos

        self.velocity = cfg.Coord(0.,0.)

    def Move(self,keydown,level):
        # Figure out which movement was sent 
        if keydown == pygame.K_DOWN:
            self.target_pos = cfg.Coord( *tuple_utils.AddTuples(self.current_pos,(0.,1.)) )
        elif keydown == pygame.K_RIGHT:
            self.target_pos = cfg.Coord( *tuple_utils.AddTuples(self.current_pos,(1.,0.)) )
        elif keydown == pygame.K_LEFT:
            self.target_pos = cfg.Coord( *tuple_utils.AddTuples(self.current_pos,(-1.,0.)) )
        elif keydown == pygame.K_UP:
            self.target_pos = cfg.Coord( *tuple_utils.AddTuples(self.current_pos,(0.,-1.)) )
        else: print "Unknown Direction Passed!"
        if level.levelmap[int(self.target_pos.y)][int(self.target_pos.x)] in cfg.tiles["unwalkable"]:
            self.target_pos = self.current_pos
        elif self.target_pos.x<0. or self.target_pos.y<0.: self.target_pos = self.current_pos
        # Calculate the velocity to be used in the update() call
        neg_current_pos = tuple_utils.ScaleTuple(self.current_pos, -1.)
        self.velocity = cfg.Coord( *tuple_utils.ScaleTuple( tuple_utils.AddTuples( neg_current_pos, self.target_pos ), cfg.player["move_speed"] ) )
        self.prev_move = keydown

    def Rotate(self,keydown):
        if self.prev_move == pygame.K_RIGHT:
            if keydown == pygame.K_DOWN:
                self.rel_angle = -90.
            elif keydown == pygame.K_RIGHT:
                self.rel_angle = 0.
            elif keydown == pygame.K_LEFT:
                self.rel_angle = 180.
            elif keydown == pygame.K_UP:
                self.rel_angle = 90.
        elif self.prev_move == pygame.K_LEFT:
            if keydown == pygame.K_DOWN:
                self.rel_angle = 90.
            elif keydown == pygame.K_RIGHT:
                self.rel_angle = 180.
            elif keydown == pygame.K_LEFT:
                self.rel_angle = 0.
            elif keydown == pygame.K_UP:
                self.rel_angle = -90.
        elif self.prev_move == pygame.K_UP:
            if keydown == pygame.K_DOWN:
                self.rel_angle = 180.
            elif keydown == pygame.K_RIGHT:
                self.rel_angle = -90.
            elif keydown == pygame.K_LEFT:
                self.rel_angle = 90.
            elif keydown == pygame.K_UP:
                self.rel_angle = 0.
        elif self.prev_move == pygame.K_DOWN:
            if keydown == pygame.K_DOWN:
                self.rel_angle = 0.
            elif keydown == pygame.K_RIGHT:
                self.rel_angle = 90.
            elif keydown == pygame.K_LEFT:
                self.rel_angle = -90.
            elif keydown == pygame.K_UP:
                self.rel_angle = 180.
        else: pass
        self.target_angle = (self.current_angle + self.rel_angle)%360
        self.rotating = True
        self.prev_move = keydown
    
    def update(self):
        if self.rotating==True:
            self.current_angle += cfg.player["rotate_speed"]*self.rel_angle
            self.current_angle = self.current_angle%360
            if abs(self.current_angle - self.target_angle)<10:
                self.current_angle = self.target_angle
                self.rel_angle = 0.
                self.rotating=False
            self.image = pygame.transform.rotate( self.orig_surf, self.current_angle )

        elif self.target_pos != self.current_pos:
            neg_current_pos = tuple_utils.ScaleTuple(self.current_pos, -1.)
            diff = tuple_utils.AddTuples( neg_current_pos, self.target_pos )
            if abs(diff[0])<0.005 and abs(diff[1])<0.005:
                self.current_pos = self.target_pos
                self.velocity = cfg.Coord(0.,0.)
            else:
                self.current_pos = cfg.Coord( *tuple_utils.AddTuples( self.current_pos, self.velocity ) )
        else: pass
