class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for n in nums:
            val = abs(n)
            map_i = val - 1
            if 0 <= map_i < len(nums) and nums[map_i] > 0:
                nums[map_i] *= -1 
            elif 0 <= map_i < len(nums) and nums[map_i] == 0:
                nums[map_i] = -(len(nums) + 1)
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1