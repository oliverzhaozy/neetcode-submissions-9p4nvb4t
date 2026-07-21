class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        
        dp = [[False] * (len(nums) + 1) for _ in range(target + 1)]
        for i in range(len(nums) + 1):
            dp[0][i] = True
        for j in range(1, target + 1):
            dp[j][0] = False

        for i in range(1, target + 1):
            for j in range(1, len(nums) + 1):
                exclude = dp[i][j - 1]
                include = False
                if i - nums[j-1] >= 0:
                    include = dp[i - nums[j-1]][j - 1] 
                
                dp[i][j] = exclude or include
        
        return dp[-1][-1]
                