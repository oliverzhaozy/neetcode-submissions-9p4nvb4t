class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set()
        for n in nums:
            seen.add(n)
        
        res = 1
        for n in nums:
            if (n - 1) not in seen:
                longest = 1
                while (n + 1) in seen:
                    longest += 1
                    res = max(res, longest)
                    n += 1
        
        return res