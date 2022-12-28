import sys
 
# Function to find the maximum sublist sum using divide-and-conquer
#calculating the sum from top to bottom
def findMaximumSum(nums):
 
    # Find the middle element in the list
    if len(nums)>1:
        mid = len(nums) // 2
        L=nums[:mid]
        R=nums[mid:]
        # Find maximum sublist sum for the left sublist
        leftMax = -sys.maxsize
        total = 0
        for i in range(len(L)-1,-1,-1):
            total += L[i]
            if total > leftMax:
                leftMax = total
    
        # Find maximum sublist sum for the right sublist
        rightMax = -sys.maxsize
        total = 0        # reset sum to 0
    
        for i in range(0,len(R)):
            total += R[i]
            if total > rightMax:
                rightMax = total
    
        # Recursively find the maximum sublist sum for the left
        # and right sublist, and take maximum
        # print(L)
        # print(R)
        # print(leftMax)
        # print(rightMax)
        
        maxLeftRight = max(findMaximumSum(L),
                        findMaximumSum(R))
        print(maxLeftRight)
        # return the maximum of the three
        #calculating the summation of top tree(leftMax+rightMax) to compare them to bottom tree branch
        return max(maxLeftRight, leftMax + rightMax)
    #return the value
    return nums[0]
nums = [2, -4, 1, 9, -6, 7, -3]
#nums=[-2,1,-3,4,-1,2,1,-5,4]
#nums=[5,4,-1,7,8]
#nums=[1]
#nums=[-2,-3,-1]
print('The Maximum sum of the sublist is', findMaximumSum(nums))
# for i in range(len(nums)-1,-1,-1):
#     print(nums[i])