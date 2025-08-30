class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousNum = {}
        for i, n in enumerate(nums):
            if(target - n in previousNum):
                return [previousNum[target-n], i]
            else:
                previousNum[n] = i
        