def sorting_arr(arr):
    d={0:0,1:0}

    for i in range(len(arr)):
        d[arr[i]]=1+d.get(arr[i])

    count=d.get(0)
    
    for i in range(count):
        arr[i]=0
    value=len(arr)-count+1
    for i in range(len(arr)-count-1):
        #print(i)
        arr[value+i]=1
    # arr[len(arr)-count+1:]=1
    return arr

def sorting_arr_2(arr):
    idx,start=0,0
    while idx<(len(arr)):
        if arr[idx]==0:
            arr[start],arr[idx]=arr[idx],arr[start]
            start+=1
        idx+=1
    return arr
        


arr=[1,0,1,1,0,0]
print(sorting_arr_2(arr))