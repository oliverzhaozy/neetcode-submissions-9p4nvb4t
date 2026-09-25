class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0] * 1001
        for t in trips:
            numPass, start, end = t
            passChange[start] += numPass
            passChange[end] -= numPass
        
        curPass = 0
        for change in passChange:
            curPass += change
            if curPass > capacity:
                return False
        return True