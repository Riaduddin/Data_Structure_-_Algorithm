#Binary search algorithm 

#Different types of test cases
test_cases=[[13, 11, 10, 7, 4, 3, 1, 0],
[13, 11, 10, 7, 4, 3, 1, 0],[4, 2, 1, -1],[3, -1, -9, -127],[6],[9, 7, 5, 2, -9],
[],[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]]


query=[3,6,0,3,0,-1,-1,7,2]
output=[7,1,4,-127,6,4,7,3,6]

#Linear Search Algorithm
'''It takes to much time. Time Complexity O(n). Space complexity
    O(1).'''
# def binary_search(arr,x):
#     position=0
#     while position<len(arr):
#         if arr[position]==x:
#             print(position)
#             return position
#         position+=1
#         if position==len(arr):
#             return -1



#binary_search_using_recursion
'''In can not detect the position of the number for the repeated 
    numbers. '''
# def binary_search(arr,lo,hi,x):
#     #For only one variable
#     if len(arr)==1:
#         if arr[lo]==x:
#             return lo
#         else:
#             return -1

#     else:
#         mid=lo+(hi-lo)//2    # calculating middle point

#         if arr[mid]==x:
#             return mid
#         elif arr[mid]<x:
#             return binary_search(arr,lo,mid-1,x) # Recursive call
#         elif arr[mid]>x:
#             return binary_search(arr,mid+1,hi,x) #Recursive call



def test_location(arr,x,mid):
    
    if arr[mid]==x:
        #for detecting the repeated number
        if mid-1>=0 and arr[mid-1]==x:
            return 'left'
        else:
            return 'found'
    elif arr[mid]<x:
        return 'left'
    else:
        return 'right'

def binary_search(arr,x):
    lo,hi=0,len(arr)-1

    while lo<=hi:
        # calculating the middle point
        mid=lo+(hi-lo)//2
        result=test_location(arr,x,mid)
        if result=='found':
            return mid
        elif result=='left':
            hi=mid-1
        else:
            lo=mid+1
    return -1
    
        


# arr=[8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
# lo=0
# hi=len(arr)-1
# x=2
# print(binary_search(arr,lo,hi,x))


for (arr,x,result) in zip(test_cases,output,query):
    value=binary_search(arr,x)
    print(value)






