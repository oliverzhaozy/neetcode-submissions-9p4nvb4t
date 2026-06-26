class Solution:
    def jump(self, nums: List[int]) -> int:
        def dp(i, cache):
            # Base case
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]
            
            count, min_jump = 0, 9999
            for jump in range(1, nums[i] + 1):
                count = 1 + dp(i + jump, cache)
                min_jump = min(count, min_jump)
            
            cache[i] = min_jump
            return cache[i]
            
        return dp(0, {})