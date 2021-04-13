# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:12:08 2020

@author: Thinh Vo
"""
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.where(a<4)
print(a[b])
print(b)