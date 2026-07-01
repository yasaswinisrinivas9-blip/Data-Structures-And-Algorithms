def left_rotate_by_one(nums):
    temp = nums[0]

    for i in range(1, len(nums)):
        nums[i - 1] = nums[i]

    nums[-1] = temp


def left_rotate(nums, d):
    n = len(nums)

    d = d % n

    for _ in range(d):
        left_rotate_by_one(nums)

    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
d = 2

print(left_rotate(nums, d))