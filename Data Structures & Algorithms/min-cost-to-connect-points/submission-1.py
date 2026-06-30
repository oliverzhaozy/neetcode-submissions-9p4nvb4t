class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {}
        for i in range(n):
            adj[i] = []

        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        cost = 0
        visit = set()
        minHeap = [[0, 0]]

        while len(visit) < n:
            dist, i = heapq.heappop(minHeap)
            if i in visit:
                continue
            visit.add(i)
            cost += dist
            for dist, neighbour in adj[i]:
                if neighbour not in visit:
                    heapq.heappush(minHeap, [dist, neighbour])
        
        return cost
