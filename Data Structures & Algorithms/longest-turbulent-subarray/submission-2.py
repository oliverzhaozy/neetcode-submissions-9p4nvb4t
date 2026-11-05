class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, res = 0, 1
        prev_sign = ""

        for r in range(1, len(arr)):
            if arr[r - 1] < arr[r]:
                if prev_sign != "<": # if prev_sign is ">" or "", the window can be expanded
                    prev_sign = "<"
                else:
                    l = r - 1
                    prev_sign = "<"
            
            elif arr[r - 1] > arr[r]:
                if prev_sign != ">":
                    prev_sign = ">"
                else:
                    l = r - 1
                    prev_sign = ">"
            
            else: # arr[r - 1] == arr[r]
                l = r
                prev_sign = ""
            
            res = max(res, r - l + 1)
        
        return res