class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsSet = set(nums)

        largest = 0
        for i in numsSet:
            #check if i is the starting of a series by checking if a i-1 no exists
            if (i-1) not in numsSet:
                length = 1
                while(i+length) in numsSet:
                    length += 1
                largest = max(largest,length)
        return largest