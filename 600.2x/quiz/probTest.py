def probTest(limit):
    n = 1
    result = 1
    while result >= limit:
        result = (1.0 / 6.0) * (5.0 /6.0)**(n-1)
        n +=1
    print (n - 1)