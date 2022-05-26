#Different types of cases
test_cases=[1,2,3,9,8,7,6]


def twomissingNumber(nums):
    a=len(nums)
    #calculate the summation according to array
    sum=int(a*(a+1)/2)
    value=0
    for i in nums:
        #summation of actual array
        value+=i
    value=value-sum
    avg=value//2
    for i in range():
        

#Brute force Approach/Using Hashing
# def twomissingNumber(nums):
#     value=set(nums)
#     arr=[]
#     for i in range(1,len(nums)+1):
#         if i not in value:
#             arr.append(i)
#     return arr


print(twomissingNumber(test_cases))