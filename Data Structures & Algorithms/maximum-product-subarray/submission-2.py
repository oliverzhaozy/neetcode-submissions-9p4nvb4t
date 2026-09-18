class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = 1
        res = nums[0]

        for n in nums:
            temp = cur_max
            cur_max = max(cur_max * n, cur_min * n, n)
            cur_min = min(temp * n, cur_min * n, n)
            res = max(res, cur_max)
        return res