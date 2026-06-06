class Solution(object):
    def searchRange(self, nums, target):
        def FirstOccur():
            left, right=0, len(nums)-1
            ans=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    ans=mid
                    right=mid-1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return ans
        def LastOccur():
            left, right=0, len(nums)-1
            ans=-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                    ans=mid
                    left=mid+1
                elif nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return ans
        return [FirstOccur(), LastOccur()]
        