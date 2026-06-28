class Solution(object):
    def reverseWords(self, s):
        res=s.split()
        for i in range(len(res)):
            sp=res[i]
            res[i]=sp[::-1]
        return " ".join(res)
        