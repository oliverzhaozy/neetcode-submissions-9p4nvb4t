class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        running_sum, res = 0, 0
        for n in nums:
            running_sum += n
            if (running_sum - k) in hashmap:
                res += hashmap[running_sum - k]
            
            hashmap[running_sum] = hashmap.get(running_sum, 0) + 1
        
        return res