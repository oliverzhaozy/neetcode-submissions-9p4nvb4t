class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[0], height[-1]

        res = 0
        last_moved = l
        while l < r:
            amount = min(maxL, maxR) - height[last_moved]
            maxL, maxR = max(maxL, height[l]), max(maxR, height[r])
            
            if maxR < maxL:
                r -= 1
                last_moved = r
            else: 
                l += 1
                last_moved = l
            
            if amount < 0:
                continue
            res += amount
        
        return res
            