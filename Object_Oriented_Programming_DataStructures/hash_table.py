"""
Course: CS 260
Professor: Galen Long
Student: Quoc Thinh Vo

"""

class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class HashTable:
    def __init__(self, n, hash_func):
        self.n = n
        self.table = [None for x in range(self.n)]
        self.hash_func = hash_func
            
    def get(self, key):
        idx = self.hash_func(key,self.n)
        cur = self.table[idx]
        
        while cur  is not None:
            if cur.data[0] == key:
                return cur .data[1]
            cur = cur.next_node
                
        return None
            
    def insert(self, key, value):
        idx = self.hash_func(key,self.n)
        new = Node((key,value),None)       
        dup = 0
        
        if self.table[idx] is not None:
            cur = self.table[idx]
            if cur.data[0] == key:
                cur.data = (key,value)
                dup = 1
            while cur.next_node is not None:
                cur = cur.next_node   
            if dup == 0:
                cur.next_node = new
                 
        else:
            self.table[idx] = new            
        
    def remove(self, key):       
        idx = self.hash_func(key,self.n)   
        prev = None
        cur = self.table[idx]
        
        while cur is not None:
            if cur.data[0] == key:
                data = cur.data[1]
                if prev is None:
                    if cur.next_node is None:
                        self.table[idx] = None
                    if cur.next_node is not None:
                        cur = cur.next_node
                        self.table[idx] = cur
                else: 
                    if cur.next_node is None:
                        prev.next_node = None
                    else: 
                        prev.next_node = cur.next_node
                return data
            prev = cur
            cur = cur.next_node    
        
        return None


hash_mod = lambda key, n: key % n # simple hash function for testing
n = 10 # table size
table = HashTable(n, hash_mod)
table.insert(0, 'a') # slot 0
table.insert(3, 'b') # slot 0 - collision
table.insert(2, 'c') # slot 2
table.insert(0, 'aa') # overwrite previous value for key 0
table.insert(6, 'd') # slot 0 - collision
table.insert(12, 'e') 
# table now looks something like this
# (order of elements in linked lists doesn't matter):
# slot 0: (0, 'aa')  -> (3, 'b') ->(6, 'd') -> None
# slot 1: None
# slot 2: (2, 'c') -> None

# Slot 0: (0, 'aa') ->(3, 'b') ->(6, 'd') -> (12, 'e') ->None

print(table.get(3)) 
print(table.remove(3))
print(table.get(3))
print("----------------###########")
print(table.get(1))
print(table.get(6))
print(table.get(0))
print(table.get(12))
print("----------------###########")

"""