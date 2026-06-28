#Optimal Approach

class Solution:
    def isSorted(self,arr):
        
        for i in range(1,len(arr)):
            
            if arr[i] < arr[i-1]:
                return False
        return True
        

sol = Solution()
arr = [1, 2, 3, 4, 9,5]
print(sol.isSorted(arr))


'''
Time Complexity - o(n)
Space Complexity - o(1)

'''
