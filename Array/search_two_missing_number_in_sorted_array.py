#Different types of cases
test_cases=[[1,2,3,9,8,7,6],[9,4,3,5,7,8,1],[1,2,3,9,8,7,5]]

target=[[4,5],[2,6],[4,6]]


#Using XOR mechanism
#Time complexity O(n)
#Space complexity O(1)
def twomissingNumber(nums):
    a=len(nums)+2
    #calculate the summation according to array
    sum=int(a*(a+1)/2)
    value=0
    for i in nums:
        #summation of actual array
        value+=i
    avg_value=(sum-value)//2
    leftside=0
    rightside=0
    #XOR operation of all value less than the 
    #avg value
    for i in range(1,avg_value+1):
        leftside^=i
    #XOR operation of all value more than the 
    #avg value
    for j in range(avg_value+1,a+1):
        rightside^=j
    for i in range(a-2):
        #XOR operation of less than avg value 
        #in the array
        if nums[i]<=avg_value:
            leftside^=nums[i]
        #XOR operation of more than avg value 
        #in the array
        else:
            rightside^=nums[i]
    #returing the missing number
    return [leftside,rightside]

        

#Brute force Approach/Using Hashing
#Time complexity O(n)
#Space complexity O(n)
def twomissingNumber(nums):
    value=set(nums)
    arr=[]
    for i in range(1,len(nums)+1):
        if i not in value:
            arr.append(i)
    return arr

for arr in test_cases:
    output=twomissingNumber(arr)
    print(output)