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

class GameState(object):
    def __init__(self):
        self.state = "stationary"
        self.prev_state = "stationary"
        self.states = {"rotating","moving","stationary","paused"}

    def ChangeState(self,new_state):
        self.prev_state = self.state
        self.state = new_state

# Setup some pygame stuff here. Also callable class objects here to save
# time in the main game loop
pygame.init()

tilemap = gamemap.Map()
tilemap.levelmap = cfgLevels.level1
tilemap.LoadSurfaces()

hero = player.Player(tilemap)

screen = gamescreen.GameScreen(hero, tilemap)


gamestate = GameState()

clock = pygame.time.Clock()

def Moving(screen,hero):
    c = pygame.time.Clock()
    MOVING = True
    while MOVING:
        c.tick(100)
        print "hero.target_pos =",hero.target_pos
        hero.update()
        screen.Move()
        screen.update()
        print "new hero.current_pos =",hero.current_pos
        if hero.current_pos==hero.target_pos: MOVING = False

def Rotating(screen,hero):
    c = pygame.time.Clock()
    ROTATING = True
    while ROTATING:
        c.tick(100)
        hero.update()
        screen.update()
        if hero.current_angle==hero.target_angle: ROTATING = False

def Paused():
    c = pygame.time.Clock()
    PAUSED = True
    while PAUSED:
        c.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    PAUSED = False
                else: continue
            else: continue

def main():
    MAINGAME = True
    pressed_keys = []
    input_time = 0

    while MAINGAME:
        milliseconds = clock.tick(cfg.MAXFPS)
        input_time+=milliseconds
        if input_time>=cfg.GAMESPEED:
            input_time=0
            for event in pygame.event.get():
                evtType = event.type
                if evtType == pygame.QUIT: MAINGAME = False
                elif evtType == pygame.KEYDOWN:
                    pressed_keys.append(event.key)
                    if event.key == pygame.K_ESCAPE: MAINGAME = False
                    elif event.key == pygame.K_p: gamestate.ChangeState("paused")
                    elif event.key in cfg.MOVECMDS:
                        if event.key==hero.prev_move:
                            gamestate.ChangeState("moving")
                            hero.Move(event.key,tilemap)
                        else:
                            gamestate.ChangeState("rotating")
                            hero.Rotate(event.key)
                    else: pass
                elif evtType == pygame.KEYUP:
                    try:
                        pressed_keys.remove(event.key)
                    except ValueError:
                        pass
                else: continue
    
            if gamestate.state=="stationary":
                screen.update()
            elif gamestate.state=="moving":
                Moving(screen,hero)
                gamestate.ChangeState("stationary")
            elif gamestate.state=="rotating":
                Rotating(screen,hero)
                gamestate.ChangeState("stationary")
            elif gamestate.state=="paused":
                Paused()
                gamestate.ChangeState(gamestate.prev_state)
            else:
                print "Entered an unknown state"
                MAINGAME = False
    pygame.quit()

if __name__ == "__main__":
    main()
