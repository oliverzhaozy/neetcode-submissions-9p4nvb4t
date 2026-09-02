class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        total = m + n
        half = total // 2
        low, high = 0, m
        
        while low <= high:
            x = (low + high) // 2
            y = half - x

            L1 = nums1[x - 1] if x > 0 else float('-inf')
            R1 = nums1[x] if x < m else float('inf')
            L2 = nums2[y - 1] if y > 0 else float('-inf')
            R2 = nums2[y] if y < n else float('inf')
            
            if L1 > R2:
                high = x - 1
            elif L2 > R1:
                low = x + 1
            else:
                if total % 2 == 1:
                    return float(min(R1, R2))
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0