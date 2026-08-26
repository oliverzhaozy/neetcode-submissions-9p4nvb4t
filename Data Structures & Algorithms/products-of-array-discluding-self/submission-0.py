class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = nums.count(0)
        res = []

        if zeros > 1:
            return [0] * len(nums)

        for n in nums:
            if n != 0:
                product *= n
        
        for n in nums:
            if zeros == 1:
                res.append(product if n == 0 else 0)
            else:
                res.append(product // n)
        
        return res