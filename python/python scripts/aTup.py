aTup = (1,2,3,4,5,6,7,8,9)
n = 0
L = []
while n < len(aTup):
    L.append(aTup[n])
    n += 2
print tuple(L)
