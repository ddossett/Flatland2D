# Some named tuples and other small objects that will come in handy in many areas
# and I don't want to keep defining them in many places
from collections import namedtuple as ntuple

rgb = ntuple('RGB', 'r g b')
PixelSize = ntuple('PixelSize', 'w h')
