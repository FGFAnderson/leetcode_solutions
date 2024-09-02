class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        while i < len(s):
            numeral = s[i]
            if numeral == "I":
                if i + 1 < len(s) and s[i + 1] == "V":
                    total += 4
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "X":
                    total += 9
                    i += 1
                else:
                    total += 1
            elif numeral == "V":
                total += 5
            elif numeral == "X":
                if i + 1 < len(s) and s[i + 1] == "L":
                    total += 40
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "C":
                    total += 90
                    i += 1
                else:
                    total += 10
            elif numeral == "L":
                total += 50
            elif numeral == "C":
                if i + 1 < len(s) and s[i + 1] == "D":
                    total += 400
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "M":
                    total += 900
                    i += 1
                else:
                    total += 100
            elif numeral == "D":
                total += 500
            elif numeral == "M": 
                total += 1000
            i += 1
        return total
