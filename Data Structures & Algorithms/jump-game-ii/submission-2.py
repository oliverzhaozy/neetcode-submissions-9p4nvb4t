class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r, max_r = 0, 0, 0
        count = 0

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                max_r = max(max_r, i + nums[i])
            l = r + 1
            r = max_r
            count += 1
        return count
