class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curRes = []
        candidates.sort()

        def dfs(index, curSum):
            # Base case
            if curSum == target:
                res.append(curRes.copy())
                return
            if index >= len(candidates) or curSum > target:
                return

            num = candidates[index]

            # Choice to include
            curRes.append(num)
            dfs(index + 1, curSum + num)
            
            # Choice not to include
            curRes.pop()
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            dfs(index + 1, curSum)

        dfs(0, 0)
        return res