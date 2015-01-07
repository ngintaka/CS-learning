def recurPower(base,exp):
    ans = 0
    if exp == 0:
        return 1
    else:
        return base * recurPower(base,exp-1)
