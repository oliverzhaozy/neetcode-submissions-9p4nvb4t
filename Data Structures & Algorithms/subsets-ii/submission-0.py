class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curRes = []
        nums.sort()

        def helper(index):
            # Base case
            if index >= len(nums):
                res.append(curRes.copy())
                return
            
            num = nums[index]

            # Choice to include
            curRes.append(num)
            helper(index + 1)

            # Choice not to include
            curRes.pop()
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            helper(index + 1)

        helper(0)
        return res