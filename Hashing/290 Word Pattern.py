class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split()
        if len(s)!=len(pattern):
            return False
        p_dict={}
        s_dict={}
        l=0
        for i in range(len(s)):
            if s[i] in s_dict and s_dict[s[i]]!=pattern[l]:
                return False
            s_dict[s[i]]=pattern[l]
            l+=1
        l=0
        for i in range(len(pattern)):
            if pattern[i] in p_dict and p_dict[pattern[i]]!=s[l]:
                return False
            p_dict[pattern[i]]=s[l]
            l+=1
        return True
        