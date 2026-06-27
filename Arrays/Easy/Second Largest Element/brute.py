#Brute Force Approach

class Solution:
    def secondlargest(self,arr):
        
        arr.sort()
        
        return arr[-2]
    
    
sol = Solution()
arr = [1,3,5,7,7,8]
print(sol.secondlargest(arr))

#Second Largest should be 5 here in case of duplicates it won't work.


'''
Time Complexity - O(n log n)
Space Complexity - O(1)

'''
