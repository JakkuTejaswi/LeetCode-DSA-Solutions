class Solution(object):
    def minStartValue(self, nums):
        start=1
        while True:
            curr=start
            valid=True
            for num in nums:
                curr+=num
                if curr<1:
                    valid=False
                    break
            if valid:
                return start
            start+=1

        