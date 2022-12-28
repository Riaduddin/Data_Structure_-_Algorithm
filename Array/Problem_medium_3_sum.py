def three_sum(nums):
    a=[]
    if len(nums)<3:
        return []
    if len(nums)>1:
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    x=nums[i]+nums[j]+nums[k]
                    if x==0:
                        p,q,r=nums[i],nums[j],nums[k]
                        a.append(tuple(sorted((nums[i],nums[j],nums[k]))))
    return list(set(a))

nums=[-1,0,1,2,-1,-4]
print(three_sum(nums))