def gcdRecur(a,b):
    hi = max(a,b)
    lo = min(a,b)
    if a == 0:
        return a
    elif b == 0:
        return b
    elif hi % lo == 0:
        return lo
    else:
        return gcdRecur(lo,hi % lo)
