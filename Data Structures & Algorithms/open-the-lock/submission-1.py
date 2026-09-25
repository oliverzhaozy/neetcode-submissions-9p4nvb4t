class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        visited = set()
        queue = deque(["0000"])

        res = 0
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return res

                for j in range(4):
                    for change in (1, -1):
                        digit = (int(curr[j]) + change) % 10
                        next_state = curr[:j] + str(digit) + curr[j + 1:]                     
                        if next_state not in deadends_set and next_state not in visited:
                            queue.append(next_state)
                            visited.add(next_state)

            res += 1
        
        return -1