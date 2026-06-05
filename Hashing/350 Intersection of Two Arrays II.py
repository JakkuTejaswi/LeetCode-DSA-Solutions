class Solution(object):
    def intersect(self, nums1, nums2):
        r=[]
        d1={}
        d2={}
        for num in nums1:
            d1[num]=d1.get(num,0)+1
        for num in nums2:
            d2[num]=d2.get(num,0)+1
        for key in d1:
            if key in d2:
                for i in range(min(d1[key], d2[key])):
                    r.append(key)
        return r