#Brute Force Approach

class Solution:
    def leftRotateByOnePlace(self,arr,n):
        
        
        temp = [0] * n
        
        if n == 0:
            return temp
        
        for i in range(1, n):
            temp[i-1] = arr[i]
        
        temp[n-1] = arr[0]
        
        return temp
    

sol = Solution()
print(sol.leftRotateByOnePlace([1, 2, 3, 4, 5], 5))
        
        
        
        
        