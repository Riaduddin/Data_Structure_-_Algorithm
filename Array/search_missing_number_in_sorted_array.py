#Different types of test cases
test_cases=[[3,0,1],[0,1],[9,6,4,2,3,5,7,0,1],[0,1,2,3,4,6,7,8,9],[0,1,3]]

output=[2,2,8,5,2]

#Using natural number of summation
#Time complexity O(n)
#Space complecity O(1)
def missingNumber(nums):
    a=len(nums)
    #calculate the summation according to array
    sum=(a*(a+1))/2
    value=0
    for i in nums:
        #summation of actual array
        value+=i
    return sum-value

        


#Using X-OR
#Time complexity O(n)
#Space complecity O(1)
def missingNumber(nums):
    a=len(nums)
    missing=a
    for i in range(0,a):
        missing ^= i ^nums[i]
    return missing




for arr in test_cases:
    value=missingNumber(arr)
    print(value)