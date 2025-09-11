class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_map = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            count_map[tuple(count)].append(i)
        ans = list(count_map.values())
        return ans

