class Solution(object):
    def intersection(self, nums1, nums2):
        r=[]
        for num in nums1:
            if num in nums2 and num not in r:
                r.append(num)
        return r

        