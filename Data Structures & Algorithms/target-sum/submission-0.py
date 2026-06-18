class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(i, curSum, cache):
            # Base case
            if i == len(nums):
                return 1 if curSum == target else 0
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            count = 0
            count += dp(i + 1, curSum + nums[i], cache)
            count += dp(i + 1, curSum - nums[i], cache)
            cache[(i, curSum)] = count
            
            return count
        
        return dp(0, 0, {})