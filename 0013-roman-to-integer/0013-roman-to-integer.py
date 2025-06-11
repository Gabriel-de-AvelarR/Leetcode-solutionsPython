class Solution:
    simbols = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        sumTotal = 0
        for index in range(len(s)):
            adition = self.simbols[s[index]]
            if(index < len(s) - 1):
                if(self.simbols[s[index]] < self.simbols[s[index + 1]]):
                    adition *= -1

            sumTotal += adition
        
        return sumTotal
        