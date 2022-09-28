def single_element(nums):
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = start + (end - start)//   2

        if nums[mid + 1] != nums[mid] != nums[mid - 1]:
            return nums[mid]
        elif nums[mid] == nums[mid-1] and mid%2 == 0:
            end = mid - 2
        elif nums[mid] == nums[mid-1] and mid%2 != 0:
                start = mid + 1
        elif nums[mid] == nums[mid+1] and mid%2 == 0:
                start = mid + 2
        elif nums[mid] == nums[mid+1] and mid%2 != 0:
                end = mid - 1
    return nums[start]

print(single_element([1, 1, 2, 3, 3, 4, 4, 8, 8]))