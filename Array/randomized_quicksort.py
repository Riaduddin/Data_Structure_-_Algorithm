#dividing the array
import random
def partition(arr,p,q):
    #randomly choosing the index of the array
    m=random.randint(p,q)
    x=arr[m]
    arr[p],arr[m]=arr[m],arr[p]
    i=p
    for j in range(p+1,q+1):
        if arr[j]<x:
            i=i+1
            temp=arr[i]
            #swapping the value
            arr[i],arr[j]=arr[j],arr[i]
    arr[p],arr[i]=arr[i],arr[p]
    return i
#quicksort implementation
def quicksort(arr,p,q):
    #single array
    if p==q:
        return arr[p]
    if p<q:
        mid=partition(arr,p,q)
        #recursive function
        quicksort(arr,p,mid-1)
        quicksort(arr,mid+1,q)

arr=[50,70,80,30,40,88,19,27,69]
quicksort(arr,0,len(arr)-1)
print(arr)
