
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if len(strs) == 1:
            return strs[0]
            
    largestPrefix = ""
    for i in range(len(strs[0])):
        prefix = strs[0][:i+1]
        for compare in strs[1:]:
            if not compare.startswith(prefix):
                return largestPrefix
        largestPrefix = prefix

    return largestPrefix


print("Longest:" + longestCommonPrefix(["reflower","flow","flight"]))