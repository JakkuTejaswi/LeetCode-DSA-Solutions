class Solution(object):
    def largestAltitude(self, gain):
        res=[0]
        sum=0
        for i in range(len(gain)):
            sum+=gain[i]
            res.append(sum)
        return max(res)
        