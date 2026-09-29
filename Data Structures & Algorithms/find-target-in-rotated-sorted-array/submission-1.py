class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            left_val, mid_val, right_val = nums[l], nums[m], nums[r]

            if mid_val == target:
                return m

            if right_val > mid_val: # pivot point lies left of m
                if mid_val <= target <= right_val:
                    l = m + 1
                else:
                    r = m - 1

            else: # pivot point lies right of m
                if left_val <= target <= mid_val:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1