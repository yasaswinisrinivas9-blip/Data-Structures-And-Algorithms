#Optimal Approach

class Solution:
    def largestelement(self, arr):
        
        largest = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] > largest:
                largest = arr[i]
        return largest
    
sol = Solution()
arr = [1,2,9,8,6]
print(sol.largestelement(arr))

'''
Time Complexity - o(n)
Space Complexity - o(1)

'''
