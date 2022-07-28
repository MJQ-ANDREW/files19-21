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
    elif all(g(x) == 'p1' for x in m(h)):
        return 'v1'
    elif any(g(x) == 'v1' for x in m(h)):
        return 'p2'
    elif all(g(x) == 'p1' or g(x) == 'p2' for x in m(h)):
        return 'v2'
    elif any(g(x) == 'v2' for x in m(h)):
        return 'p3'
    elif all(g(x) == 'p1' or g(x) == 'p2' or g(x) == 'p3' for x in m(h)):
        return 'v3'
    

for s in range(101, 0, -1):
    h = 13, s
    if g(h) == 'v2':
        print(s, g(h))
        break

