class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = float("inf")

        while l <= r:
            cur_k, cur_sum = 1, 0
            target = (l + r) // 2
            
            for n in nums:
                cur_sum += n

                if cur_sum > target:
                    cur_k += 1
                    cur_sum = n

                    if cur_k > k:
                        l = target + 1
                        break
            
            if cur_k <= k:
                r = target - 1
                res = min(res, target)
        
        return res
