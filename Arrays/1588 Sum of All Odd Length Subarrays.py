class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        odd_len=[i for i in range(1, len(arr)+1) if i%2!=0]
        sum=0
        for odd in odd_len:
            curr_sum=0
            l=0
            for right in range(l, len(arr)):
                curr_sum+=arr[right]
                if right-l+1==odd:
                    sum+=curr_sum
                    curr_sum-=arr[l]
                    l+=1
        return sum

