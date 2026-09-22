class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, target in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            
            # check for duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                total = nums[l] + nums[r]

                if total < -target:
                    l += 1
                elif total > -target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], target])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res