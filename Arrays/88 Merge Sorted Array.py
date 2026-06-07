class Solution(object):
    def merge(self, nums1, m, nums2, n):
        j=m
        for i in range(n):
            nums1[j]=nums2[i]
            j+=1
        nums1.sort()
        return nums1