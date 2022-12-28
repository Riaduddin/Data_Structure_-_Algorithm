def checkingzerosum(arr):
    '''
        T(C): O(N)
        S(C): O(N)
    '''
    total_subarray=list()
    initial=0
    for i in range(len(arr)-1):
        value=initial+arr[i]
        if value in total_subarray:
            return True
        total_subarray.append(value)
        initial=value
    if 0 in total_subarray:
        return True
    return False

array=[4,2,-3,1,7]
print(checkingzerosum(array))