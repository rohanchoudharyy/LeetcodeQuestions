class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0)+1

        for key,value in hmap.items():
            if hmap.get(key) > 1:
                return True

        return False 