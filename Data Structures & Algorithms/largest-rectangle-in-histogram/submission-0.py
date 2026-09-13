class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonic increasing stack containing (index of last popped element, height)
        res = 0

        for i, height in enumerate(heights):
            last_i = i
            while stack and stack[-1][1] > height: # if next height is decreasing
                last_i, last_height = stack.pop()
                area = last_height * (i - last_i)
                res = max(area, res)
            
            stack.append((last_i, height))
        
        for i, height in stack:
            res = max(res, height * (len(heights) - i))
        
        return res