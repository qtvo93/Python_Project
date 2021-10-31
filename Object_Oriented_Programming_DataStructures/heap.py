"""
Author: Quoc Thinh Vo
"""
class MinHeap:
    def __init__(self, length):
        """Creates heap array with length empty slots,
        initialized to None. Array length should never change."""
        self.length = length
        self.array = [None for i in range(self.length)]
        self.array_Idx_tracking = 0

    
    def insert(self, value):
        """Takes numeric value as argument. Returns nothing.
        Inserts value into heap using upheap algorithm.
        If heap has no empty slots remaining, do nothing."""
        if self.array_Idx_tracking  < self.length:
            self.array[self.array_Idx_tracking] = value
            self.array_Idx_tracking += 1
        self._up_heap(self.array_Idx_tracking-1)   
        
    def _up_heap(self, i):
        parent_index = (i - 1) // 2
        if parent_index >= 0 and self.array[i] < self.array[parent_index] :
            self.array[i], self.array[parent_index] = self.array[parent_index], self.array[i]
            self._up_heap(parent_index)
        
    def extract_min(self):
        """Takes no arguments. Removes and returns
        min value in heap using downheap algorithm.
        If heap is empty, return None."""
        if all([i == None for i in self.array]):
            return None
        else:
            self.array[0], self.array[self.array_Idx_tracking-1] = self.array[self.array_Idx_tracking-1], self.array[0]  
            element = self.array[self.array_Idx_tracking-1]  
            self.array[self.array_Idx_tracking - 1] = None
            self.array_Idx_tracking -= 1
            self._down_heap(self.array,0)
            return element
    
    def _down_heap(self,array,i):    
        if ((i+1)*2-1) >= self.length or array[(i+1)*2-1] is None:
            return
        left = array[(i+1)*2-1]
        right = array[(i+1)*2]
        if right is not None:
            if array[i] > right or array[i] > left:
                min_Idx = array.index(min(left,right))
                array[i] , array[min_Idx] = array[min_Idx] , array[i] 
                self._down_heap(array,min_Idx)
        else:
            if array[i] > left:
                min_Idx = array.index(left)
                array[i] , array[min_Idx] = array[min_Idx] , array[i] 
                self._down_heap(array,min_Idx)
  
    def get_heap_array(self):
        """Takes no arguments. Returns internal heap array
        for automated grading tests."""
        return self.array
"""
length = 20
values = [1,2,3,4,5,6,7,7,6,5,4,3,2,1]
length_values = len(values)
heap = MinHeap(length)
print(heap.get_heap_array()) # [None, None, None, None, None, None, None, None]

for value in values:
    heap.insert(value)
print(heap.get_heap_array()) # [-3, 6, 7, 18, 44, 10, 8, None]

print(heap.extract_min()) # -3
print(heap.get_heap_array()) # [6, 8, 7, 18, 44, 10, None, None
(heap.insert(1))
print(heap.get_heap_array())

print(heap.extract_min()) 
(heap.insert(-99))
print(heap.get_heap_array())
"""
