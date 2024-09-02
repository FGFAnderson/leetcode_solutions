class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        nextval = 0
        for count, numeral in enumerate(s):
            val = values[numeral]
            if count + 1 < len(s):
                nextval = values[s[count+1]]
                if nextval > val:
                    total = total - val
                    continue

            total = total + val

        return total