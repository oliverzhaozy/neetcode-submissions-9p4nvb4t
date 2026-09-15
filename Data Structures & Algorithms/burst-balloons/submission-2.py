class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dp(left, right):
            # Base case
            if right - left <= 1:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            
            res = 0
            for i in range(left + 1, right):
                coins = nums[left] * nums[right] * nums[i] + dp(left, i) + dp(i, right)
                res = max(res, coins)
            
            cache[(left, right)] = res
            return res
        
        return dp(0, len(nums) - 1)
            

