class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        adj = {}
        for i in range(n):
            adj[i] = []
        for s, d, p in flights: # s = source, d = destination, p = price
            adj[s].append((d, p))

        q = deque([(0, src, 0)])
        while q:
            curCost, node, stops = q.popleft()
            if stops > k:
                continue
            
            for neighbour, price in adj[node]:
                nextCost = curCost + price
                if nextCost < prices[neighbour]:
                    prices[neighbour] = nextCost
                    q.append((nextCost, neighbour, stops + 1))
        
        return prices[dst] if prices[dst] != float("inf") else -1