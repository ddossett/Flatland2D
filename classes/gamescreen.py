import pygame
import config.main as cfg
import config.objects as objects
import config.tiles as cfgTiles

class GameScreen(object):
    def __init__(self,player,tilemap):
        self.screen = pygame.display.set_mode(cfg.SCREENSIZE)
        print cfg.SCREENSIZE
        pygame.display.set_caption(cfg.TITLE)
        self.camera_pos = objects.PixelPos(0,0)
        self.tile_pos = [0,0]
        self.player = player
        self.tilemap = tilemap

    def BlitMap(self,level):
        self.screen.fill(cfg.COLOUR_BLACK)
        for y,row in enumerate(level.levelmap):
            for x,tilekey in enumerate(row):
                tile_surface = level.required_surfaces[tilekey]
                tile_rect = pygame.Rect(0, 0, cfgTiles.TILESIZE.w, cfgTiles.TILESIZE.h)
                tile_rect.left = x*cfgTiles.TILESIZE.w - self.camera_pos.x
                tile_rect.top = y*cfgTiles.TILESIZE.h - self.camera_pos.y
                self.screen.blit(tile_surface,tile_rect)

    def BlitPlayer(self,player):
        self.screen.blit(player.image, player.rect)

    def AddPositions(self,tuple1,tuple2,scale):
        return tuple([ (itup1+(scale*itup2)) for itup1, itup2 in zip(tuple1,tuple2) ])

    def Move(self,keydown,level):
        move_pos = (0,0)
        if keydown == pygame.K_DOWN:
            move_pos = (0,1)
        elif keydown == pygame.K_RIGHT:
            move_pos = (1,0)
        elif keydown == pygame.K_LEFT:
            move_pos = (-1,0)
        elif keydown == pygame.K_UP:
            move_pos = (0,-1)
        else:
            print "Unknown direction passed: ",keydown
        tile_pos = self.AddPositions( self.tile_pos, move_pos, 1)
        map_pos = self.HeroToScreenIndex(tile_pos)
        if level.levelmap[map_pos[1]][map_pos[0]] not in cfgTiles.UNWALKABLE:
            self.tile_pos = tile_pos
        self.camera_pos = self.TileToPixel( self.tile_pos )

    def TileToPixel(self,tile_pos):
        x = tile_pos[0]*cfgTiles.TILESIZE.w
        y = tile_pos[1]*cfgTiles.TILESIZE.h
        return objects.PixelPos(x,y)

    def HeroToScreenIndex(self,hero_pos):
        x_diff = (cfgTiles.NUMXTILES-1)/2
        y_diff = (cfgTiles.NUMYTILES-1)/2
        index = (x_diff+hero_pos[0],y_diff+hero_pos[1])
        return index

    def update(self):
        self.BlitMap(self.tilemap)
        self.BlitPlayer(self.player)
        pygame.display.flip()
