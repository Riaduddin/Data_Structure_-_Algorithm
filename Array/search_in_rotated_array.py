#Different types of test cases
test_cases=[[4,5,6,7,0,1,2],[1],[],[1,2,3,4,6,8],[7,9,10,4],[12,14,19,21,32,1,3,5,7,9,10],[5,1,3],[3,1]]

targets=[0,0,8,6,10,9,5,3]
output=[4,-1,-1,4,2,9,0,0]

#Time complexity O(logn)
#space comlexity O(1)
def search(arr,target):
    i,j=0,len(arr)-1
    while i<=j:
        mid=i+(j-i)//2
        #for one element
        #for the last element
        if i==j:
            if arr[i]==target:
                return i
            else:
                return -1
        elif arr[mid]==target:
            return mid
        #Check condition for selecting left or right of 
        #sorted array
        elif arr[i]<=arr[mid]:
            if arr[i]<=target<arr[mid]:
                #select the left side
                j=mid-1
            else:
                #select the right side
                i=mid+1
        else:
            if arr[mid]<target<=arr[j]:
                #select the right side
                i=mid+1
            else:
                #select the left side
                j=mid-1
    return -1


for arr,target in zip(test_cases,targets):
    value=search(arr,target)
    print(value)
    