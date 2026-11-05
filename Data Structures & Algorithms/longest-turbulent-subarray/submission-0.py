class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        
        l, r = 0, 1
        res = 0
        prev_sign = None
        if arr[l] < arr[r]:
            prev_sign = "<"
        elif arr[l] > arr[r]:
            prev_sign = ">"
        
        for r in range(1, len(arr)):
            if arr[r - 1] < arr[r] and prev_sign == "<":
                prev_sign = ">"
            elif arr[r - 1] > arr[r] and prev_sign == ">":
                prev_sign = "<"
            elif arr[r - 1] == arr[r]:
                l = r
            else:
                l = r - 1
            
            length = r - l + 1
            res = max(res, length)
        
        return res
            