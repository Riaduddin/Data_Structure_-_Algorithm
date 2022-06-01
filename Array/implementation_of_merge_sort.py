
def mergesort(arr):
    #moving top to bottom in a Recursive Tree
    if len(arr)>1:
        #finding the mid of the array
        mid=len(arr)//2
        #dividing the array into two halves
        #left subtree
        L=arr[:mid]
        #right subtree
        R=arr[mid:]
        #sorting the first half(left_tree)
        mergesort(L) #recursive call
        #sorting the second half(right_tree)
        mergesort(R) #recursive call
        #move from bottom to top by applyling merge procedure
        i=j=k=0
        while (i<len(L) and j<len(R)):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1
        #checking if any element was missed in left_tree
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1
        #checking if any element was missed in right_tree
        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1

arr=[50,20,40,90,88,11,13]
print(arr)
mergesort(arr)
print(arr)