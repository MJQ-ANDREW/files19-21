from math import ceil
from functools import lru_cache

def m(h):
    a, b = h
    return (ceil(a * 1.5), b), (a, ceil(b * 1.5)), (a + 7, b), (a, b + 7)

@lru_cache(None)
def g(h):
    a, b = h 
    if a + b >= 115:
        return 'w'
    elif any(g(x) == 'w' for x in m(h)):
        return 'p1'
    elif any(g(x) == 'p1' for x in m(h)):
        return 'v1'
    elif any(g(x) == 'v1' for x in m(h)):
        return 'p2'
    elif all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)):
        return 'v2'
    

for s in range(1, 102):
    h = 13, s
    if g(h) == 'v1':
        print(s, g(h))
        break

