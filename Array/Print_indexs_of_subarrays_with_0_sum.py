#Brute-force approach
def print_all_subarrays_with_0_sum(arr):

    for i in range(len(arr)):
        total=0
        for j in range(i,len(arr)):
            total+=arr[j]
            if total==0:
                print('Sublist:',(i,j))

def printallSublist(arr):
    # insert (0, -1) pair into the dictionary to handle the case when
    # sublist with zero-sum starts from index 0
    d={0:[-1]}
    total=0
    for i in range(len(arr)):
        total+=arr[i]
        if total in d:
 
            list = d.get(total)
 
            # find all sublists with the same sum
            for value in list:
                print('Sublist is', (value + 1, i))
        d.setdefault(total,[]).append(i)


arr=[4,2,-3,-1,0,4]
print_all_subarrays_with_0_sum(arr)
#printallSublist(arr)