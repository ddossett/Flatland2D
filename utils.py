# Some helpful functions to be used all over the place.
# Mostly tuple mathematics atm. Switching to numpy arrays
# might be an option in the future if this gets out of hand.

from config.main import tiles as cfgTiles
from config.main import player as cfgPlayer
import tuple_utils

def TileCoordToPos(coord):
    return tuple_utils.MultiplyTuples(cfgTiles["size"],coord)

def TilePosToPlayerPos(tile_pos):
    """Since the player square rect is actually smaller than the normal tiles
    we have to convert a tile topleft pixel position into a square topleft position."""
    return tuple_utils.AddToTuple( tile_pos, cfgPlayer["space"] )

def PlayerPosToTilePos(player_pos):
    """Since the player square rect is actually smaller than the normal tiles
    we have to convert a player topleft pixel position into a tile topleft position."""

    return tuple_utils.AddToTuple( tile_pos, -cfgPlayer["space"] )

def PlayerPosToCamera(player_pos):
    """Player Position is here defined as the topleft of the player's tile position.
    The position is in the coordinates of the level i.e. Starting at (0,0)
    from the top left of the map and increasing in (x,y) as you go right
    and down This is NOT a pixel position, but instead a position in the level
    coordinates. Since the player is in the centre of the screen at all times,
    we need a 'camera position' to more easily compute how to shift
    the map around.
    
    We define the camera position such that when we blit the level tiles,
    we need only add the camera position to the tile position in order to
    correctly place the center of the player at the position on the map."""

    # Account for the player being in the middle of the screen, not the edge
    camera_pos = cfgTiles["centre"]
    # Account for the position on the level the player is
    tile_pixelpos = TileCoordToPos(player_pos)
    camera_pos = tuple_utils.AddTuples( tuple_utils.ScaleTuple(tile_pixelpos,-1), camera_pos)
    # Account for the difference in size between the tile_rect and the player_rect
#    camera_pos = AddTuples( TilePosToPlayerPos(player_pos), camera_pos ) 
#    print "Half Screen + Tile Coord + PlayerSpace =",camera_pos
    return camera_pos

