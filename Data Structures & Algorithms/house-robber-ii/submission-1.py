class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums1, nums2 = nums[:-1], nums[1:]

        def dp(nums):
            m = len(nums)
            if m == 1:
                return nums[0]
            dp = [0] * m
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, m):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
            return dp[-1]
        
        return max(dp(nums1), dp(nums2))