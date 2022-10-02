def sortIntByBits(arr):
    bit_data = []

    for n in arr:
        count = bin(n)[2:].count("1")
        bit_data.append([count,n])
    
    bit_data.sort()
    nums = [i[1] for  i in bit_data]

    return nums

print(sortIntByBits([0,1,2,3,4,5,6,7,8]))