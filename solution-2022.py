class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int rows
        :type n: int cols
        :rtype: List[List[int]]
        """
        output = []
    
        if len(original) != m*n:
            return []

        for i in range(1,m+1):
            output.append(original[(i-1)*n:i*n])


        return output
                