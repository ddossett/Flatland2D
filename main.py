import os, sys
import math
import pygame
# Get the setup constants from our config files
import config.main as cfg
import config.player as cfgPlayer
import config.objects as objects
import config.levels as cfgLevels
import classes.gamescreen as gamescreen
import classes.gamemap as gamemap

sys.path.append("config")
sys.path.append("classes")

# Setup some pygame stuff here. Also callable class objects here to save
# time in the main game loop
pygame.init()
hero_surf = pygame.image.load(os.path.join(cfg.SPRITEPATH,cfgPlayer.HEROIMAGE))
clock = pygame.time.Clock()
screen = gamescreen.GameScreen()
tilemap = gamemap.Map()
tilemap.levelmap = cfgLevels.level1
tilemap.LoadSurfaces()

def main():
    RUNNING = True
    while RUNNING:
        milliseconds = clock.tick(cfg.MAXFPS)
        for event in pygame.event.get():
            evtType = event.type
            if evtType == pygame.QUIT: RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: RUNNING = False
                else: pass
            else: continue
        screen.BlitMap(tilemap)
        hero_rect = hero_surf.get_rect()
        screen.screen.blit(hero_surf, hero_rect)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
