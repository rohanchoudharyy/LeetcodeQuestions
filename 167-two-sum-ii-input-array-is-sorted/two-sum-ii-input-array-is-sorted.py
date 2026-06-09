class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for index,value in enumerate(numbers):
            k = target-value
            if k in hmap:
                return [hmap[k]+1,index+1]
            else:
                hmap[value]=index