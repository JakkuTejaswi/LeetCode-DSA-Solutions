class Solution(object):
    def minimumDifference(self, nums, k):
        left=0
        nums.sort()
        ans=float("inf")
        if k==1:
            return 0
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans


        




        