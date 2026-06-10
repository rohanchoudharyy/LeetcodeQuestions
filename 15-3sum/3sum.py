class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        
        for index,value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            l,r = index+1,len(nums)-1
            while r>l:
                threesum = value + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum <0:
                    l+=1
                else:
                    ans.append([value,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and r>l:
                        l+=1
        return ans

