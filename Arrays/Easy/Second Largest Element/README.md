# Second Largest Element in an Array

## Problem

Find the second largest element in the given array.

---

## Approach 1 - Brute Force

### Idea
Sort the array and return the second largest distinct element.

### Time Complexity
O(N log N)

### Space Complexity
O(1)

---

## Approach 2 - Better

### Idea
Find the largest element in the first traversal and then find the largest element smaller than it in the second traversal.

### Time Complexity
O(2N)

### Space Complexity
O(1)

---

## Approach 3 - Optimal

### Idea
Find both the largest and second largest elements in a single traversal.

### Time Complexity
O(N)

### Space Complexity
O(1)
