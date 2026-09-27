class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.res = 0 
        subsets = [] 

        def generateSubsets(i, total):
            # Base case
            if i >= len(nums):
                self.res += total
                return
            
            # Choice to include
            generateSubsets(i + 1, total ^ nums[i])

            # Choice to exclude
            generateSubsets(i + 1, total)

        generateSubsets(0, 0)
        return self.res