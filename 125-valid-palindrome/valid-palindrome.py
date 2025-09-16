class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = ""
        for i in s:
            if i.isalnum():
                ss+=(i.lower())
        rev = ss[::-1]
        if ss!=rev:
            return False
        return True