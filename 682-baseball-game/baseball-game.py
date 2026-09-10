class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = {'+','D','C'}
        stack = []
        for i in operations:
            if (i=='+'):
                stack.append(stack[-1]+stack[-2])
            elif (i=='D'):
                stack.append(stack[-1]*2)
            elif(i=='C'):
                stack.pop()
            else: 
                stack.append(int(i))
            
        sum=0
        for i in stack:
            sum+=i
        
        return sum
