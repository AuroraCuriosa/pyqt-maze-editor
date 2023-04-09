'''
Created on 7 Apr 2023

@author: Rob Probin

Emulate the minimal piece of numpy we use.

'''

#inf = 1e100 # poor emulation of infinity
inf = float('inf')

def zeros(size, dtype=None):
    # lists are pretty fast
    return [0]*size

