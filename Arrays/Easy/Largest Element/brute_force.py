#Brue Force Approach

def largestelement(arr):
    
    arr.sort()
    
    return arr[-1]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print(largestelement(arr))
    
    
'''

Time Complexity - o(n log n)
Space Complexity - o(1)

'''
