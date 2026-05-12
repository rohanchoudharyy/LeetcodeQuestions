class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = {'C','+','D'}
        ans = []
        for i in operations:
            if i not in ops:
                ans.append(int(i))
            elif i == 'C':
                ans.pop()
            elif i == 'D':
                ans.append(ans[-1]*2)
            elif i == '+':
                ans.append(ans[-1]+ans[-2])
        
        return sum(ans)