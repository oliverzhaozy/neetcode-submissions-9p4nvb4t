class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        ans = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, count in count.items():
            freq[count].append(num)
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                
                if len(ans) == k:
                    return ans
