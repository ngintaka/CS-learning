def listCreate(start,stop,step):
    L = [start]
    l = start
    while l < (stop-step):
        l = l +step
        L.append(l)
    L.append(stop)
    return L