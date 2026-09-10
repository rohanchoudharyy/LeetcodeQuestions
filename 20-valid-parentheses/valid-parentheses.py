class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '(':')',
            '{':'}',
            '[':']'
        }

        stack = []
        for i in s:
            if i in hmap:
                stack.append(i)
            elif i in hmap.values():
                if not stack:
                    return False
                if (hmap[stack[-1]]==i):
                    stack.pop()
                else :
                    return False
        
        return not stack


