def iterPower(base, exp):
    ans = base
    if exp == 0:
        ans = 1
    elif exp == 1:
        ans = base
    else:
        while exp > 1:
            ans = ans * base
            exp -= 1
    return ans