class Solution(object):
    def sortArray(self, nums):
        
        def merge(left, right):
            j,k = 0,0
            res = []

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    res.append(left[j])
                    j+=1
                else: 
                    res.append(right[k])
                    k+=1

            while j<len(left):
                res.append(left[j])
                j+=1

            while k<len(right):
                res.append(right[k])
                k+=1
            
            return res

        def mergesort(arr, L, R):
            if L==R:
                return [arr[L]]

            m = (L+R) // 2
            left = mergesort(arr, L, m)
            right = mergesort(arr, m+1, R)
            
            return merge(left, right)
        
        return mergesort(nums, 0, len(nums)-1)

        