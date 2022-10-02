def merge(nums1: list, m: int, nums2:list, n: int) -> None:
        
        nums1[n:] = nums1[0:m] 
        i =  i1 = i2 = 0
        
        while i1 < m and i2 < n:
            if nums1[n+i1] <= nums2[i2]:
                nums1[i] = nums1[n+i1]
                i1 += 1
                i += 1
            else:
                nums1[i] = nums2[i2]
                i2 += 1
                i += 1
        if i1 == m: 
            nums1[i:] = nums2[i2:]