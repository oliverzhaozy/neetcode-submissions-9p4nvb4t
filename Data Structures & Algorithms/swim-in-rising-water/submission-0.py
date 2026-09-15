class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = [(grid[0][0], 0, 0)] # elevation, row, col
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        res = 0
        while minHeap:
            elev, r, c = heapq.heappop(minHeap)
            res = max(res, elev)
            if r == n - 1 and c == n - 1:
                return res

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= 0 and nc >= 0 and nr < n and nc < n and (nr, nc) not in visited:
                    heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                    visited.add((nr, nc))
