class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi=0
        for i in range(len(s)):
            count=0
            seen=set()
            for j in range(i,len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    count+=1
                else:
                    break
            maxi=max(count, maxi)
        return maxi
        
        