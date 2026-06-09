class Solution(object):
    def calPoints(self, operations):
        stack=[]
        tot=0
        for operation in operations:
            if operation=="+":
                num1=stack.pop()
                num2=stack.pop()
                total=int(num1)+int(num2)
                stack.append(num2)
                stack.append(num1)
                stack.append(total)
            elif operation=="D":
                num=stack.pop()
                total=int(num)*2
                stack.append(num)
                stack.append(total)
            elif operation=="C":
                stack.pop()
            else:
                stack.append(operation)
        if stack:
            for num in stack:
                tot+=int(num)
            return tot
        return 0