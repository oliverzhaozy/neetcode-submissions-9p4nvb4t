class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and (stack[-2] > 0 and stack[-1] < 0):
                s1 = stack.pop()
                s2 = stack.pop()
                if abs(s1) < abs(s2):
                    stack.append(s2)
                elif abs(s1) > abs(s2):
                    stack.append(s1)
                else:
                    continue
        
        return stack