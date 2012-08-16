import os, sys
import math
import pygame

# Get the setup constants from our config files
import config.main as cfg
import config.player as cfgPlayer
import config.objects as objects
import config.levels as cfgLevels
import config.tiles as cfgTiles
import classes.gamescreen as gamescreen
import classes.gamemap as gamemap
import classes.player as player

# Setup some pygame stuff here. Also callable class objects here to save
# time in the main game loop
pygame.init()

hero = player.Player()
clock = pygame.time.Clock()
screen = gamescreen.GameScreen()

tilemap = gamemap.Map()
tilemap.levelmap = cfgLevels.level1
tilemap.LoadSurfaces()

def main():
    RUNNING = True
    pressed_keys = []
    time_move = 0
    while RUNNING:
        milliseconds = clock.tick(cfg.MAXFPS)
        time_move+=milliseconds
        for event in pygame.event.get():
            evtType = event.type
            if evtType == pygame.QUIT: RUNNING = False
            elif evtType == pygame.KEYDOWN:
                pressed_keys.append(event.key)
                if event.key == pygame.K_ESCAPE: RUNNING = False
                elif event.key in cfg.MOVECMDS:
                    if event.key==hero.prev_move:
                        if time_move>cfg.MOVETIME:
                            screen.Move(event.key)
                            time_move=0
                    else:
                        hero.Move(event.key)
                        time_move=0
                else: pass
            elif evtType == pygame.KEYUP:
                pressed_keys.remove(event.key)
            else: continue

        for key in pressed_keys:
            if key in cfg.MOVECMDS:
                if time_move>cfg.MOVETIME:
                    screen.Move(event.key)
                    time_move=0

        screen.BlitMap(tilemap)
        screen.BlitPlayer(hero)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
