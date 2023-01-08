def length_of_maximum_subarray(arr,k):
    # count=0
    prefix_sum=0
    d={0:-1}
    count=0
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        diff=prefix_sum-k
        #print(d.keys())
        if diff in d.keys():
            count=max(d.get(diff,0),i+1-d.get(diff,0))
            # d[prefix_sum]=i
            # continue
        d[prefix_sum]=i
        #print(d)
    return count

arr=[5,6,-5,5,3,5,3,2,0]
arr2=[1,0,1,1,1,1,1]
arr3=[1, -2, 1, 1, -2, 1]
target_sum=[2]
print(length_of_maximum_subarray(arr3,0))