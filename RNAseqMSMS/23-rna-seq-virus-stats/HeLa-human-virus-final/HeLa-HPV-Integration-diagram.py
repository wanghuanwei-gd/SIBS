import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt 
import time
from matplotlib.path import Path
import matplotlib.patches as patches

chr_MIN = 128000000
chr_MAX= 128800000
OFFSET = 10000
LEN = chr_MAX - chr_MIN + 1

fig = plt.figure()
ax=fig.add_subplot(211)
#ax.set_xlim(-OFFSET, OFFSET + LEN)
ax.set_xlim(chr_MIN-OFFSET, chr_MAX+OFFSET)
#ax.set_xticks([1]+range(1000,HPV_len+100,1000)+[HPV_len])
#ax.set_ylim(-1,1)
ax.set_ylim(0,1)

### genome region
verts = [
    (chr_MIN, 0.4), # left, bottom
    (chr_MIN, 0.5), # left, top
    (chr_MAX,0.5), # right, top
    (chr_MAX,0.4), # right, bottom
    (0,0)
    ]
codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]
path = Path(verts, codes)
patch = patches.PathPatch(path, facecolor='orange', lw=1)
ax.add_patch(patch)

### add integration point

POS = sorted([128241377,128231055,128241548,
            128231213,128241370,128230632,128235913
            ])  

y = 0
for pos in POS:
    y += 1
    ax.scatter(pos, 0.05*y, c='red',marker='^',edgecolors='')

### add gene annotation
MYC = [(128748315,0.6),(128748315,0.66),(128753680,0.66),(128753680,0.6),(0,0)]
path = Path(MYC, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((105+581)/2.0,-0.25,'E6',horizontalalignment='center',verticalalignment='center',fontsize=6)
PCAT1 = [(128025399,0.6),(128025399,0.66),(128033259,0.66),(128033259,0.6),(0,0)]
path = Path(PCAT1, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)

CCAT1 = [(128219629,0.6),(128219629,0.66),(128231333,0.66),(128231333,0.6),(0,0)]
path = Path(CCAT1, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)

BC106081 = [(128240804,0.7),(128240804,0.76),(128241377,0.76),(128241377,0.7),(0,0)]
path = Path(BC106081, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)

ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)

#################################################
################################################

chr_MIN = 1
chr_MAX= 7857
OFFSET = 100

ax=fig.add_subplot(212)
#ax.set_xlim(-OFFSET, OFFSET + LEN)
ax.set_xlim(chr_MIN-OFFSET, chr_MAX+OFFSET)
#ax.set_xticks([1]+range(1000,HPV_len+100,1000)+[HPV_len])
#ax.set_ylim(-1,1)
ax.set_ylim(0,1)

### genome region
verts = [
    (chr_MIN, 0.5), # left, bottom
    (chr_MIN, 0.6), # left, top
    (chr_MAX,0.6), # right, top
    (chr_MAX,0.5), # right, bottom
    (0,0)
    ]
codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]
path = Path(verts, codes)
patch = patches.PathPatch(path, facecolor='orange', lw=1)
ax.add_patch(patch)

### add integration point

POS = sorted([929, 23, 2497, 930, 929, 5736, 929])

y = 0
for pos in POS:
    y += 1
    ax.scatter(pos, 0.6+0.05*y, c='red',marker='v',edgecolors='')

## add gene annotation
E6 = [(105,0.3),(105,0.36),(581,0.36),(581,0.3),(0,0)]
path = Path(E6, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((105+581)/2.0,-0.25,'E6',horizontalalignment='center',verticalalignment='center',fontsize=6)

E7 = [(590,0.2),(590,0.26),(907,0.26),(907,0.2),(0,0)]
path = Path(E7, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((590+907)/2.0,-0.45,'E7',horizontalalignment='center',verticalalignment='center',fontsize=6)

E1 = [(914,0.3),(914,0.36),(2887,0.36),(2887,0.3),(0,0)]
path = Path(E1, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((914+2887)/2.0,-0.25,'E1',horizontalalignment='center',verticalalignment='center',fontsize=6)

E2 = [(2817,0.2),(2817,0.26),(3914,0.26),(3914,0.2),(0,0)]
path = Path(E2, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((2817+3914)/2.0,-0.45,'E2',horizontalalignment='center',verticalalignment='center',fontsize=6)

E4 = [(3418,0.3),(3418,0.36),(3684,0.36),(3684,0.3),(0,0)]
path = Path(E4, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((3418+3684)/2.0,-0.25,'E4',horizontalalignment='center',verticalalignment='center',fontsize=6)

E5 = [(3936,0.3),(3936,0.36),(4157,0.36),(4157,0.3),(0,0)]
path = Path(E5, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((3936+4157)/2.0,-0.25,'E5',horizontalalignment='center',verticalalignment='center',fontsize=6)

L2 = [(4244,0.2),(4244,0.26),(5632,0.26),(5632,0.2),(0,0)]
path = Path(L2, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((4244+5632)/2.0,-0.45,'L2',horizontalalignment='center',verticalalignment='center',fontsize=6)

L1 = [(5430,0.3),(5430,0.36),(7136,0.36),(7136,0.3),(0,0)]
path = Path(L1, codes)
patch = patches.PathPatch(path, facecolor='magenta', lw=1)
ax.add_patch(patch)
#ax.text((5430+7136)/2.0,-0.25,'L1',horizontalalignment='center',verticalalignment='center',fontsize=6)

ax.axes.get_yaxis().set_visible(False)
ax.axes.get_xaxis().set_visible(False)



plt.savefig('HeLa-HPV-Integration-diagram.pdf')


