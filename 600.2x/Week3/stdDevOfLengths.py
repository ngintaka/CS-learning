def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
      
      This version passed grader.
    """
    if L == []:
        return float('nan')
    
    chars = 0
    totalChars = 0
    lengths = []
    sum = 0
    for i in L:
        lengths.append(len(i))
        for k in i:
            totalChars +=1
    
    mean = float(totalChars) / len(L)
    for j in range(len(lengths)):
        sum = (sum + (lengths[j] - mean)**2)
    return (float(sum)/len(lengths)) ** (0.5)
        
 
#L = ['a','z','p']   
L = ['apples', 'oranges', 'kiwis', 'pineapples']
s = stdDevOfLengths(L)