def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n <= 5:
        return False

    elif n%20 == 0 or n%9 == 0 or n%6 == 0:
        return True

    elif n/20/9/6 ==0 or n/20/6/9 ==0 or n/20/9 == 0 or n/20/6 ==0:
        return True

    elif n/9/20/6 == 0 or n/9/6/20 == 0 or n/9/20 ==0 or n/9/6 ==0:
        return True

    elif n/6/20/9 == 0 or n/6/9/20 == 0 or n/6/20 ==0 or n/6/9 ==0:
        return True

    else:
        return False
