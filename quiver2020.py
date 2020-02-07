#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to make a 3d vector plot of the b-field, pretty handy for visualizing.
Created on Tue Sep 25 09:24:46 2019

@author: fpiermaier
"""

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import mpl_toolkits.mplot3d.art3d as art3d

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.ticker import FormatStrFormatter
import matplotlib.patches as patches

import scipy.interpolate as interp


# %%
#---IMPORT DATA---#

df1 = pd.read_csv('run1.csv')
df2 = pd.read_csv('run2.csv')
df3 = pd.read_csv('run3.csv')
# df1 = pd.read_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/run1.csv')
# df2 = pd.read_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/run2.csv')
# df3 = pd.read_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/run3.csv')

dfa = df1.append(df2)
dfa = dfa.append(df3)

xn_all = dfa.x.unique()
yn_all = dfa.y.unique()
zn_all = dfa.z.unique()
zn_max = np.max(dfa.z)
zn_min = np.min(dfa.z)

# %%
#---QUIVER PLOT---#

# new
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Color by length of vector
cn = np.sqrt(dfa['Bx']**2+dfa['By']**2+dfa['Bz']**2)
# Flatten and normalize
cn = (cn.ravel() - cn.min()) / np.ptp(cn)
# Repeat for each body line and two head lines
cn = np.concatenate((cn, np.repeat(cn, 2)))
# Colormap
cn = plt.cm.plasma(cn)
qn = ax.quiver(dfa['x'], dfa['y'], dfa['z'], dfa['Bx']*2, dfa['By']*2, dfa['Bz']*2, colors=cn, length=0.1)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
#axn.set_xlim(-320, 200)
#axn.set_ylim(-350, 200)
#axn.set_zlim(-200, -40)
fig.tight_layout(pad=3,rect=[0, 0, 1, 0.99])
plt.show()

# %%


dfn = dfa[dfa.z>=150]

#---QUIVER PLOT---#

# new
fign = plt.figure()
axn = fign.add_subplot(111, projection='3d')
# Color by length of vector
cn = np.sqrt(dfn['Bx']**2+dfn['By']**2+dfn['Bz']**2)
# Flatten and normalize
cn = (cn.ravel() - cn.min()) / np.ptp(cn)
# Repeat for each body line and two head lines
cn = np.concatenate((cn, np.repeat(cn, 2)))
# Colormap
cn = plt.cm.plasma(cn)
qn = axn.quiver(dfn['x'], dfn['y'], dfn['z'], dfn['Bx']*2, dfn['By']*2, dfn['Bz']*2, colors=cn, length=0.1)
axn.set_xlabel('X axis')
axn.set_ylabel('Y axis')
axn.set_zlabel('Z axis')
#axn.set_xlim(-320, 200)
#axn.set_ylim(-350, 200)
#axn.set_zlim(-200, -40)
fig.tight_layout(pad=3,rect=[0, 0, 1, 0.99])
plt.show()
