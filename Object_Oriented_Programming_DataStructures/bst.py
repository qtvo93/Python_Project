"""
Author: Quoc Thinh Vo
Last Edit: Feb 18th, 2021 
"""

class BTNode:
    '''Binary Tree Node class - do not modify'''
    def __init__(self, value, left, right):
        '''Stores a reference to the value, left child node, and right child node. If no left or right child, attributes should be None.'''
        self.value = value
        self.left = left
        self.right = right
        

class BST:
    def __init__(self):
        # reference to root node - do not modify
        self.root = None
        
    def _insert(self,value,root):
        if root.value == value:
            root.value = value
        elif value < root.value:
            if root.left == None:
                root.left = BTNode(value,None,None)
            else:                
                self._insert(value,root.left)
        else:
            if root.right == None:
                root.right = BTNode(value,None,None)
            else:               
                self._insert(value,root.right)
   
    def insert(self, value):
        '''Takes a numeric value as argument.
        Inserts value into tree, maintaining correct ordering.
        Returns nothing.'''
        if self.root is None:
            self.root = BTNode(value,None,None)
        else:
            self._insert(value, self.root)
    
            
    def _search(self, value, root):
        if root is None:
            return False
        elif value == root.value:
            return True
        elif value < root.value:
            return self._search(value, root.left)
        else:
            return self._search(value, root.right)
        
    def search(self, value):
        '''Takes a numeric value as argument.
        Returns True if its in the tree, false otherwise.'''
        return self._search(value,self.root)
    
   
    def _height(self, root):
        if root is None:
            return -1
        return 1 + max(self._height(root.left), self._height(root.right))
    
    def height(self):
        '''Returns the height of the tree.
        A tree with 0 or 1 nodes has a height of 0.'''
        if self.root is None :
            return 0
        if self.root.left is None and self.root.right is None:
            return 0
        else:
            return self._height(self.root)

  
    def _preorder(self,list_result,root):
        if root is None:
            return
        else:
            list_result.append(root.value)
            self._preorder(list_result,root.left)
            self._preorder(list_result,root.right)
        
    def preorder(self):
        '''Returns a list of the values in the tree,
        in pre-order order.'''
        result = []
        self._preorder(result,self.root)       
        return result

"""
bst = BST()

for value in [4, 2, 5, 3, 1, 6, 7]:
    bst.insert(value)
bst2= BST()   

# BST now looks like this:
#      4
#    /   \
#   2     5
#  / \     \
# 1   3     6
#            \
#             7


print(bst.search(5)) # True
print(bst.search(8)) # False

print(bst.preorder()) # [4, 2, 1, 3, 5, 6, 7]
print(bst.height()) # 3
bst2.insert(1)
print(bst2.height())
"""
