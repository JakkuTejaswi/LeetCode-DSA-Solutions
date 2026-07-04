class Solution(object):
    def findMiddleIndex(self, nums):
        prefix=[]
        suffix=[]
        left=0
        for i in range(len(nums)):
            suffix.append(left)
            left+=nums[i]
        right=0
        for i in range(len(nums)-1,-1,-1):
            prefix.append(right)
            right+=nums[i]
        prefix=prefix[::-1]
        l=0
        r=0
        while l<len(prefix) and r<len(suffix):
            if prefix[l]==suffix[l]:
                return l
            l+=1
            r+=1
        return -1
        
        

        