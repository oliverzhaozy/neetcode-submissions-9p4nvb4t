class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dp(i, cache):
            # Base case
            if i >= len(nums) - 1:
                return True
            if i in cache:
                return cache[i]
            
            for jump in range(nums[i], 0, -1):
                if dp(i + jump, cache):
                    cache[i] = True
                    return cache[i]
            cache[i] = False
            return cache[i]
        
        return dp(0, {})