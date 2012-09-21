import pygame
import config.main as cfg
import utils
import tuple_utils

class GameScreen(object):
    def __init__(self,player,npcGroup,level):
        self.screen = pygame.display.set_mode(cfg.screen["size"],pygame.NOFRAME)
        print cfg.screen["size"]
        pygame.display.set_caption(cfg.game["title"])
        self.player = player
        self.level = level
        self.camera_pos = utils.PlayerPosToCamera(player.current_pos)
        self.npcGroup = npcGroup

    def BlitMap(self):
        self.screen.fill(cfg.colours["black"])
        self.level.rect.topleft = self.camera_pos
        self.screen.blit( self.level.levelSurface, self.level.rect)

    def BlitPlayer(self):
        self.screen.blit(self.player.image, self.player.rect)

    def BlitNPCs(self):
        for character in self.npcGroup.sprites():
            character.rect.topleft = tuple_utils.AddTuples(self.camera_pos,character.rect.topleft)
            self.screen.blit(character.image, character.rect)

    def Move(self):
        self.camera_pos = utils.PlayerPosToCamera(self.player.current_pos)

    def update(self,fps):
        myFont = pygame.font.SysFont("None", 30)
        self.BlitMap()
        self.BlitPlayer()
        self.BlitNPCs()
        self.screen.blit(myFont.render("FPS: %.2f" %fps, 0, (0, 0, 0)), (10,10))
        pygame.display.flip()
