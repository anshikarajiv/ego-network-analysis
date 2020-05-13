# ego-network-analysis-
statistical and topological analysis of social network graph

We retrieve the real-world dataset of Facebook Ego Networks from SNAP. This contains the aggregate network on Facebook. The vertices represent users of Facebook while the edges represent the friendship or connection between the users of Facebook.
Observation: the graph is connected and is quite dense and clustered.

We represent facebook_combined.txt dataset in the form of an adjacency list. This is done in order to efficiently utilize the space. Each list describes the set of neighbours of vertices in the graph. The user has a connection with each of its neighbours. The graph can also be represented in the form of an adjacency matrix. 

The degree of a node is the number of edges connected to the node. Here, we can say that the degree of each node is the number of friends of a user on Facebook. Degree distribution is the frequency distribution of the different degrees across the nodes in a network.

Representation of distribution of degrees of the network i.e. degree k on x axis and fraction of nodes with degree k on y axis in the form of -
(a)	bar graph
(b)	 histogram
(c)	 scatter plot with power trendline 
(d)	logarithmic graph 
(e)	histogram with curve line

(a) The histogram clearly depicts that as k increases, p(k) decreases. This decrease is at an increasing rate. From this, we can infer that there is a possibility to find a small number of highly connected nodes. 
(b)	Facebook group networks are small-world networks. Our analysis has shown that the degree distributions cannot be entirely characterized by a power law. The graphs follow the power law for small values of k but then seem to decrease more quickly than a power law would predict for large values of k.
(c)	However, the general shape of the curve still looks like a power-law function which means that it is scale free to some extent. The value calculated for alpha is 0.5. The approximate value for R^2 score is 0.6 (quite high as there might be some outliers since there are a large number of vertices and edges in Facebook dataset.)
In lay man terms, we can say that the power law implies that a majority of nodes have very few connections, while a few important nodes have a huge number of connections. This is not always the case with Facebook. 
