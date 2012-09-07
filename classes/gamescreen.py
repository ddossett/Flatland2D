import pygame
import config.main as cfg
import config.objects as objects
import config.tiles as cfgTiles
import utils

class GameScreen(object):
    def __init__(self,player,level):
        self.screen = pygame.display.set_mode(cfg.SCREENSIZE,pygame.NOFRAME)
        print cfg.SCREENSIZE
        pygame.display.set_caption(cfg.TITLE)
        self.player = player
        self.level = level
        self.camera_pos = utils.PlayerPosToCamera(player.current_pos)

    def BlitMap(self):
        self.screen.fill(cfg.COLOUR_BLACK)
        self.level.levelRect.topleft = self.camera_pos
        self.screen.blit( self.level.levelSurface, self.level.levelRect)

    def BlitPlayer(self):
        self.screen.blit(self.player.image, self.player.rect)

    def Move(self):
        self.camera_pos = utils.PlayerPosToCamera(self.player.current_pos)

    def TileToPixel(self,tile_pos):
        x = tile_pos[0]*cfgTiles.TILESIZE.w
        y = tile_pos[1]*cfgTiles.TILESIZE.h
        return objects.PixelPos(x,y)

    def HeroToScreenIndex(self,hero_pos):
        x_diff = (cfgTiles.NUMXTILES-1)/2
        y_diff = (cfgTiles.NUMYTILES-1)/2
        index = (x_diff+hero_pos[0],y_diff+hero_pos[1])
        return index

    def update(self,fps):
        myFont = pygame.font.SysFont("None", 30)
        self.BlitMap()
        self.BlitPlayer()
        self.screen.blit(myFont.render("FPS: %.2f" %fps, 0, (0, 0, 0)), (10,10))
        pygame.display.flip()
