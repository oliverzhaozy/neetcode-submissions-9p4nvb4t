class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # Left side is sorted
                # Search left sorted portion
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else: # Right side is sorted 
                # Search right sorted portion 
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1 
        
        return -1 

