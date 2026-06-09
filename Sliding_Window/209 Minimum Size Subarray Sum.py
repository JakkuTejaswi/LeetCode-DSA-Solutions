class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        min_count=float("inf")
        curr_sum=0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                min_count=min(min_count, right-left+1)
                curr_sum-=nums[left]
                left+=1
        return 0 if min_count==float("inf") else min_count

