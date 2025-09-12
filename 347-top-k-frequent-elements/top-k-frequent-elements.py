class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = {}
        for i in nums:
            counter[i]=counter.get(i,0)+1

        arr = [[] for _ in range(len(nums)+1)]

        for index,value in counter.items():
            arr[value].append(index)

        ans=[]
        for i in range(len(arr)-1,0,-1):
            for j in arr[i]:
                ans.append(j)
                if(len(ans)==k):
                    return ans

        


        