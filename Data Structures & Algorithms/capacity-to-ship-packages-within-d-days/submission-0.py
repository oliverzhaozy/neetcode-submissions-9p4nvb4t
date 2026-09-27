class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        def helper(target):
            count, runningSum = 1, 0
            for w in weights:
                runningSum += w
                if runningSum > target:
                    count += 1
                    runningSum = w
            return count 

        res = float("inf")
        while low <= high:
            target = (low + high) // 2
            days_needed = helper(target)
            
            if days_needed <= days:
                high = target - 1
                res = min(res, target)
            else:
                low = target + 1

        return res