#finding the pivot value position
def partition(arr,p,q):
    x=arr[p] #pivot value
    i=p
    for j in range(p+1,q+1):
        if arr[j]<x:
            i=i+1
            temp=arr[i]
            #swapping the value
            arr[i],arr[j]=arr[j],arr[i]
    #swaping with the pivot value
    arr[p],arr[i]=arr[i],arr[p]
    return i

#finding the kth smallest number using quicksort implementation
def selection_procedure(arr,p,q,k):
    #single array
    if p==q:
        return arr[p]
    else:
        #divide the array using the pivot value position
        mid=partition(arr,p,q)
        #recursive function
        if mid==k:
            return arr[k-1] #return the kth smallest element
        elif mid<k:
            return selection_procedure(arr,mid+1,q,k) #recursive call
        elif mid>k:
            return selection_procedure(arr,p,mid-1,k) #recursive call


arr=[50,70,80,30,40,88,19,27,69]
print(selection_procedure(arr,0,len(arr)-1,1))

