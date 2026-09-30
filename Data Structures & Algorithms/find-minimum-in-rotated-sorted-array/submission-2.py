class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[r] > nums[m]: # min lies left of or on m
                r = m - 1
            else: # min lies right of m
                l = m + 1
        
        return res
