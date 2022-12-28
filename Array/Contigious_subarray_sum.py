#contgious subarray(not taking any random position of value)
def subarray(arr,k):
    set_numbers={0:1}
    count,sum=0,0
    for i in range(len(arr)):
        print(i)
        sum=sum+arr[i]
        diff=sum-k
        count+=set_numbers.get(diff,0)
        set_numbers[sum]=1+set_numbers.get(sum,0)
    return count
        

test_cases=[[1,2,1,2,1],[1,2,3]]
target_sum=[3,3]
output=4,2
for arr,k in zip(test_cases,target_sum):
    print(subarray(arr,k))