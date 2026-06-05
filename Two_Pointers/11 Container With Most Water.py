class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        max_area=0
        while l<r:
            h=min(height[l],height[r])
            b=r-l
            area=b*h
            max_area=max(area,max_area)
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:
                r-=1
            else:
                l+=1
                r-=1
        return max_area
        