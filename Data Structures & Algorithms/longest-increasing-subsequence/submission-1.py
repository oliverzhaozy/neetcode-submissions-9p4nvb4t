class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i, prev, cache):
            # Base case
            if i >= len(nums):
                return 0 
            if (i, prev) in cache:
                return cache[(i, prev)]
            
            # Choice to include nums[i]
            include = 0
            if nums[i] > prev:
                include = 1 + dp(i + 1, nums[i], cache)

            # Choice not to include nums[i]
            exclude = dp(i + 1, prev, cache)

            cache[(i, prev)] = max(include, exclude)
            return cache[(i, prev)]
        
        return dp(0, float("-inf"), {})