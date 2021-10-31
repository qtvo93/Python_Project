# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:38:14 2021

@author: QTVo
"""

class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node

def every_other(head):
    if head is None:
        return
    else:
        cur = head 
        cur_next = head.next
     
        while cur is not None and cur_next is not None: 
            cur.next = cur_next.next
            cur_next = Node(None,None)
            cur = cur.next
            if cur is not None: 
                cur_next = cur.next
 