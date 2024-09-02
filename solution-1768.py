class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        if len(word1) >= len(word2):
            i = 0
            for i in range(len(word2)):
                merged = merged + word1[i] + word2[i]
            
            merged += word1[i+1:]
        else:
            for i in range(len(word1)):
                merged = merged + word1[i] + word2[i]

            merged += word2[i+1:]
            
        return merged
            