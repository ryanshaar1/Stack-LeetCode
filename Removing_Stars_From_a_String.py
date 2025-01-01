class Solution(object):
    def removeStars(self, s):
        stack =[]
        for char in s:
            if char != '*':
                stack.append(char)
            else:
                if stack != []:
                    stack.pop()
        return "".join(stack)    