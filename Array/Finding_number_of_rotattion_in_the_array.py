#Different types of test_cases where all numbers are unique
test_cases=[[17,18,28,1,3,9,10],[11,13,14,15,2,7,9],[2,7,11,13,14,15,19],
[7,9,10,4],[4,7,9,10],[],[5],[13,19,21,26,29,33,35,43,45,13,2,7]]

#Desired output
output=[3,4,0,3,0,0,0,10]

#Linear Search Algorithm
#Time complexity O(n)
# def count_rotations(arr):
#     i=0
#     while i < len(arr):
#         if arr[i]<arr[i-1] and i>0:
#             return i
#         i+=1
#     return 0


#Binary_search_Algorithm
#Time complexity O(logn)
def count_rotations(arr):
    i,j=0,len(arr)-1
    while i<=j:
        #calculating middle number
        mid=i+(j-i)//2
        if arr[mid]<arr[mid-1]:
            return mid
        elif arr[mid]>arr[j]:
            #search reduce by N/2
            i=mid+1
        elif arr[mid]<arr[j]:
            #search reduce by N/2
            j=mid-1
        elif i==j:
            #one element
            #i increases to last element
            return i
    #finding no rotation
    return 0





for arr in test_cases:
    value=count_rotations(arr)
    print(value)