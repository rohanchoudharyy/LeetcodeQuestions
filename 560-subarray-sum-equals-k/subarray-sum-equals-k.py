class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        hmap = {}
        hmap[0]=1
        count = 0

        for i in nums:
            sum+=i
            if sum-k in hmap:
                count += hmap[sum-k]
                hmap[sum]=hmap.get(sum,0)+1
            else:
                hmap[sum]=hmap.get(sum,0)+1
        
        return count
