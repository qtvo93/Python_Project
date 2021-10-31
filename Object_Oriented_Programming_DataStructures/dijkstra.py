"""
Quoc Thinh Vo
CS-260
"""
import math

# paste your MinHeap class here and modify it as needed
# for use by your dijkstra function

class MinHeap:
    def __init__(self, length):
        """Creates heap array with length empty slots,
        initialized to None. Array length should never change."""
        self.length = length
        self.array =  [[None, None] for i in range(self.length)]
        self.array_Idx_tracking = 0
        self.heap_dict={}
  
    def insert(self, node, value):
        """Takes numeric value as argument. Returns nothing.
        Inserts value into heap using upheap algorithm.
        If heap has no empty slots remaining, do nothing."""
        if self.array_Idx_tracking  < self.length:
            self.array[self.array_Idx_tracking] = [node,value]
            self.array_Idx_tracking += 1
        self._up_heap(self.array_Idx_tracking-1)   
        
    def _up_heap(self, i):
        parent_index = (i - 1) // 2
        if parent_index >= 0 and self.array[i][1] < self.array[parent_index][1] :
            self.array[i][0], self.array[parent_index][0] = self.array[parent_index][0], self.array[i][0]
            self.array[i][1], self.array[parent_index][1] = self.array[parent_index][1], self.array[i][1]
            self.update_dict_heap()
            self._up_heap(parent_index)
        
    def extract_min(self):
        """Takes no arguments. Removes and returns
        min value in heap using downheap algorithm.
        If heap is empty, return None."""
        if all([i[0] == None for i in self.array]):
            return None
        else:
            self.array[0][0], self.array[self.array_Idx_tracking-1][0] = self.array[self.array_Idx_tracking-1][0], self.array[0][0]
            self.array[0][1], self.array[self.array_Idx_tracking-1][1] = self.array[self.array_Idx_tracking-1][1], self.array[0][1]
            element = self.array[self.array_Idx_tracking-1]  
            self.array[self.array_Idx_tracking - 1] = [None, None]
            self.array_Idx_tracking -= 1
            self._down_heap(self.array,0)
            return element
    
    def _down_heap(self,array,i):    
        if ((i+1)*2-1) >= self.length or array[(i+1)*2-1][0] is None:
            return
        left = array[(i+1)*2-1]
        right = array[(i+1)*2]
        if right[1] is not None:
            if array[i][1] > right[1] or array[i][1] > left[1]:
                min_Idx = array.index(min(left,right))
                array[i][0] , array[min_Idx][0] = array[min_Idx][0] , array[i][0]
                array[i][1] , array[min_Idx][1] = array[min_Idx][1] , array[i][1]
                self.update_dict_heap()
                self._down_heap(array,min_Idx)
        else:
            if array[i][1] > left[1]:
                min_Idx = array.index(left)
                array[i][0] , array[min_Idx][0] = array[min_Idx][0] , array[i][0]
                array[i][1] , array[min_Idx][1] = array[min_Idx][1] , array[i][1] 
                self.update_dict_heap()
                self._down_heap(array,min_Idx)
  
    def get_heap_array(self):
        """Takes no arguments. Returns internal heap array
        for automated grading tests."""
        return self.array
    
    def get_heap_dic(self):
        return self.heap_dict
    
    def isEmpty(self):
        return True if all([i[0] == None for i in self.array]) else False
    
    def update_dict_heap(self):     
        key = [node[0] for node in self.array]
        value = [node[1] for node in self.array]      
        self.heap_dict= {key[i]: value[i] for i in range(len(key))}
        
        return self.heap_dict


def dijkstra(graph, edges, source):
    """Takes an adjacency list dictionary, edge weight dictionary,
    and a source node label. Returns a dictionary mapping node labels
    to their minimum distances from the source node."""
    
    distance = {source: math.inf for source in graph}
    distance[source] = 0
  
    unvisited = [node for node in graph]  
    minHeap = MinHeap(len(graph))
    
    for key in distance:
        minHeap.insert(key,distance[key])
     
    while not minHeap.isEmpty():    
        shortest = minHeap.extract_min()        
        shortest_label = shortest[0]  # cur visiting node
        # shortest_distance = shortest[1]
        
        if shortest_label in unvisited:
            adjacent_nodes = adjacency(graph, shortest_label)
            for node in adjacent_nodes:
                weight = weight_to_adjacent(edges, shortest_label, node)
                if distance[node] > distance[shortest_label] + weight:   # relaxing node
                    distance[node] = distance[shortest_label] + weight
                    minHeap.insert(node,distance[node])        
            
            unvisited.remove(shortest_label)
        
    return distance

def adjacency(graph,source):
    adjacency = []
    for node in graph[source]:
        adjacency.append(node)
    return adjacency

def weight_to_adjacent(edges, source, adjacent):   
    if (source,adjacent) in edges:
        return edges[(source,adjacent)]
    return 0







"""
graph = {
    'a': ['b', 'c'], 
    'b': ['a', 'c', 'e'], 
    'c': ['b', 'd', 'e'], 
    'd': ['a'],
    'e': [],
    'f': [],
    'g': ['e'],
}
edges = {
    ('a', 'b'): 2,
    ('a', 'c'): 7,
    ('b', 'a'): 4,
    ('b', 'c'): 3,
    ('b', 'e'): 10,
    ('c', 'b'): 6,
    ('c', 'd'): 4,
    ('c', 'e'): 1,
    ('d', 'a'): 3,
    ('g', 'e'): 2
}


graph = {
    'a': ['b','c'], 
    'b': ['c','a','e'], 
    'c': ['d','f'], 
    'd': ['e'],
    'e': ['f','a'],
    'f': ['g'],
    'g': ['a','f','e'],
}

"""
graph = {
    'a': []
   
    }
edges = {
    ('a', 'b'): 2,
    ('a', 'c'): 1,
   ('b', 'a'): 4,
    ('b', 'c'): 3,
   ('b', 'e'): 5,
   ('c', 'b'): 6,
    ('c', 'd'): 4,
   ('c', 'f'): 1,
    ('d', 'a'): 3,
    ('g', 'e'): 2,
    ('d', 'e'): 1,
    ('e', 'f'): 1,
    ('f', 'g'): 1,
    ('g', 'a'): 1,
}
distances = dijkstra(graph, edges, 'a')
print(distances) 
# {'a': 0, 'b': 2, 'c': 5, 'd': 9, 'e': 6, 'f': inf, 'g': inf}

distances = dijkstra(graph, edges, 'c')
print(distances)
# {'a': 7, 'b': 6, 'c': 0, 'd': 4, 'e': 1, 'f': inf, 'g': inf}

distances = dijkstra(graph, edges, 'g')
print(distances)
# {'a': inf, 'b': inf, 'c': inf, 'd': inf, 'e': 2, 'f': inf, 'g': 0}

