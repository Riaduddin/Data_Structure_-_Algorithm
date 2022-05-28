
# def division(dividend,divisor):
#     count=0
#     while dividend>=divisor:
#         dividend=dividend-divisor
#         count+=1
#     return count
        
def division(dividend,divisor):
    count=0
    while (dividend-divisor)>=0:
        i=0
        while(dividend-(divisor<<i))>=0:
            i+=1
        dividend=dividend-(divisor<<(i-1))
        temp=1<<(i-1)
        count+=temp
        if dividend==divisor:
            count+=1
            dividend=dividend-divisor
    queotinent=count
    return queotinent
    



    
        
print(division(1586,3))

#print(division(57,13))
# value=0
# value=1<<5
#print(1<<2)
#print(value)
#print(2<<2)
#print(value)