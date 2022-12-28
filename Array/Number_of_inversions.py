def mergesort(arr):
    count=0
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]
        count+=mergesort(L)
        count+=mergesort(R)

        i=j=k=0
        while (i<len(L) and j<len(R)):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
                count+=(len(L)-i)
            k+=1
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    return count


arr=[50,20,40,90,88,11,13]
arr2=[50,84,56,32,97,95,61,5]
arr3=[70,50,60,10,20,30,80,15]
#print(count_inversions(arr3))
print(mergesort(arr2))
#print(arr2)

