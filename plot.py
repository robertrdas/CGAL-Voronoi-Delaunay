import numpy as np
import pylab as pl
from matplotlib import collections  as mc

arq = open('saida.txt','r')

line = arq.readline()
line = line.split(' * ')
voro = line[0].split(' ')
dela = line[1].split(' ')
dela.pop()

voronoi = []

for i in range(0, len(voro), 4):

	reta = [(float(voro[i]),float(voro[i+1])),(float(voro[i+2]),float(voro[i+3]))]
	voronoi.append(reta)

print(voronoi)

delaunay =[]
for i in range(0, len(dela), 4):
	
	reta = [(float(dela[i]),float(dela[i+1])),(float(dela[i+2]),float(dela[i+3]))]
	delaunay.append(reta)

print(delaunay)

c = np.array([(1, 0, 0, 1)])
d = np.array([(0, 1, 0, 1)])

lc = mc.LineCollection(delaunay, colors=c, linewidths=2)
ld = mc.LineCollection(voronoi, colors=d, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.add_collection(ld)
ax.autoscale()
ax.margins(0.1)
pl.show()