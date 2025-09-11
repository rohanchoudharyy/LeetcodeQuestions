class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for index,value in enumerate(nums):
            if value in count:
                count[value]=count[value]+1
            else:
                count[value]=1
        for key, value in count.items():
            if (value>len(nums)/2):
                return key
        return 1