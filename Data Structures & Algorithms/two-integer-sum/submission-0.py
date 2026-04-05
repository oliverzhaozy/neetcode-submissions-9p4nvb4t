class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dict to keep track of numbers already seen
        seen = {}

        for i, num in enumerate(nums):
            # Calculate number to look out for in nums
            # Target 7, first num 3, difference 4
            difference = target - num
            if difference in seen:
                return [seen[difference], i]
            seen[num] = i
        