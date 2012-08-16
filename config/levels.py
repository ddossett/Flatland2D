# Store for the level designs. Use lists to define positions of different objects.
import os
import config.main as cfg
levels = []

f = open(os.path.join(cfg.LEVELPATH,'level-001.lvl'),'r')
f_readlines = f.readlines()
f.close()

level1 = []
for line in f_readlines:
    level1.append(list(line.strip()))

levels.append(level1)
