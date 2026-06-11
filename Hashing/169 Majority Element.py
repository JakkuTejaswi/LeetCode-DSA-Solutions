class Solution(object):
    def majorityElement(self, nums):
        d={}
        for num in nums:
            d[num]=d.get(num,0)+1
        for key in d:
            if d[key]>(len(nums)//2):
                return key
        