class ArrayQueue:
    def __init__(self):
        # NOTE: your LinkedListQueue
        # will have to maintain head and tail pointers
        # and can't use Python's built-in list (which is a dynamic array)
        self.queue = []

    def is_empty(self):
        # NOTE: your LinkedListQueue
        # will not work with the len function
        # so you'll have to use another method to check if it's empty
        return len(self.queue) == 0

    def enqueue(self, value):
        # add value to end of queue
        self.queue.append(value)

    def dequeue(self):
        # if empty return None and do nothing
        if self.is_empty():
            return None
        # else delete first element and return its value
        return self.queue.pop(0)


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self): 
        return self.head is None
      
    def enqueue(self, value):
        if self.head is not None:
            cur = self.head
            while cur.next_node is not None:
                cur = cur.next_node
            cur.next_node = Node(value,None)
        else:
            self.head = Node(value,None)

    def dequeue(self):
        if self.head is None:
            return None
        else:
            element = self.head
            self.head = self.head.next_node
            return element.value

    
        
"""
q = LinkedListQueue() # creates an empty queue
print(q.is_empty())
q.enqueue(1) # adds 1 to end of queue
print(q.is_empty()) # prints False
q.enqueue(2) # adds 2 to end of queue
q.enqueue(3) # adds 3 to end of queue
# queue now looks like: 1 -> 2 -> 3 -> None
print(q.dequeue()) # prints 1; queue now looks like 2 -> 3 -> None
print(q.dequeue()) # prints 2
print(q.dequeue()) # prints 3
print(q.is_empty()) # prints True
print(q.dequeue()) # prints None, because queue is empty
"""
