class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums):
            return 0
        s = sum(nums)
        nextRow = [0] * (2 * s + 1)
        nextRow[s + target] = 1

        for i in range(len(nums) - 1, -1, -1):
            curRow = [0] * (2 * s + 1)
            for j in range(2 * s + 1):
                if j + nums[i] < 2 * s + 1:
                    curRow[j] += nextRow[j + nums[i]]
                if j - nums[i] >= 0:
                    curRow[j] += nextRow[j - nums[i]]
            nextRow = curRow
        return nextRow[s]