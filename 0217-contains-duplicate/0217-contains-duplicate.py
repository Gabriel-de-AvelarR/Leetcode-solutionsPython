class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        previousNum = set() 
        
        for n in nums:
            if(n in previousNum):
                return True
            else:
                 previousNum.add(n)
        
        return False
            