k = [1,1,1,1,1]
n = [1,2,3,4,5,6,7,8,9,10]
a,b = 0,0
for i in n:
    print n[a] + k[b%len(k)]
    a += 1
    b += 1
