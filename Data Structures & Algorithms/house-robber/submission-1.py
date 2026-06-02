class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1, 1, 3, 3
        def dp(i, cache):
            # Base case
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dp(i + 2, cache), dp(i + 1, cache))
            return cache[i]
        
        return dp(0, {})

