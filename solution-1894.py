
def chalkReplacer(chalk, k):
    """
    :type chalk: List[int]
    :type k: int
    :rtype: int
    """
    i = 0
    chalk_length = len(chalk)
    while(k >= 0):
        if i == chalk_length:
            i = 0
        k = k - chalk[i]
        i = i + 1
        if k < 0:
            return i
    
            
    return i

print(chalkReplacer([3,4,1,2], 25))