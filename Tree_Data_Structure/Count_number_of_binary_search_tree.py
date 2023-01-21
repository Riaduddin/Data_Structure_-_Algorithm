def uniqueNumberBST(n):
    n1, n2, sum = 0, 0, 0
    if n == 0 or n == 1:
        return 1
    print('value')
    for i in range(1, n+1):
        ## Recursive Function Calls for calculating catalan series
        n1 = uniqueNumberBST(i-1)
        n2 = uniqueNumberBST(n-i)
        print(n2)
        sum += n1 * n2
    return sum

print(uniqueNumberBST(3))