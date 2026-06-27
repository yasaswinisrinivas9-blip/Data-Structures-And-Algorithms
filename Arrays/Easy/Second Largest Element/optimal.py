#Optimal Approach

class Solution:
    def secondLargest(self, nums):
        
        largest = float('-inf')
        second = float('-inf')
        
        
        for num in nums:
            
            if num > largest:
                second = largest
                largest = num
                
            elif num > second and num != largest:
                second = num
                
        
        return second
    
    
sol = Solution()
arr = [12, 35, 1, 10, 10,33,34, 1]
print(sol.secondLargest(arr))


'''
Time Complexity  - O(n)
Space Complexity - O(1)


'''
