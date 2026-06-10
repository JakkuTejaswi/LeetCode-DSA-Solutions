class Solution(object):
    def removeDuplicates(self, nums):
        n=len(nums)
        k=2
        if n<=2:
            return n
        for i in range(k,n):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k



        