class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        
        j = 0
        for i in range(len(nums)):
            while hashmap.get(j, 0) == 0:
                j += 1

            nums[i] = j
            hashmap[j] -= 1