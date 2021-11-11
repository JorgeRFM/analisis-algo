# Python3 program to find minimum edge
# between given two vertex of Graph
import queue

El_Rosario=1
Instituto_del_petroleo=2
Deportivo_18_de_marzo=3
Martin_Carrer=4
La_Raza=5
Consulado=6
Oceania=7
Tacuba=8
Guerrero=9
Garibaldi=10
Hidalgo=11
Bellas_Artes=12
Morelos=13
Balderas=14
Salto_del_Agua=15
Pino_Suarez=16
San_Lazaro=17
Candelaria=18
Tacubaya=19
Centro_Medico=20
Chabacano=21
Jamaica=22
Pantitlan=23
Santa_Anita=24
Mixcoac=25
Zapata=26
Ermita=27
Atlantico=28


# function for finding minimum
# no. of edge using BFS
def minEdgeBFS(edges, u, v, n):
	
	# visited[n] for keeping track
	# of visited node in BFS
	visited = [0] * n

	# Initialize distances as 0
	distance = [0] * n

	# queue to do BFS.
	Q = queue.Queue()
	distance[u] = 0

	Q.put(u)
	visited[u] = True
	while (not Q.empty()):
		x = Q.get()
		
		for i in range(len(edges[x])):
			if (visited[edges[x][i]]):
				continue

			# update distance for i
			distance[edges[x][i]] = distance[x] + 1
			Q.put(edges[x][i])
			visited[edges[x][i]] = 1
	return distance[v]

# function for addition of edge
def addEdge(edges, u, v):
	edges[u].append(v)
	edges[v].append(u)

# Driver Code
if __name__ == '__main__':

	# To store adjacency list of graph
	n = 51
	edges = [[] for i in range(n)]
	addEdge(edges, El_Rosario, Instituto_del_petroleo)
	addEdge(edges, El_Rosario, Tacuba)
	addEdge(edges, Instituto_del_petroleo, Deportivo_18_de_marzo)
	addEdge(edges, Instituto_del_petroleo, La_Raza)
	addEdge(edges, Deportivo_18_de_marzo, Martin_Carrer)
	addEdge(edges, Deportivo_18_de_marzo, La_Raza)
	addEdge(edges, Martin_Carrer, Consulado)
	addEdge(edges, La_Raza, Consulado)
	addEdge(edges, La_Raza, Guerrero)
	addEdge(edges, Consulado, Morelos)
	addEdge(edges, Consulado, Oceania)
	addEdge(edges, Oceania, San_Lazaro)
	addEdge(edges, Oceania, Pantitlan)
	addEdge(edges, Tacuba, Hidalgo)
	addEdge(edges, Tacuba, Tacubaya)
	addEdge(edges, Guerrero, Hidalgo)
	addEdge(edges, Guerrero, Garibaldi)
	addEdge(edges, Garibaldi, Morelos)
	addEdge(edges, Garibaldi, Bellas_Artes)
	addEdge(edges, Hidalgo, Bellas_Artes)
	addEdge(edges, Hidalgo, Balderas)
	addEdge(edges, Bellas_Artes, Salto_del_Agua)
	addEdge(edges, Bellas_Artes, Pino_Suarez)
	addEdge(edges, Morelos, San_Lazaro)
	addEdge(edges, Morelos, Candelaria)
	addEdge(edges, San_Lazaro, Pantitlan)
	addEdge(edges, San_Lazaro, Candelaria)
	addEdge(edges, Balderas, Tacubaya)
	addEdge(edges, Balderas, Salto_del_Agua)
	addEdge(edges, Balderas, Centro_Medico)
	addEdge(edges, Salto_del_Agua, Pino_Suarez)
	addEdge(edges, Salto_del_Agua, Chabacano)
	addEdge(edges, Pino_Suarez, Candelaria)
	addEdge(edges, Pino_Suarez, Chabacano)
	addEdge(edges, Candelaria, San_Lazaro)
	addEdge(edges, Candelaria, Jamaica)
	addEdge(edges, Pantitlan, Jamaica)
	addEdge(edges, Tacubaya, Centro_Medico)
	addEdge(edges, Tacubaya, Mixcoac)
	addEdge(edges, Centro_Medico, Chabacano)
	addEdge(edges, Centro_Medico, Zapata)
	addEdge(edges, Chabacano, Ermita)
	addEdge(edges, Chabacano, Jamaica)
	addEdge(edges, Chabacano, Santa_Anita)
	addEdge(edges, Jamaica, Santa_Anita)
	addEdge(edges, Mixcoac, Zapata)
	addEdge(edges, Zapata, Ermita)
	addEdge(edges, Ermita, Atlantico)


	u = El_Rosario
	v = Zapata
	print(minEdgeBFS(edges, u, v, n))

# This code is contributed by PranchalK
