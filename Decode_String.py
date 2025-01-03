#This one was hard for me idk why
class Solution(object):
    def decodeString(self, s):
        stack_nums = []
        stack_strings = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == "[":
                stack_nums.append(current_num)
                stack_strings.append(current_string)
                current_string = ""
                current_num = 0
            elif char == "]":
                num = stack_nums.pop()
                previous_string = stack_strings.pop()
                current_string = previous_string + current_string * num
            else:
                current_string += char

        return current_string
