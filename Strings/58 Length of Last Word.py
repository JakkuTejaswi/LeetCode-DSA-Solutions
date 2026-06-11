class Solution(object):
    def lengthOfLastWord(self, s):
       a=s.strip().split()
       result=len(a[-1])
       return result
        