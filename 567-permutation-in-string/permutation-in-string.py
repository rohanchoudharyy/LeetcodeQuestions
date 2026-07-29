class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        stringone={}     
        for char in s1:
            stringone[char]=stringone.get(char,0)+1
        
        i=0
        j=len(s1)-1

        while j<len(s2):
            stringtwo={}   
            window = s2[i:j+1]
            for char in window:
                stringtwo[char]=stringtwo.get(char,0)+1
            if stringone == stringtwo:
                return True
            i+=1
            j+=1
        
        return False
                
