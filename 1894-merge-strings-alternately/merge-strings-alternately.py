class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        ans = ''
        i,j = 0,0

        while i<len(word1) and j<len(word2):
            ans+=word1[i]
            ans+=word2[j]
            i,j = i+1,j+1
        print (i,j)
        
        if i<len(word1):
            ans+=word1[i:]
        
        if j<len(word2):
            ans+=word2[j:]

        return ans