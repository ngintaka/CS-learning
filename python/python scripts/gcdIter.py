def gcdIter(a,b):
    hi = max(a,b)
    lo = min(a,b)
    gcd = lo
    if hi % lo == 0:
        return lo
    else:
        while hi % gcd != 0 or lo % gcd != 0:
            gcd -= 1
    return gcd
