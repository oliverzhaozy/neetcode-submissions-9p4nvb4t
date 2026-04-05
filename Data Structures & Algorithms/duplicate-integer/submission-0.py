class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for num in nums:
            dict[num] = dict.get(num, 0) + 1
            if dict[num] > 1:
                return True
        return False