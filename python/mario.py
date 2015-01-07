def mario():
    height = int(raw_input("Height: "))
    base = height + 1
    width = 2
    
    if 0 < height < 23:
        while width <= base:
            print ' ' * (base-width) + '*' * width
            width += 1
        
    else:
        return mario()
mario()        