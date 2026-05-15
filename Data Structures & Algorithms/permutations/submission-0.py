class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        curPerm = []

        def helper():
            # Base case
            if len(curPerm) == len(nums):
                res.append(curPerm.copy())
                return

            for i in range(len(nums)):
                if nums[i] not in seen:
                    curPerm.append(nums[i])
                    seen.add(nums[i])
                    helper()
                    curPerm.pop()
                    seen.discard(nums[i])

        helper()
        return res