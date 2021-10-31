"""
Author: Quoc Thinh Vo
"""
def kruskals(graph, edges):
    """Takes dictionary adjacency list of undirected graph
    and dictionary of edge weights (each undirected edge
    will be represented exactly once in arbitrary order).
    Returns total weight of minimum spanning tree."""
    edges = dict(sorted(edges.items(), key=lambda item: item[1]))
    MST_weight = 0
    dj_set = Dis_Joint_Set() 

    if len(graph) == 0:
        return 0
    dj_set.make_set(graph)
    result = {}
    for edge in edges:
        node_1 = edge[0]
        node_2 = edge[1]
        edge_weight = edges[edge]
        x = dj_set.find(node_1)
        y = dj_set.find(node_2)
        
        if x != y:         
            MST_weight += edge_weight
            result[(node_1,node_2)]= edge_weight
            dj_set.union(x,y)
    print(result)      
    return MST_weight
        
        


class Dis_Joint_Set:
    parent = {}
    rank = {}
  
    def make_set(self, graph):
        for node in graph:
            self.parent[node] = node
            self.rank[node] = 0
   
    def find(self, node):
        if self.parent[node] == node:
            return node        
        return self.find(self.parent[node])
 
    def union(self, node_1, node_2):
        x = self.find(node_1)
        y = self.find(node_2)
               
        if self.rank[x] <  self.rank[y]:
             self.parent[x] = y           
        elif self.rank[x] >  self.rank[y]:  
            self.parent[y] = x           
        elif  self.rank[x] ==  self.rank[y]:
            self.parent[y] = x
            self.rank[x] += 1

graph = {
    "a": ["b", "c", "d"],
    "b": ["a", "c", "f"],
    "c": ["a", "b", "d", "e"],
    "d": ["a", "c", "e"],
    "e": ["c", "d", "f"],
    "f": ["b", "e", "g"],
    "g": ["f"],
}

edges = {
    ("a", "b"): 1,
    ("a", "c"): 7,
    ("a", "d"): 3,
    ("b", "c"): 2,
    ("f", "b"): 6,
    ("c", "d"): 1,
    ("c", "e"): 8,
    ("d", "e"): 4,
    ("e", "f"): 1,
    ("f", "g"): 3,
}

mst_weight = kruskals(graph, edges)
print(mst_weight) # prints 12, total weight of MST found
