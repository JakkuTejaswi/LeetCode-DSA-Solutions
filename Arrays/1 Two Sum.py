class Solution(object):
    def twoSum(self, nums, target):
        r=[]
        for i in range(len(nums)):
            sum=0
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    r.append(i)
                    r.append(j)
                    break
        return r
                    
        
        