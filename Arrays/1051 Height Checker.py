class Solution(object):
    def heightChecker(self, heights):
        h=sorted(heights)
        count=0
        for i in range(len(heights)):
            if h[i]!=heights[i]:
                count+=1
        return count
        