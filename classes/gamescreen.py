import pygame
import config.main as cfg
import config.objects as objects
import config.tiles as cfgTiles

class GameScreen(object):
    def __init__(self):
        self.screen = pygame.display.set_mode(cfg.SCREENSIZE)
        print cfg.SCREENSIZE
        pygame.display.set_caption(cfg.TITLE)
        self.camera_pos = objects.PixelPos(0,0)

    def BlitMap(self,level):
        self.screen.fill(cfg.COLOUR_BLACK)
#        for tilex in range(cfgTiles.NUMXTILES):
#            for tiley in range(cfgTiles.NUMYTILES):
        for y,row in enumerate(level.levelmap):
            for x,tilekey in enumerate(row):
                #                tilekey = level.levelmap[tilex][tiley]
                tile_surface = level.required_surfaces[tilekey]
                tile_rect = pygame.Rect(0, 0, cfgTiles.TILESIZE.w, cfgTiles.TILESIZE.h)
                tile_rect.left = x*cfgTiles.TILESIZE.w - self.camera_pos.x
                tile_rect.top = y*cfgTiles.TILESIZE.h - self.camera_pos.y
                self.screen.blit(tile_surface,tile_rect)

    def BlitPlayer(self,player):
        self.screen.blit(player.surf, player.rect)

    def AddPositions(self,tuple1,tuple2,scale):
        return objects.PixelPos(*[ (itup1+(scale*itup2)) for itup1, itup2 in zip(tuple1,tuple2) ])

    def Move(self,keydown):
        move_pos = (0,0)
        dx = cfgTiles.TILESIZE.w
        dy = cfgTiles.TILESIZE.h
        if keydown == pygame.K_DOWN:
            move_pos = (0,dy)
        elif keydown == pygame.K_RIGHT:
            move_pos = (dx,0)
        elif keydown == pygame.K_LEFT:
            move_pos = (-dx,0)
        elif keydown == pygame.K_UP:
            move_pos = (0,-dy)
        else:
            print "Unknown direction passed: ",keydown
        self.camera_pos = self.AddPositions( self.camera_pos, move_pos, 1)
