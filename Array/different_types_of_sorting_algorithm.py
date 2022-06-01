def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    return arr

def insertion_sort(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        j=i-1
        while(j>=0 and value<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=value
    return arr


print(insertion_sort([70,50,20,30,90,3,15]))