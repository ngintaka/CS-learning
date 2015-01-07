n = 10

a = 0
b = 0
c = 0


for i in range(n):
    c += 1
    print 'c',c
    for i in range (n):
        b += 1
        print 'b',b
        for i in range (n):
            a += 1
            print 'a',a
    div = (6*a + 9*b + 20*c)
    print div
