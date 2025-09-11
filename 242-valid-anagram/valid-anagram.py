class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s)!=len(t)):
            return False

        alphabet_arr = [0]*26
        for i,j in zip(s,t):
            alphabet_arr[ord(i)-ord('a')]+=1
            alphabet_arr[ord(j)-ord('a')]-=1
        
        if all(i==0 for i in alphabet_arr):
            return True
        return False