class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0 
        subsets = [] 

        def generateSubsets(i, curSet):
            # Base case
            if i >= len(nums):
                subsets.append(curSet.copy())
                return
            
            # Choice to include
            curSet.append(nums[i])
            generateSubsets(i + 1, curSet)
            curSet.pop()

            # Choice to exclude
            generateSubsets(i + 1, curSet)

        generateSubsets(0, [])
        for subset in subsets:
            curXOR = 0
            for n in subset:
                curXOR ^= n
            res += curXOR
        
        return res