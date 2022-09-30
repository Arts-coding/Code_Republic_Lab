def shape_area(n):
    if n >= 10**4 or n < 1:
        return False
        
    res = n**2 + (n-1)**2
    
    return res
print(shape_area(3))