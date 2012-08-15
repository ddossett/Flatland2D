import os, sys
import math
import pygame
# Get the setup constants from our config files
import config.main as cfg
import config.player as cfgPlayer
import config.objects as objects

# Setup some pygame stuff here. Also callable class objects here to save
# time in the main game loop
pygame.init()
hero_surf = pygame.image.load(os.path.join(cfg.SPRITEPATH,cfgPlayer.HEROIMAGE))
screen = pygame.display.set_mode(cfg.SCREENSIZE)
pygame.display.set_caption(cfg.TITLE)
clock = pygame.time.Clock()

def main():
    RUNNING = True
#    i,j = 0, 0
    while RUNNING:
        milliseconds = clock.tick(cfg.MAXFPS)
        screen.fill(cfg.COLOUR_WHITE)
        for event in pygame.event.get():
            evtType = event.type
            if evtType == pygame.QUIT: RUNNING = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: RUNNING = False
                else: pass
            else: continue
    
        hero_rect = hero_surf.get_rect()
#        hero_rect.center = ( TILESIZE.w*(1+i), TILESIZE.h*(1+j) )
        screen.blit(hero_surf, hero_rect)
        pygame.display.flip()
#        if i==15 or j==15:
#            RUNNING=False
#        i+=1
#        j+=1
#        pygame.time.delay(1000)
    pygame.quit()

if __name__ == "__main__":
    main()
