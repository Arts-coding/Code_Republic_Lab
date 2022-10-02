def intersection(nums1: list, nums2: list):
        result = []

        if len(nums2) <= len(nums1):
            for i in range(0, len(nums1)):
                if (nums1[i] in nums2) and (nums1[i] not in result):
                    result.append(nums1[i])
        else:
            for i in range(0, len(nums2)):
                if (nums2[i] in nums1) and (nums2[i] not in result):
                    result.append(nums2[i])

        return result