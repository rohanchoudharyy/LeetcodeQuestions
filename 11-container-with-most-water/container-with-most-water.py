class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j, max_area = 0, len(height)-1, 0
        while j>i:
            min_height = min(height[i],height[j])
            max_area = max(max_area, min_height*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area

