class Solution(object):
    def maximumSubarraySum(self, nums, k):
        freq=defaultdict(int)
        window_sum=0
        left=0
        max_sum=0
        for right in range(len(nums)):
            window_sum+=nums[right]
            freq[nums[right]]+=1
            if right-left+1>k:
                window_sum-=nums[left]
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            if right-left+1==k:
                if len(freq)==k:
                    max_sum=max(max_sum, window_sum)
        return max_sum
        