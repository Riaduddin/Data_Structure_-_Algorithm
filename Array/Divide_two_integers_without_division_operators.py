#divide two integers using '<<' shifting operators instead of
#using any mathematical operators
def division(dividend,divisor):
    #checking the queotient sign
    sign=( -1 if ((dividend<0)^(divisor<0)) else 1)
    count=0
    dividend=abs(dividend)
    divisor=abs(divisor)
    #looping until the dividend value is bigger
    while (dividend-divisor)>=0:
        i=0
        #checking which number of shifting operation is bigger than dividend
        while(dividend-(divisor<<i))>=0:
            i+=1
        #decrease the dividend value to reiterate
        dividend=dividend-(divisor<<(i-1))
        #calculating the number of queotient value
        temp=1<<(i-1)
        #saving the value
        count+=temp
        if dividend==divisor:
            count+=1
            #changing the value to zero
            #not to reiterate one time again
            dividend=dividend-divisor
    queotient=count
    queotient=sign *queotient
    return min(2147483647,max(-2147483648,queotient))
    
 
        
print(division(-2147483648,-1))