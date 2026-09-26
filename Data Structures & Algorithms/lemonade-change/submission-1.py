class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount, tenCount = 0, 0
        for b in bills:
            if b == 5:
                fiveCount += 1
            elif b == 10:
                tenCount += 1
                fiveCount -= 1
            else:
                if tenCount > 0:
                    tenCount -= 1
                    fiveCount -=1
                else:
                    fiveCount -= 3
            
            if fiveCount < 0 or tenCount < 0:
                return False
        
        return True
