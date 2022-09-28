def reverse_bits(a):
    return int(bin(a)[2:][::-1], 2)

print(reverse_bits(97))