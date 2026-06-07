class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)<1:
            return 0
        r=[]
        s=set(nums)
        nums=list(s)
        nums.sort()
        count=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                count+=1
            else:
                r.append(count)
                count=1
        r.append(count)
        return max(r)
