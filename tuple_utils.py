# Some helpful functions to be used all over the place.

def AddToTuple(pos, val):
    return tuple( [ x+val for x in pos ] )

def AddTuples(pos1, pos2):
    return tuple( [ x1+x2 for x1,x2 in zip(pos1,pos2) ] )

def MultiplyTuples(pos1, pos2):
    return tuple( [ x1*x2 for x1,x2 in zip(pos1,pos2) ] )

def ScaleTuple(pos, scale):
    return tuple( [ x*scale for x in pos ] )
