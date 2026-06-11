class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        left=strs[0]
        right=strs[-1]
        result=""
        for i in range(min(len(left), len(right))):
            if left[i]==right[i]:
                result+=left[i]
            else:
                break
        return result