class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1, nums2 = nums[:-1], nums[1:]

        def dp(i, nums, cache):
            # Base case
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(dp(i + 2, nums, cache) + nums[i], dp(i + 1, nums, cache))
            return cache[i]
        
        return max(dp(0, nums1, {}), dp(0, nums2, {}))