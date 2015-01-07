def McNuggets(n):

    if n%20 == 0 or n%6 == 0 or n%9 == 0:
        return True
    ans = []
    for a in range(5):
        for b in range(5):
            for c in range(5):
                ans.append(6*a + 9*b + 20*c)
                #print ans
    if n in ans:
        return True
    else:
        return False
