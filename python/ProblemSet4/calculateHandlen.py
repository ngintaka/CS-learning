def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    letters = 0
    for k, v in hand.items():
        letters = letters +v
    return letters
