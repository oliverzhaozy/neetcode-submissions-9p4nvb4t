class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        prefix[0] = nums[0]
        postfix[len(nums) - 1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        for j in range(len(nums) - 2, 0, -1):
            postfix[j] = postfix[j + 1] * nums[j]
        
        res = [0] * len(nums)
        res[0] = postfix[1]
        res[len(nums) - 1] = prefix[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            res[i] = prefix[i - 1] * postfix[i + 1]
    
        return res
