class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        adj_list = defaultdict(list)

        for dst, src in prerequisites:
            in_degree[dst] += 1
            adj_list[src].append(dst)
        
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        count = 0
        while q:
            src = q.popleft()
            count += 1

            for dst in adj_list[src]:
                in_degree[dst] -= 1
                if in_degree[dst] == 0:
                    q.append(dst)
        
        return True if count == numCourses else False