def solution(n, k):
    return n & ~(1 << (k - 1))

print(solution(37, 3)) 

