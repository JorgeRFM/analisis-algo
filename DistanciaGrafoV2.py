# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
El_Rosario=1
Instituto_del_petroleo=2
Deportivo_18_de_marzo=3
Martin_Carrera=4
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
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(El_Rosario, Instituto_del_petroleo)
g.addEdge(El_Rosario, Tacuba)
g.addEdge(Instituto_del_petroleo, El_Rosario)
g.addEdge(Instituto_del_petroleo, Deportivo_18_de_marzo)
g.addEdge(Instituto_del_petroleo, La_Raza)
g.addEdge(Deportivo_18_de_marzo, Instituto_del_petroleo)
g.addEdge(Deportivo_18_de_marzo, Martin_Carrera)
g.addEdge(Deportivo_18_de_marzo, La_Raza)
g.addEdge(Martin_Carrera, Deportivo_18_de_marzo)
g.addEdge(Martin_Carrera, Consulado)
g.addEdge(La_Raza, Deportivo_18_de_marzo)
g.addEdge(La_Raza, Instituto_del_petroleo)
g.addEdge(La_Raza, Consulado)
g.addEdge(La_Raza, Guerrero)
g.addEdge(Consulado, La_Raza)
g.addEdge(Consulado, Martin_Carrera)
g.addEdge(Consulado, Morelos)
g.addEdge(Consulado, Oceania)
g.addEdge(Oceania, Consulado)
g.addEdge(Oceania, San_Lazaro)
g.addEdge(Oceania, Pantitlan)
g.addEdge(Tacuba, El_Rosario)
g.addEdge(Tacuba, Hidalgo)
g.addEdge(Tacuba, Tacubaya)
g.addEdge(Guerrero, La_Raza)
g.addEdge(Guerrero, Hidalgo)
g.addEdge(Guerrero, Garibaldi)
g.addEdge(Garibaldi, Guerrero)
g.addEdge(Garibaldi, Morelos)
g.addEdge(Garibaldi, Bellas_Artes)
g.addEdge(Hidalgo, Guerrero)
g.addEdge(Hidalgo, Tacuba)
g.addEdge(Hidalgo, Bellas_Artes)
g.addEdge(Hidalgo, Balderas)
g.addEdge(Bellas_Artes, Garibaldi)
g.addEdge(Bellas_Artes, Hidalgo)
g.addEdge(Bellas_Artes, Salto_del_Agua)
g.addEdge(Bellas_Artes, Pino_Suarez)
g.addEdge(Morelos, Garibaldi)
g.addEdge(Morelos, Consulado)
g.addEdge(Morelos, San_Lazaro)
g.addEdge(Morelos, Candelaria)
g.addEdge(San_Lazaro, Morelos)
g.addEdge(San_Lazaro, Oceania)
g.addEdge(San_Lazaro, Pantitlan)
g.addEdge(San_Lazaro, Candelaria)
g.addEdge(Balderas, Hidalgo)
g.addEdge(Balderas, Tacubaya)
g.addEdge(Balderas, Salto_del_Agua)
g.addEdge(Balderas, Centro_Medico)
g.addEdge(Salto_del_Agua, Balderas)
g.addEdge(Salto_del_Agua, Bellas_Artes)
g.addEdge(Salto_del_Agua, Pino_Suarez)
g.addEdge(Salto_del_Agua, Chabacano)
g.addEdge(Pino_Suarez, Bellas_Artes)
g.addEdge(Pino_Suarez, Salto_del_Agua)
g.addEdge(Pino_Suarez, Candelaria)
g.addEdge(Pino_Suarez, Chabacano)
g.addEdge(Candelaria, Pino_Suarez)
g.addEdge(Candelaria, Morelos)
g.addEdge(Candelaria, San_Lazaro)
g.addEdge(Candelaria, Jamaica)
g.addEdge(Pantitlan, San_Lazaro)
g.addEdge(Pantitlan, Candelaria)
g.addEdge(Pantitlan, Jamaica)
g.addEdge(Tacubaya, Balderas)
g.addEdge(Tacubaya, Tacuba)
g.addEdge(Tacubaya, Centro_Medico)
g.addEdge(Tacubaya, Mixcoac)
g.addEdge(Centro_Medico, Tacubaya)
g.addEdge(Centro_Medico, Balderas)
g.addEdge(Centro_Medico, Chabacano)
g.addEdge(Centro_Medico, Zapata)
g.addEdge(Chabacano, Salto_del_Agua)
g.addEdge(Chabacano, Pino_Suarez)
g.addEdge(Chabacano, Centro_Medico)
g.addEdge(Chabacano, Ermita)
g.addEdge(Chabacano, Jamaica)
g.addEdge(Chabacano, Santa_Anita)
g.addEdge(Jamaica, Candelaria)
g.addEdge(Jamaica, Chabacano)
g.addEdge(Jamaica, Pantitlan)
g.addEdge(Jamaica, Santa_Anita)
g.addEdge(Mixcoac, Tacubaya)
g.addEdge(Mixcoac, Zapata)
g.addEdge(Zapata, Chabacano)
g.addEdge(Zapata, Mixcoac)
g.addEdge(Zapata, Ermita)
g.addEdge(Ermita, Chabacano)
g.addEdge(Ermita, Zapata)
g.addEdge(Ermita, Atlantico)
g.addEdge(Atlantico, Ermita)
g.addEdge(Atlantico, Santa_Anita)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex EL Rosario)")
g.BFS(El_Rosario)
 
# This code is contributed by Neelam Yadav