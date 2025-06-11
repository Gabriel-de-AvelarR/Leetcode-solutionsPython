class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)

        sequence = self.intToList(x)
        reversedInt = self.reversedListToInt(sequence) 
        reversedInt *= sign

        if(reversedInt < INT_MAX and reversedInt > INT_MIN):
            return reversedInt 
        else:
            return 0

    def intToList(self, number):
        return[int(digit) for digit in str(number)]
    def reversedListToInt(self, sequence):
        totalSum = 0
        for i in range(len(sequence)):
            totalSum+= sequence[i]*10**(i)
        return totalSum