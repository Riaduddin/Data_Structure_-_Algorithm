#Different_types_of_casestest_case
value=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
value2=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]




def search_matrix(arr,target):
    i=0
    #number of columns
    j=len(arr[0])-1
    #number of rows
    n=len(arr)
    #Time complexity O(n)
    while i<n:
        if arr[i][j]==target:
            return print("row:",i,'col:',j)
        elif arr[i][j]<target:
            #increase the rows number 
            i=i+1
        elif arr[i][j]>target:
            #reducing the columns
            j=j-1
    #donot find the target value
    return 0


search_matrix(value2,23)
