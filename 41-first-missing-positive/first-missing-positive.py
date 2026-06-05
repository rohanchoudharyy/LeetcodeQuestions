class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_new = set(nums)
        
        if len(nums)==1:
            for i in range(1,len(nums)+1):
                if 1 in nums_new:
                    return 2
                else:
                    return 1

        for i in range(1,len(nums)+1):
            if i not in nums_new:
                return i
        
        return len(nums)+1
