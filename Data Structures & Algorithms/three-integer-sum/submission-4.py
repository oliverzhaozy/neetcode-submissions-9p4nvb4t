class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        ans = []

        for i in range(length - 1):
            j, k = i + 1, length - 1
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                else: 
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        
        return ans
        # [-4, -1, -1, 0, 1, 2]
        # nums[j] + nums[k] = -nums[i]