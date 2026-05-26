class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        p_queue, a_queue = deque(), deque()
        pacific, atlantic = set(), set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # Append the border grids to the queue
        for row in range(ROWS):
            p_queue.append((row, 0)) # left column
            pacific.add((row, 0))
            a_queue.append((row, COLS - 1)) # right column
            atlantic.add((row, COLS - 1))

        for col in range(COLS):
            p_queue.append((0, col)) # top row
            pacific.add((0, col))
            a_queue.append((ROWS - 1, col)) # bottom row 
            atlantic.add((ROWS - 1, col))
        
        def bfs(queue, hashset):
            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and (nr, nc) not in hashset and heights[nr][nc] >= heights[row][col]:
                        hashset.add((nr, nc))
                        queue.append((nr, nc))

        bfs(p_queue, pacific)
        bfs(a_queue, atlantic)

        res = []
        common = pacific & atlantic
        for coords in common:
            res.append(list(coords))
        return res