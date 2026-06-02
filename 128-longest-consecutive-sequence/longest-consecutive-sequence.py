class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = set(nums)

        ans = 0
        for i in lst:
            length = 0
            if i-1 not in lst:
                length=1
                while i+length in lst:
                    length+=1
            ans = max(length, ans)

        return ans