# Left Rotate Array by D Places

## Problem

Given an array of integers and an integer `D`, rotate the array to the left by `D` positions.

The rotation should be performed in-place whenever possible.

---

# Approach 1 - Brute Force

## Intuition

Rotate the array one position to the left, `D` times.

Each rotation shifts every element one position to the left while moving the first element to the end.

Although simple to understand, this approach becomes inefficient when `D` is large.

---

## Algorithm

1. Repeat the following `D` times:

   * Store the first element.
   * Shift all remaining elements one position to the left.
   * Place the stored element at the last index.
2. Return the rotated array.

### Example

Input

```python
nums = [1,2,3,4,5]
D = 2
```

After First Rotation

```text
[2,3,4,5,1]
```

After Second Rotation

```text
[3,4,5,1,2]
```

---

### Time Complexity

**O(N × D)**

---

### Space Complexity

**O(1)**

---

# Approach 2 - Optimal (Reversal Algorithm)

## Intuition

Instead of rotating one step at a time, use the **Reversal Algorithm**.

For left rotation by `D` positions:

1. Reverse the first `D` elements.
2. Reverse the remaining `N-D` elements.
3. Reverse the entire array.

This achieves the rotation in linear time.

---

## Algorithm

1. Compute:

```python
D = D % N
```

2. Reverse the first `D` elements.
3. Reverse the remaining elements.
4. Reverse the entire array.

---

## Example

Input

```python
nums = [1,2,3,4,5,6,7]
D = 2
```

### Step 1

Reverse first `D` elements

```text
[2,1,3,4,5,6,7]
```

### Step 2

Reverse remaining elements

```text
[2,1,7,6,5,4,3]
```

### Step 3

Reverse entire array

```text
[3,4,5,6,7,1,2]
```

Output

```python
[3,4,5,6,7,1,2]
```

---

## Time Complexity

**O(N)**

Three reversals are performed, each taking linear time.

---

## Space Complexity

**O(1)**

The rotation is performed completely in-place.

---

# Pattern

* Arrays
* Reversal Algorithm
* Two Pointers
* In-place Array Manipulation

---

# Key Takeaway

* **Brute Force:** Rotate the array one position at a time (**O(N × D)**).
* **Optimal:** Use the **Reversal Algorithm** to perform the rotation in **O(N)** time with **O(1)** extra space.
