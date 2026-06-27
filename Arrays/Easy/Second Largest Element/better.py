#Better Approach

class Solution:
    def largestElement(self,nums):
        
        largest = max(nums)
        
        second = float('-inf')
        
        for num in nums:
            if num != largest:
                second = max(second,num)
            
        return second
    

sol = Solution()
print(sol.largestElement([1, 2, 3, 4,3, 4,8, 5]))

'''


Time Complexity  - O(n)
Space Complexity - O(1)

'''
