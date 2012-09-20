# Main screen and game loop config settings
import math
from collections import namedtuple as ntuple
import pygame
import tuple_utils

rgb = ntuple('RGB', 'r g b')
PixelSize = ntuple('PixelSize', 'w h')
PixelPos = ntuple('PixelPos', 'x y')
Coord = ntuple('Coord', 'x y')

game =  {   "move_cmds":{pygame.K_UP,pygame.K_RIGHT,pygame.K_DOWN,pygame.K_LEFT},
            "title":"Flatland 2D"
        }

timing =    {   "fps":100,
                "move":5,
                "input":5,
            }

colours =   {   "black":rgb(0,0,0),
                "white":rgb(255,255,255)
            }

player =    {   "size":PixelSize(32,32),
                "image":"a-square.png",
                "rotate_speed":0.2,
                "move_speed":0.2,
                "space":5
            }

paths = {   "sprite":"data/sprites",
            "tile":"data/map",
            "level":"data/map",
        }

tiles = {   "size":PixelSize( *tuple_utils.AddToTuple(player["size"],(2*player["space"])) ),
            "number":Coord(15,15),
            "centre":PixelPos(0,0),
            "dict":{},
            "unwalkable":[]
        }

tiles["centre"] = PixelSize( *tuple_utils.MultiplyTuples( tuple_utils.ScaleTuple( tuple_utils.AddToTuple(tiles["number"],-1), 0.5), tiles["size"] ) )
tiles["dict"]["v"] = "tile-grass.png"
tiles["dict"]["#"] = "tile-dirt.png"
tiles["dict"]["~"] = "tile-water.png"
tiles["unwalkable"].append("~")

screen =    {   "size":PixelSize( *tuple_utils.MultiplyTuples(tiles["size"],tiles["number"]) )
            }
