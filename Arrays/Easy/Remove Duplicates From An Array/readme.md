# Remove Duplicates from Sorted Array

## Problem

Given a **sorted** array, remove the duplicate elements **in-place** such that each unique element appears only once.

Return the number of unique elements after removing duplicates.

---

# Approach 1 - Brute Force

## Intuition

Since the array is sorted, we can traverse it and store only the unique elements in a temporary array.

After collecting all unique elements, copy them back into the original array.

Although simple, this approach requires extra space.

### Algorithm

1. Create an empty temporary array.
2. Insert the first element.
3. Traverse the original array.
4. Whenever the current element differs from the previous one, append it to the temporary array.
5. Copy the temporary array back to the original array.
6. Return the size of the temporary array.

### Example

Input

```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

Temporary Array

```text
[0,1,2,3,4]
```

Modified Array

```text
[0,1,2,3,4]
```

### Time Complexity

**O(N)**

### Space Complexity

**O(N)**

---

# Approach 2 - Optimal (Two Pointers)

## Intuition

Since the array is already sorted, duplicate elements are adjacent.

Instead of using another array, maintain two pointers:

* `i` → Last unique element
* `j` → Current element being checked

Whenever a new unique element is found:

* Move `i` one step forward.
* Copy `nums[j]` to `nums[i]`.

This modifies the array in-place without extra memory.

---

## Dry Run

Input

```python
nums = [0,0,1,1,1,2,2,3,3,4]
```

Initially

```text
[0,0,1,1,1,2,2,3,3,4]
 i j
```

Unique element `1`

```text
[0,1,1,1,1,2,2,3,3,4]
    i   j
```

Unique element `2`

```text
[0,1,2,1,1,2,2,3,3,4]
      i     j
```

Unique element `3`

```text
[0,1,2,3,1,2,2,3,3,4]
        i       j
```

Unique element `4`

```text
[0,1,2,3,4,2,2,3,3,4]
          i         j
```

Final Unique Elements

```text
[0,1,2,3,4]
```

Return

```python
5
```

---

## Time Complexity

**O(N)**

The array is traversed only once.

---

## Space Complexity

**O(1)**

The array is modified in-place without using additional memory.

---

# Pattern

* Arrays
* Two Pointers
* In-place Array Modification

---

# Key Takeaway

* **Brute Force:** Easy to understand but requires extra memory.
* **Optimal:** Uses the **Two Pointers** technique to achieve **O(N)** time complexity with **O(1)** extra space, making it the preferred solution for interviews.
