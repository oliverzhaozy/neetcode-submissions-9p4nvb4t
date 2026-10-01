class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        max_num, max_count = nums[0], 0

        for num in nums:
            if num == max_num:
                max_count += 1
            else:
                max_count -=1
                if max_count < 0:
                    max_num = num
                    max_count = 0
        
        return max_num