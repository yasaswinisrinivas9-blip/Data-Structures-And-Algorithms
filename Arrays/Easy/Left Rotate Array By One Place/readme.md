# Left Rotate Array by One Place

## Problem

Given an array, rotate it to the left by **one position**.

The first element should move to the last position, and every other element should shift one position to the left.

---

# Approach - Optimal

## Intuition

Instead of creating another array, we can perform the rotation **in-place**.

Store the first element in a temporary variable.

Shift every remaining element one position to the left.

Finally, place the stored element at the last index.

This completes the left rotation using constant extra space.

---

## Algorithm

1. Store the first element.
2. Traverse the array from index `1` to `n-1`.
3. Shift every element one position to the left.
4. Place the stored first element at the last index.
5. Return the rotated array.

---

## Example

### Input

```python
nums = [1,2,3,4,5]
```

### Step 1

Store the first element.

```text
temp = 1
```

---

### Step 2

Shift all elements to the left.

```text
[2,3,4,5,5]
```

---

### Step 3

Place the stored element at the last position.

```text
[2,3,4,5,1]
```

---

### Output

```python
[2,3,4,5,1]
```

---

## Dry Run

Initial

```text
[1,2,3,4,5]
```

Store

```text
temp = 1
```

After shifting

```text
[2,3,4,5,5]
```

After placing `temp`

```text
[2,3,4,5,1]
```

---

## Time Complexity

**O(N)**

The array is traversed once.

---

## Space Complexity

**O(1)**

Only one temporary variable is used.

---

## Pattern

* Arrays
* In-place Array Manipulation
* Simulation

---

## Key Takeaway

For a left rotation by one position, storing the first element and shifting the remaining elements is the most efficient approach.

It achieves **O(N)** time complexity while using **O(1)** extra space.
