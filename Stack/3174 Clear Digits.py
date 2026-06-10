class Solution(object):
    def clearDigits(self, s):
        stack=[]
        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)