import math
class Solution(object):
    def majorityElement(self, nums):
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        res=[]
        for key in d:
            if d[key]> math.floor(len(nums)/3):
                res.append(key)
        return res
