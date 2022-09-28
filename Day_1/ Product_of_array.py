from types import new_class


def  product_of_array(nums):
    res = 1
    new_nums = [1]

    for i in range(1,len(nums)):
        res *= nums[i - 1]
        new_nums.append(res)

    print(new_nums)

    res = 1

    for y in range(len(new_nums) - 1, -1, -1):
        new_nums[y] *= res 
        res *= nums[y]
    
    return new_nums

print(product_of_array([1, 2, 3, 4]))