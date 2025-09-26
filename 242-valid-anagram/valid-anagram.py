class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr = [0]*26
        for i in s:
            arr[ord(i) - ord('a')] += 1
        
        for i in t:
            arr[ord(i) - ord('a')] -= 1
        
        for i in arr:
            if i!=0:
                return False
        return True