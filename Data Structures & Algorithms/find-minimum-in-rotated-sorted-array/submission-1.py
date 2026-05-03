class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = 9999

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
                min_num = min(nums[mid], min_num)
            else: # nums[mid] < nums[r]
                r = mid - 1
                min_num = min(nums[mid], min_num)

        return min_num
