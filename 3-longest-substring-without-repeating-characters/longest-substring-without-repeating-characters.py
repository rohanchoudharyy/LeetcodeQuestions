class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        ans = 0
        seen = set()
        for j in range(len(s)):
            while (s[j] in seen):
                seen.remove(s[i])
                i+=1
            seen.add(s[j])
            ans = max(ans,len(seen))

        return ans
            