class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, 0, res, [])
        return res

    def helper(self, nums, index, res, curRes):
        # Base case
        if index >= len(nums):
            res.append(curRes.copy())
            return

        # Choice to include
        curRes.append(nums[index])
        self.helper(nums, index + 1, res, curRes)
        curRes.pop()

        # Choice to not include 
        self.helper(nums, index + 1, res, curRes)