# Check if the Array is Sorted

## Problem

Given an array of integers, determine whether the array is sorted in **non-decreasing order**.

Return:

* `True` if the array is sorted.
* `False` otherwise.

---

## Intuition

A sorted array always satisfies the following condition:

```text
nums[i] >= nums[i - 1]
```

for every element from the second element to the last.

If we ever find an element smaller than its previous element, the array is not sorted.

Since we only need to compare adjacent elements once, a single traversal is sufficient.

---

## Approach

Traverse the array from the second element to the last.

For every index:

* Compare the current element with the previous element.
* If the current element is smaller than the previous one, immediately return `False`.
* If the traversal completes without finding such a pair, return `True`.

---

## Example

### Input

```python
nums = [1, 2, 3, 4, 5]
```

Comparisons:

```text
2 >= 1 ✅
3 >= 2 ✅
4 >= 3 ✅
5 >= 4 ✅
```

Output:

```text
True
```

---

### Input

```python
nums = [1, 3, 2, 4, 5]
```

Comparisons:

```text
3 >= 1 ✅
2 >= 3 ❌
```

Output:

```text
False
```

---

## Time Complexity

**O(N)**

The array is traversed only once.

---

## Space Complexity

**O(1)**

No extra space is used.

---

## Pattern

* Arrays
* Linear Traversal
* Simulation
