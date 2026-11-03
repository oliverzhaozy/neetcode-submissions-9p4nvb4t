class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            curWeight = people[r]
            if curWeight + people[l] <= limit:
                l += 1
            res += 1
            r -= 1
        
        return res