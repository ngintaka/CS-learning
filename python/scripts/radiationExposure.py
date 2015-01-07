def f(x):
	import math
	return 400*math.e**(math.log(0.5)/3.66 * x)
	
def radiationExposure(start, stop, step):
    L = [start]
    l = start
    total = 0
    while l < (stop-step):
        l = l +step
        L.append(l)
    #L.append(stop)
    print L    
    for y in L:
        rad = f(y)
        print y,rad 
        total = total + rad
    return total*step