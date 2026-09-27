class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        res = 0
        for i, h in enumerate(heights):
            start_i = i
            while stack and h < stack[-1][0]:
                prev_h, prev_i = stack.pop()
                area =  (i - prev_i) * prev_h
                res = max(area, res)
                start_i = prev_i
            stack.append((h, start_i))
        
        for h, start_i in stack:
            area = (len(heights) - start_i) * h
            res = max(area, res)
        
        return res