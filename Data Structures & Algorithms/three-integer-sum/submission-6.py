class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        seen = set()
        ans = []

        for i in range(length - 1):
            j, k = i + 1, length - 1

            while j < k:
                if nums[j] + nums[k] < -nums[i]:
                    j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] == -nums[i] and tuple([nums[i], nums[j], nums[k]]) not in seen: 
                    ans.append([nums[i], nums[j], nums[k]])
                    seen.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                else:
                    j += 1
                    k -= 1


        return ans