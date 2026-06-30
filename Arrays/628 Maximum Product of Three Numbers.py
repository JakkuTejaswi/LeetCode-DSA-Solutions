class Solution(object):
    def maximumProduct(self, nums):
        nums=sorted(nums, reverse=True)
        max_pro=max(nums[0]*nums[-1]*nums[-2], nums[0]*nums[1]*nums[2])
        return max_pro
        