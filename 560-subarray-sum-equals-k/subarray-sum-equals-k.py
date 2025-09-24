class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans=0
        sum=0
        hmap = {}
        hmap[0] = 1
        for i in nums:
            sum+=i
            diff = sum-k
            ans += hmap.get(diff,0)
            hmap[sum] = hmap.get(sum,0)+1
        return ans