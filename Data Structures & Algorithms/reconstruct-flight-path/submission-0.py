class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj_list[src].append(dst)
        
        res = []
        def dfs(src):
            while adj_list[src]:
                dst = adj_list[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]

