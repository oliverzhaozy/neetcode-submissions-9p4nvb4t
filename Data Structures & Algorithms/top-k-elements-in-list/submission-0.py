class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        ans = []
        for i in range(k):
            maximum = max(hashmap, key=hashmap.get)
            ans.append(maximum)
            hashmap.pop(maximum)
        
        return ans