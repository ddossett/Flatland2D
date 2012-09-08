# Store for the level designs. Use lists to define positions of different objects.
import os
import config.main as cfg
levels = []

f = open(os.path.join(cfg.LEVELPATH,'level-002.lvl'),'r')
f_readlines = f.readlines()
f.close()

level2 = []
for line in f_readlines:
    level2.append(list(line.strip()))

levels.append(level2)
