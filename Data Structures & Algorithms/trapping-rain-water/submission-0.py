class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        
        max_so_far = 0
        for i in range(len(height)):
            prefix_max[i] = max_so_far
            max_so_far = max(max_so_far, height[i])
        max_so_far = 0
        for j in range(len(height) - 1, -1, -1):
            suffix_max[j] = max_so_far
            max_so_far = max(max_so_far, height[j])
        
        res = 0
        for i in range(len(height)):
            amount = min(prefix_max[i], suffix_max[i]) - height[i]
            if amount < 0:
                continue
            res += amount
        
        return res