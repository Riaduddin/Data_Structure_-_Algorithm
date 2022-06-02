#divide_and_conquer_method
def dac_max_min(arr,low,high):
    max_value=arr[low]
    min_value=arr[low]
    #small_problem
    #number_of_element==1
    if low==high:
        return (max_value,min_value)
    #small_problem
    #number_of_element==2
    elif low==high-1:
        if arr[low]>arr[high]:
            max_value=arr[low]
            min_value=arr[high]
        else:
            max_value=arr[high]
            min_value=arr[low]
        return (max_value,min_value)
    #big problem
    #number_of_element>2
    else:
        mid=low+(high-low)//2
        max_1,min_1=dac_max_min(arr,low,mid) #T(n/2)
        max_2,min_2=dac_max_min(arr,mid+1,high) #T(n/2)
        max_value=max(max_1,max_2)
        min_value=min(min_1,min_2)

        return (max_value,min_value)

arr=[50,90,20,10,15,75,6,95,-6]
low=0
high=len(arr)-1
print(dac_max_min(arr,low,high))