#Recurrence Relation -> T(n)=T(n/2)+c
#Master's Theorem -> T(n)=O(log n)

#Time complexity T(n/2)
def find_power(a,n):
    #small problem
    if n==1:
        #print('a: ',a)
        return a
    #bigger problem -> Divide & Conquer method
    else:
        mid=n//2
        #print('mid: ',mid)
        b=find_power(a,mid) #T(n/2)
        #print('b: ',b)
        #performing on the both parts
        c=b*b
        #print('c: ',c)
        #checking n is even or odd
        if n%2==0:
            #print('c')
            return c
        else:
            #print('a')
            return c*a

print(find_power(3,5))