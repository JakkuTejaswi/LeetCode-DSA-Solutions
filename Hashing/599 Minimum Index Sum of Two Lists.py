class Solution(object):
    def findRestaurant(self, list1, list2):
        d={}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    d[list1[i]]=i+j
        mini=len(list1)+len(list2)
        r=[]
        for key in d:
            if d[key]<mini:
                mini=d[key]
                r=[key]
            elif d[key]==mini:
                r.append(key)

        return r
