def f(x):
	import math
	return 200*math.e**(math.log(0.5)/14.1 * x)

def radiationExposure(start, stop, step):
    total = 0
    for y in range(start, stop,step): #step can only be integer
        rad = f(y)
        print y,rad 
        total = total + rad
    return total

def radiationExposure1(start, stop, step):
    total = 0
    for y in ([x * step for x in range(start, stop)]):
        print x
        rad = f(y)
        print y,rad 
        total = total + rad
    return total
