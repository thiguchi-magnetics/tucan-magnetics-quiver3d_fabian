#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Direct copy of Takashi Higuchis 'Data_sorting_mapping_0809' script.
Used to add names to the datacolumns and to correct false offsets
Created on Tue Sep 17 08:43:53 2019

@author: fpiermaier
"""

import pandas as pd

# %%
#---IMPORT DATA & ADD NAMES---#

df_names = ['cycle','time_start','time_end','x','y','z', 'By','dBy','Bz','dBz','Bx','dBx']
df1 = pd.read_csv('raw/20200201_1026_Feb01_map_avg.csv', names=df_names)
df2 = pd.read_csv('raw/20200201_1356_Feb01_map_02_avg.csv', names=df_names)
df3 = pd.read_csv('raw/20200202_1119_Feb02_map01_avg.csv', names=df_names)
# df1 = pd.read_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/raw/20200201_1026_Feb01_map_avg.csv', names=df_names)
# df2 = pd.read_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/raw/20200201_1356_Feb01_map_02_avg.csv', names=df_names)
# df3 = pd.read_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/raw/20200202_1119_Feb02_map01_avg.csv', names=df_names)

# Coordinate transformation and scaling to muT
df1['Bx'] = 100*df1['Bx']
df1['By'] = 100*df1['By']
df1['Bz'] = 100*df1['Bz']
del df1['dBx']
del df1['dBy']
del df1['dBz']
del df1['cycle']
del df1['time_start']
del df1['time_end']

df2['Bx'] = 100*df2['Bx']
df2['By'] = 100*df2['By']
df2['Bz'] = 100*df2['Bz']
del df2['dBx']
del df2['dBy']
del df2['dBz']
del df2['cycle']
del df2['time_start']
del df2['time_end']

df3['Bx'] = 100*df3['Bx']
df3['By'] = 100*df3['By']
df3['Bz'] = 100*df3['Bz']
del df3['dBx']
del df3['dBy']
del df3['dBz']
del df3['cycle']
del df3['time_start']
del df3['time_end']


# %%
#---SAVE TO NEW FILES---#
df1.to_csv('run1.csv', columns=['x','y','z', 'Bx','By','Bz'],
           index=False)
df2.to_csv('run2.csv', columns=['x','y','z', 'Bx','By','Bz'],
           index=False)
df3.to_csv('run3.csv', columns=['x','y','z', 'Bx','By','Bz'],
           index=False)
# df1.to_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/run1.csv', columns=['x','y','z', 'Bx','By','Bz'],
#            index=False)
# df2.to_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/run2.csv', columns=['x','y','z', 'Bx','By','Bz'],
#            index=False)
# df3.to_csv('~/Schreibtisch/Studium/Bachelor/Bachelor Thesis/Work Fabian/map2020/run3.csv', columns=['x','y','z', 'Bx','By','Bz'],
#            index=False)