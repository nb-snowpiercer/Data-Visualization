import matplotlib.pyplot as plt;
from matplotlib.path import Path;
import matplotlib.patches as patches;
import matplotlib.patches as mpatches;
verts = [(0., 0.), (0., 5.), (4., 5.),(4., 0.), (0., 0.),];
codes = [Path.MOVETO,Path.LINETO,Path.LINETO,Path.LINETO,Path.CLOSEPOLY,];
path = Path(verts, codes);
fig = plt.figure();
ax = fig.add_subplot(111);
patch = patches.PathPatch(path, facecolor='green', lw=2);
ax.add_patch(patch);
arrow = mpatches.FancyArrowPatch((0.1, 0.1), (0.5, 0.5),mutation_scale=10);
ax.add_patch(arrow);
rect = mpatches.Rectangle((0.3, 0.3), 0.5, 0.5, fc = 'white',ec="none");
ax.add_patch(rect);
ax.set_xlim(-2,6);
ax.set_ylim(-2,6);
plt.show();