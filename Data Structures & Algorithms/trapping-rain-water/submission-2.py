class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        last_moved = l
        res = 0

        while l < r:
            volume = min(maxL, maxR) - height[last_moved]
            
            if maxL < maxR:
                l += 1
                last_moved = l
                maxL = max(maxL, height[l])
            else:
                r -= 1
                last_moved = r
                maxR = max(maxR, height[r])
            
            if volume < 0:
                continue
            res += volume
        
        return res