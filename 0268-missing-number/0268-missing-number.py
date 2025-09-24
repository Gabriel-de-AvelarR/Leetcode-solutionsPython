class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        vector = [-1] * (size + 1)

        for num in nums:
            vector[num] = num
        
        for i in range(size + 1):
            if vector[i] == -1:
                return i