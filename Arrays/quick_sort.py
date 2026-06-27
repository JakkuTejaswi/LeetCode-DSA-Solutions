def quicksort(arr, low, high):
    if low<high:
        pivot=partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)
    return arr
def partition(arr, low, high):
    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while i<=high and arr[i]<=pivot:
            i+=1
        while j>=low and arr[j]>pivot:
            j-=1
        if i<j:
            arr[i], arr[j]=arr[j], arr[i]
        else:
            break
    arr[low], arr[j]=arr[j], arr[low]
    return j
arr=[2,1, 6 ,5,4, 8]
print(quicksort(arr,0, len(arr)-1))