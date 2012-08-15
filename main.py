import os, sys, pygame
from collections import namedtuple as ntuple

# Some named tuples that will come in handy
rgb = ntuple('RGB', 'r g b')
PixelSize = ntuple('PixelSize', 'w h')

# Config Options, put these into a config file later to be edited by menu (xml?)
HEROSIZE = PixelSize(32,32)
SCREENSIZE = PixelSize(HEROSIZE.w*16, HEROSIZE.h*16)
COLOUR_WHITE = rgb(255,255,255)
COLOUR_BLACK = rgb(0,0,0)
TITLE = "Flatland 2D" 
MAXFPS = 150

# Setup some pygame stuff here. Also callable class objects here to save
# time in the main game loop
pygame.init()
hero_surf = pygame.image.load(os.path.join("data/sprites","A-Square.png"))
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
RUNNING = True

while RUNNING:
    milliseconds = clock.tick(MAXFPS)
    screen.fill(COLOUR_WHITE)
    for event in pygame.event.get():
        evtType = event.type
        if evtType == pygame.QUIT: RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: RUNNING = False
            elif event.key == pygame.K_TAB: STATS = True
            else: pass
        else: continue

    hero_rect = hero_surf.get_rect()
    screen.blit(hero_surf, hero_rect)
    pygame.display.flip()
