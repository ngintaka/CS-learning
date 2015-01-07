def sem(str1,str2):

    if len(str1) != len(str2):
        return False
    if len(str1) >= 1:
        if str1[0] != str2[-1]:
            return False
        else:
            return sem(str1[1:],str2[:-1])
    return True
