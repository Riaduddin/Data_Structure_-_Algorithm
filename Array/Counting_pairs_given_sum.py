def pair_sum(arr,target):
    '''
        T(C):O(N2)
        S(C):0(1)
    '''
    a=len(arr)
    count=0
    for i in range(a-1):
        for j in  arr[i+1:]:
            value=arr[i]+j
            if value==target:
                count+=1
    return count

def pair_sum2(arr,target):
    '''
        T(C): O(N)
        S(C): O(N)
    '''
    set_numbers=set()
    a=len(arr)
    count=0
    # if a==1 and arr[count]==target:
    #     count+=1
    for i in range(a-1):
        value=target-arr[i]
        if value in set_numbers or value==0 or value==arr[i]:
            count+=1
        set_numbers.add(arr[i])
    return count
def pair_sum3(arr,target):
    '''
        T(C):O(nlogn)
        S(C):O(1)
    '''
    arr.sort()
    left=0
    right=len(arr)-1
    count_pairs=0
    while(left<right):
        value=arr[left]+arr[right]
        if value==target:
            count_pairs+=1
            right-=1
            #left+=1
        elif value>target:
            right-=1
        else:
            left+=1
    return count_pairs
array=[[1,5,-1,7,100],[1,2,1,2,1],[-1,-1,1],[1],[1,1,1]]
target_sum=[6,3,0,1,2]
output=2,3,2,1,2
for arr,k in zip(array,target_sum):
    value=pair_sum2(arr,k)
    print(value)

