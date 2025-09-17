class Solution(object):

    def isPalindrome(self, s):
        def alnum(string):
            return ((ord('a') <= ord(string) <= ord('z')) or
            (ord('A') <= ord(string) <= ord('Z')) or
            (ord('0') <= ord(string) <= ord('9')))

        s=s.lower()
        i,j = 0,len(s)-1
        while(i<j):
            if not alnum(s[i]):
                i+=1
                continue
            if not alnum(s[j]):
                j-=1
                continue
            if (s[i]!=s[j]):
                return False
            i+=1
            j-=1
        
        return True