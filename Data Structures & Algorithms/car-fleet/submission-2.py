class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_to_speed = {}
        for i in range(len(position)):
            pos_to_speed[position[i]] = speed[i]
        position.sort(reverse=True)

        stack = []
        for pos in position:
            speed = pos_to_speed[pos]
            time = (target - pos) / speed

            if stack and time <= stack[-1]: # they will merge
                continue
            else:
                stack.append(time)
        
        return len(stack)