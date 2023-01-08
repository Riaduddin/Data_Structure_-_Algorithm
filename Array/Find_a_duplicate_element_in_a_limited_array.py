#TC--->O(N)  SC--->O(N)
def containsDuplicate(nums):
    d={}
    for i in range(len(nums)):
        value=nums[i]
        d[value]=1+d.get(value,0)
        if d.get(value)>1:
            return True
    return False

def containsDuplicate_2(nums):
    n=len(nums)
    total=(n+1)*(n/2)
    sum=0
    for i in range(n):
        sum+=nums[i]
    if sum-total != 0:
        return True
    return False

#using xor function
def containsDuplicate_3(nums):
    n=len(nums)
    missing=0
    for i in range(1,n+1):
        #print(i)
        #print(nums[i])
        missing ^= i^nums[i-1]
    if missing==0:
        return False
    else:
        return True
    #return missing
arr=[1,2,3,2]
print(containsDuplicate_3(arr))