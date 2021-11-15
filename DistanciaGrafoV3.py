# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict
from queue import PriorityQueue
El_Rosario=0
Instituto_del_petroleo=1
Deportivo_18_de_marzo=2
Martin_Carrera=3
La_Raza=4
Consulado=5
Oceania=6
Tacuba=7
Guerrero=8
Garibaldi=9
Hidalgo=10
Bellas_Artes=11
Morelos=12
Balderas=13
Salto_del_Agua=14
Pino_Suarez=15
San_Lazaro=16
Candelaria=17
Tacubaya=18
Centro_Medico=19
Chabacano=20
Jamaica=21
Pantitlan=22
Santa_Anita=23
Mixcoac=24
Zapata=25
Ermita=26
Atlantico=27
# This class represents a directed graph
# using adjacency list representation
class Graph:

    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
 
    # function to add an edge to graph
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
 
    # Function to print a BFS of graph
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
 
# Driver code
 
# Create a graph given in
# the above diagram
g = Graph(28)
g.add_edge(El_Rosario, Instituto_del_petroleo,5)
g.add_edge(El_Rosario, Tacuba,3)
g.add_edge(Instituto_del_petroleo, El_Rosario,5)
g.add_edge(Instituto_del_petroleo, Deportivo_18_de_marzo,1)
g.add_edge(Instituto_del_petroleo, La_Raza,1)
g.add_edge(Deportivo_18_de_marzo, Instituto_del_petroleo,1)
g.add_edge(Deportivo_18_de_marzo, Martin_Carrera,1)
g.add_edge(Deportivo_18_de_marzo, La_Raza,1)
g.add_edge(Martin_Carrera, Deportivo_18_de_marzo,1)
g.add_edge(Martin_Carrera, Consulado,2)
g.add_edge(La_Raza, Deportivo_18_de_marzo,1)
g.add_edge(La_Raza, Instituto_del_petroleo,1)
g.add_edge(La_Raza, Consulado,1)
g.add_edge(La_Raza, Guerrero,1)
g.add_edge(Consulado, La_Raza,2)
g.add_edge(Consulado, Martin_Carrera,2)
g.add_edge(Consulado, Morelos,1)
g.add_edge(Consulado, Oceania,2)
g.add_edge(Oceania, Consulado,2)
g.add_edge(Oceania, San_Lazaro,1)
g.add_edge(Oceania, Pantitlan,2)
g.add_edge(Tacuba, El_Rosario,3)
g.add_edge(Tacuba, Hidalgo,6)
g.add_edge(Tacuba, Tacubaya,4)
g.add_edge(Guerrero, La_Raza,1)
g.add_edge(Guerrero, Hidalgo,1)
g.add_edge(Guerrero, Garibaldi,1)
g.add_edge(Garibaldi, Guerrero,1)
g.add_edge(Garibaldi, Morelos,2)
g.add_edge(Garibaldi, Bellas_Artes,1)
g.add_edge(Hidalgo, Guerrero,1)
g.add_edge(Hidalgo, Tacuba,6)
g.add_edge(Hidalgo, Bellas_Artes,1)
g.add_edge(Hidalgo, Balderas,1)
g.add_edge(Bellas_Artes, Garibaldi,1)
g.add_edge(Bellas_Artes, Hidalgo,1)
g.add_edge(Bellas_Artes, Salto_del_Agua,1)
g.add_edge(Bellas_Artes, Pino_Suarez,2)
g.add_edge(Morelos, Garibaldi,2)
g.add_edge(Morelos, Consulado,1)
g.add_edge(Morelos, San_Lazaro,1)
g.add_edge(Morelos, Candelaria,1)
g.add_edge(San_Lazaro, Morelos,1)
g.add_edge(San_Lazaro, Oceania,2)
g.add_edge(San_Lazaro, Pantitlan,5)
g.add_edge(San_Lazaro, Candelaria,1)
g.add_edge(Balderas, Hidalgo,1)
g.add_edge(Balderas, Tacubaya,5)
g.add_edge(Balderas, Salto_del_Agua,1)
g.add_edge(Balderas, Centro_Medico,2)
g.add_edge(Salto_del_Agua, Balderas,1)
g.add_edge(Salto_del_Agua, Bellas_Artes,1)
g.add_edge(Salto_del_Agua, Pino_Suarez,1)
g.add_edge(Salto_del_Agua, Chabacano,2)
g.add_edge(Pino_Suarez, Bellas_Artes,2)
g.add_edge(Pino_Suarez, Salto_del_Agua,1)
g.add_edge(Pino_Suarez, Candelaria,1)
g.add_edge(Pino_Suarez, Chabacano,1)
g.add_edge(Candelaria, Pino_Suarez,1)
g.add_edge(Candelaria, Morelos,1)
g.add_edge(Candelaria, San_Lazaro,1)
g.add_edge(Candelaria, Jamaica,1)
g.add_edge(Pantitlan, San_Lazaro,5)
g.add_edge(Pantitlan, Oceania,2)
g.add_edge(Pantitlan, Jamaica,4)
g.add_edge(Tacubaya, Balderas,5)
g.add_edge(Tacubaya, Tacuba,4)
g.add_edge(Tacubaya, Centro_Medico,2)
g.add_edge(Tacubaya, Mixcoac,2)
g.add_edge(Centro_Medico, Tacubaya,2)
g.add_edge(Centro_Medico, Balderas,2)
g.add_edge(Centro_Medico, Chabacano,1)
g.add_edge(Centro_Medico, Zapata,2)
g.add_edge(Chabacano, Salto_del_Agua,2)
g.add_edge(Chabacano, Pino_Suarez,1)
g.add_edge(Chabacano, Centro_Medico,1)
g.add_edge(Chabacano, Ermita,5)
g.add_edge(Chabacano, Jamaica,1)
g.add_edge(Chabacano, Santa_Anita,1)
g.add_edge(Jamaica, Candelaria,1)
g.add_edge(Jamaica, Chabacano,1)
g.add_edge(Jamaica, Pantitlan,4)
g.add_edge(Jamaica, Santa_Anita,1)
g.add_edge(Mixcoac, Tacubaya,2)
g.add_edge(Mixcoac, Zapata,2)
g.add_edge(Zapata, Centro_Medico,3)
g.add_edge(Zapata, Mixcoac,2)
g.add_edge(Zapata, Ermita,1)
g.add_edge(Ermita, Chabacano,5)
g.add_edge(Ermita, Zapata,1)
g.add_edge(Ermita, Atlantico,1)
g.add_edge(Atlantico, Ermita,1)
g.add_edge(Atlantico, Santa_Anita,5)
 
D = g.dijkstra(0)

for vertex in range(len(D)):
    print("Distance from vertex 0 to vertex", vertex, "is", D[vertex])
 
# This code is contributed by Neelam Yadav