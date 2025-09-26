class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = {}
        for i in s:
            counter[i] = counter.get(i,0)+1

        for idx, val in enumerate(s):
            if counter[val] == 1:
                return idx
        return -1