class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0)+1

        for key,value in hmap.items():
            if value > 1:
                return True

        return False 