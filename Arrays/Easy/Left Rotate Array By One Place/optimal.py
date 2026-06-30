#Optimal Approach

class Solution:
    def leftRotateArrayByOnePlace(self,nums):
        
        temp = nums[0]
        
        for i in range(1,len(nums)):
            
            nums[i-1] = nums[i]
            
        nums[-1] = temp
            
        return nums
        
print(Solution().leftRotateArrayByOnePlace([1, 2, 3, 4, 5]))