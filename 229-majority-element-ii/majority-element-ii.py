class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = {}
        lst = []
        for index, value in enumerate(nums):
            counter[value] = counter.get(value,0)+1

        for key, value in counter.items():
            if (value>(len(nums)/3)):
                lst.append(key)
        
        return lst