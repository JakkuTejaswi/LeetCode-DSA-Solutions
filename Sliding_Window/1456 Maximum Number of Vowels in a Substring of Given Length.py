class Solution(object):
    def maxVowels(self, s, k):
        l=0
        count=0
        max_count=0
        st=""
        for r in range(len(s)):
            st+=s[r]
            if s[r] in "aeiou":
                count+=1
            if r-l+1==k:
                max_count=max(count, max_count)
                if s[l] in "aeiou":
                    count-=1
                l+=1
                st=st[l:r+1]
        return max_count

        