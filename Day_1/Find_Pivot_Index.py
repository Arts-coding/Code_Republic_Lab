def find_pivot_index(nums):
    sum_el = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        if left_sum == (sum_el - left_sum - nums[i]):
            return i
        left_sum += nums[i]
    return -1

print(find_pivot_index([1, 7, 3, 6, 5, 6]))