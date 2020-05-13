#rajiv anshika
#analysis of facebook_combined.txt

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm

#reading the graph
g=nx.read_edgelist('C:/Users/Anshika Rajiv/Downloads/facebook_combined.txt/facebook_combined.txt',create_using=nx.Graph(),nodetype=int)

#printing the info of the graph
print(nx.info(g))
sp = nx.spring_layout(g)
plt.axis('off')

#drawing the network diagram of the graph
nx.draw_networkx(g,pos=sp,with_label=False,node_size=35)
plt.show()

#printing adjacency matrix
A = nx.to_numpy_matrix(g)
print(A)

#printing adjacency list
for line in nx.generate_adjlist(g):
    print(line)

#printing the degrees
degrees = [len(list(g.neighbors(n))) for n in g.nodes()]
print(degrees)

#getting the degree distribution
degrees = [len(list(g.neighbors(n))) for n in g.nodes()]
degree_final = sorted(set(degrees))
fraction= [list(degrees).count(i)/float(nx.number_of_nodes(g)) for i in degree_final]

#plotting degree distribution graph
plt.figure(figsize=(100, 10))
plt.bar(degree_final,fraction)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()


plt.plot(degree_final,fraction, 'o',color='#ee9a00')
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.xscale('log')
plt.yscale('log')
plt.show()

#plotting best fit curve
(mu, sigma)=norm.fit(degrees)
plt.figure()
n,bins,patches=plt.hist(degrees,4000, density=True,color='#ee9a00')
y=norm.pdf(bins, mu, sigma)
l=plt.plot(bins,y,'k--',linewidth=2)
plt.xlabel('Degree')
plt.ylabel('Fraction of Nodes')
plt.show()



