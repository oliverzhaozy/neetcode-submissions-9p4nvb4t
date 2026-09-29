class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = {i: [0, 0] for i in range(1, n + 1)} # (how many trusts person, how many person trusts)
        for a, b in trust: # a trusts b 
            adj_list[a][1] += 1
            adj_list[b][0] += 1
        
        count, res = 0, 0
        for person in adj_list:
            if adj_list[person][0] == n - 1 and adj_list[person][1] == 0:
                res = person
                count += 1
        
        return res if (res != 0 and count == 1) else -1