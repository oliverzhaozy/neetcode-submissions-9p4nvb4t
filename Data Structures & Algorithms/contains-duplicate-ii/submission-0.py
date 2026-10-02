class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)
        for i, n in enumerate(nums):
            hashmap[n].append(i)
        
        for key in hashmap:
            if len(hashmap[key]) < 2:
                continue
            i = 0
            while (i + 1) < len(hashmap[key]):
                if abs(hashmap[key][i] - hashmap[key][i + 1]) <= k:
                    return True
                i += 1
        return False
