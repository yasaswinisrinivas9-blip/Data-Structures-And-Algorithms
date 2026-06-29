#Brute Force Approach

class Solution:
    
    def removeDuplicate(self, nums):
        
        seen = set()
        
        index = 0
        
        for num in nums:
            
            if num not in seen:
                
                seen.add(num)
                
                nums[index] = num
                
                index += 1
                
        return index
    

sol = Solution()
print(sol.removeDuplicate([0,1,1, 1, 2, 2, 3,3,3,3,4,4]))

'''
Time Complexity - O(n)
Space Complexity - O(n)

'''
