def updateHand(hand,word):

    newHand = hand.copy()

    for l in word:
        if l in newHand:
            newHand[l] = newHand[l]-1

    for k, v in newHand.items():
        if v == 0:
            del newHand[k]

    return newHand

updateHand({'a': 1, 'r': 1, 'e': 3, 'd': 2},'red')
    
