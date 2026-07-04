class Solution(object):
    def findMaxLength(self, nums):
        prefix_sum=0
        max_len=0
        prefix_map={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                prefix_sum-=1
            else:
                prefix_sum+=1
            if prefix_sum in prefix_map:
                max_len=max(max_len, i-prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum]=i
        return max_len
        