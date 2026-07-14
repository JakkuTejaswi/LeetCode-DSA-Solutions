class Solution:
    def countRevPairs(self, arr):
        self.count=0
        self.mergesort(arr)
        return self.count
    def mergesort(self,arr):
        if len(arr)<=1:
            return arr
        mid=(len(arr))//2
        left=self.mergesort(arr[:mid])
        right=self.mergesort(arr[mid:])
        j=0
        for i in range(len(left)):
            while j<len(right) and left[i]>2*right[j]:
                j+=1
            self.count+=j
        return self.merge(left,right)
    def merge(self,left,right):
        res=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
                
        