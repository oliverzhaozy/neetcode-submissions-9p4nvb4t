class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curRes = []

        def helper(index, curSum):
            # Base case
            if curSum == target:
                res.append(curRes.copy())
                return
            if index >= len(nums) or curSum > target:
                return

            num = nums[index]

            # Choice to include
            curRes.append(num)
            helper(index, curSum + num)
            curRes.pop()

            # Choice to not include
            helper(index + 1, curSum)

        helper(0, 0)
        return res