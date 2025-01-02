
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if abs(asteroid) > abs(stack[-1]):
                    stack.pop()  
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()  
                break
            else:
                stack.append(asteroid)
        
        return stack
