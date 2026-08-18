class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        pairs.sort(key=lambda x: x[0], reverse=True)
        stack = [(target - pairs[0][0]) / pairs[0][1]]

        for p, s in pairs:
            time = (target - p) / s

            if time <= stack[-1]:
                continue
            else:
                stack.append(time)
        
        return len(stack)
